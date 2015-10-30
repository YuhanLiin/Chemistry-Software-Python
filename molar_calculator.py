from find_element import *
corpus = p_table().table
avgro = 6.022e+23

while 1==1:
    compound = raw_input("Enter compound: ")
    elem = find_elements(1, corpus, compound)
    print ''
    print str(molar_mass(elem)) + 'g/mol.'
   
    while 1==1:
        print '##################################################################'
        print ''
        t_grams, t_atoms = 0, 0
        print "Question types:"
        print "1. Given # of moles, find mass or # of molecules."
        print "2. Given # of molecules, find mass or # of moles."
        print "3. Given mass, find # of moles or # of molecules."
        print "4. Given atoms, find moles, molecules, and mass."
        choice = raw_input("Choose by entering the question number. Press any other key to go back: ")
        print ''

        if choice == '1':
            moles = float(raw_input("Enter # of moles: "))
            for e in elem:
                print e + ": " + str(moles*elem[e]) + " moles, " + str(moles*elem[e]*avgro) + " atoms."
                print "Mass: " + str(moles*elem[e]*corpus[e]["Atomic mass"]) + "g."
                t_grams += elem[e]*corpus[e]["Atomic mass"]
                t_atoms += elem[e]
            print ''
            print "Atoms per molecule: " + str(t_atoms)
            print "Total # of molecules: " + str(moles*avgro)
            print "Total mass: " + str(moles*t_grams) + "g"
            print "Total # of atoms: " + str(moles*avgro*t_atoms)+'\n'

        elif choice == '2':
            molecules = float(input("Enter total # of molecules, using Python scientific notation if necessary: (6e+02 means 6 times 10 to the power of 2 in Scientific Notation): "))
            moles = molecules/avgro
            for e in elem:
                print e + ": " + str(moles*elem[e]) + " moles, " + str(moles*elem[e]*avgro) + " atoms."
                print "Mass: " + str(moles*elem[e]*corpus[e]["Atomic mass"]) + "g."
                t_grams += elem[e]*corpus[e]["Atomic mass"]
                t_atoms += elem[e]
            print ''
            print "Atoms per molecule: " + str(t_atoms)
            print "Total # of " + compound + " moles: " + str(moles)
            print "Total mass: " + str(moles*t_grams) + "g"
            print "Total # of atoms: " + str(molecules*t_atoms)+"\n"

        elif choice == '3':
            mass = float(input("Enter mass in grams: "))
            for e in elem:
                t_grams += elem[e]*corpus[e]["Atomic mass"]
            moles = mass/t_grams
            for e in elem:
                print e + ": " + str(moles*elem[e]) + " moles, " + str(moles*elem[e]*avgro) + " atoms."
                print "Mass: " + str(moles*elem[e]*corpus[e]["Atomic mass"]) + "g."
                t_atoms += elem[e]
            print ''
            print "Atoms per molecule: " + str(t_atoms)
            print "Total # of " + compound + " moles: " + str(moles)
            print "Total # of molecules: " + str(moles*avgro)
            print "Total # of atoms: " + str(moles*avgro*t_atoms)+"\n"

        elif choice == '4':
            atoms = int(input('Enter # of atoms: '))
            for e in elem:
                t_atoms += elem[e]
            moles = (atoms/t_atoms)/avgro
            for e in elem:
                print e + ": " + str(moles*elem[e]) + " moles, " + str(moles*elem[e]*avgro) + " atoms."
                print "Mass: " + str(moles*elem[e]*corpus[e]["Atomic mass"]) + "g."
                t_grams += elem[e]*corpus[e]["Atomic mass"]
            print ''
            print "Atoms per molecule: " + str(t_atoms)
            print "Total # of " + compound + " moles: " + str(moles)
            print "Total mass: " + str(moles*t_grams) + "g"
            print "Total # of molecules: " + str(moles*avgro)+"\n"



        else: break
            
      
        


