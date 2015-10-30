from find_element import *
from GCF import gcf
corpus = p_table().table

def formula_to_pc(formula):
    total_mass = 0.0
    cpnd = find_elements (1, corpus, formula)
    for e in cpnd:
        mass = corpus[e]['Atomic mass']*cpnd[e]
        total_mass += mass
        cpnd[e] = mass
    for e in cpnd:
        cpnd[e] = (cpnd[e]/total_mass)*100
    return cpnd

def m_to_e(m_formula):
    cpnd = find_elements (1, corpus, m_formula)
    m_subscripts = [cpnd[e] for e in cpnd]
    e_subscripts = [s/gcf(m_subscripts) for s in m_subscripts]
    i = 0
    for e in cpnd:
        cpnd[e] = e_subscripts[i]
        i+=1
    return cpnd

def mass_e_to_m(mass, e_formula):
    cpnd = find_elements (1, corpus, e_formula)
    total_mass = 0.0
    for e in cpnd:
        total_mass += corpus[e]['Atomic mass']*cpnd[e]
    coe = int(round(mass/total_mass))
    for e in cpnd:
        cpnd[e] = cpnd[e]*coe
    return cpnd

def masses_to_pc(masses):
    total_mass = float(sum([masses[e] for e in masses]))
    print total_mass
    for e in masses:
        masses[e] = masses[e]/total_mass*100
    return masses

def pc_to_e(pc):
    smallest = float('INF')
    for e in pc:
        pc[e] = pc[e]/corpus[e]['Atomic mass']
        if pc[e] < smallest:
            smallest = pc[e]
    coe = []
    for e in pc:
        pc[e] = round(pc[e]/smallest, 2)
        deci = str(pc[e])[-2:]
        if deci[0] == '.':
            deci = int(deci[1]+'0')
        else:
            deci = int(deci)
        if deci in range(83,86):
            coe.append(6)
        elif deci in range(78,83):
            coe.append(5)
        elif deci in range(72,78):
            coe.append(4)
        elif deci in range(65,72):
            coe.append(3)
        elif deci in range(56,65):
            coe.append(5)
        elif deci in range(46,56):
            coe.append(2)
        elif deci in range(36,46):
            coe.append(5)
        elif deci in range(28,36):
            coe.append(3)
        elif deci in range(23,28):
            coe.append(4)
        elif deci in range(18,23):
            coe.append(5)
        elif deci in range(14,18):
            coe.append(6)
        else:
            coe.append(1)
    for e in pc:
        pc[e] = int(round(max(coe)*pc[e]))
    return pc

while True:
     print "Question types:"
     print "1. Given the chemical formula, find percentage composition."
     print "2. Given percentage composition, find empirical formula."
     print "3. Given molecular formula, find empirical formula."
     print "4. Given empirical formula and molar mass, find molecular formula."
     print "5. Given masses of elements find percentage composition and empirical formula."
     choice = raw_input("Enter question number: ")
     print ''
     
     if choice == '1':
         cpnd = raw_input('Enter formula: ')
         pc = formula_to_pc(cpnd)
         print ''
         for e in pc:
             print e+': '+str(pc[e])+'%.'
             
     elif choice == '2':
         n, pc, e_formula = int(raw_input('Enter number of elements: ')), {}, ''
         for i in range(n):
             e = raw_input('Enter element: ')
             p = int(raw_input('Enter percent composition: '))
             pc[e] = p
         emp = pc_to_e(pc)
         for e in emp:
             e_formula += e+str(emp[e])+' '
         print ''
         print "Empirical formula, in no particular order: "+e_formula
         
     elif choice == '3':
         m, e_formula = raw_input('Enter molecular formula: '), ''
         emp = m_to_e(m)
         for e in emp:
             e_formula += e+str(emp[e])+' '
         print ''
         print "Empirical formula, in no particular order: "+e_formula
         
     elif choice == '4':
         emp = raw_input('Enter empirical formula: ')
         mass, m_formula = float(raw_input('Enter molar mass in grams: ')), ''
         m = mass_e_to_m(mass, emp)
         for e in m:
             m_formula += e+str(m[e])+' '
         print ''
         print 'Molecular formula, in no particular order: '+m_formula

     elif choice == '5':
         n, masses, e_formula = int(raw_input('Enter number of elements: ')), {}, ''
         for i in range(n):
             e = raw_input('Enter element: ')
             mass = float(raw_input('Enter mass in grams: '))
             masses[e] = mass
         print ''
         pc = masses_to_pc(masses)
         for e in pc:
             print e+': '+str(pc[e])+'%.'
             
         emp = pc_to_e(pc)
         for e in emp:
             e_formula += e+str(emp[e])+' '
         print "Empirical formula, in no particular order: "+e_formula
         
     print "\n####################################################################\n"
    
     
