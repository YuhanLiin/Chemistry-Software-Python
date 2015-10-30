from find_element import *
corpus = p_table().table

while True:
    print "Enter given compound:"
    cpnd = raw_input()
    print "Enter its coefficient:"
    coe = int(raw_input())
    given = (coe, cpnd)
    choice = raw_input('Given mass or moles? ')

    if choice == 'mass':
        mass = float(raw_input('Enter mass in grams: '))
        mm = molar_mass(find_elements(coe, corpus, cpnd))
        ratio = mass/mm

    elif choice == 'moles':
        moles = float(raw_input('Enter # of moles: '))
        ratio = moles/coe
        
    while True:
        print ''
        print "Enter required compound:"
        cpnd = raw_input()
        print "Enter its coefficient:"
        coe = int(raw_input())
        req = (coe, cpnd)
        choice = raw_input('Find mass or moles? ')

        if choice == 'mass':
            mm = molar_mass(find_elements(coe, corpus, cpnd))
            print 'Mass of ' + cpnd + ' is ' + str(ratio*mm)

        elif choice == 'moles':
            print str(ratio*coe) + ' moles of ' + cpnd
        
        print ''
        new = raw_input('New given? (Y or N): ')
        if new == 'Y':
            print '##################################################'
            break
    
        
        
        
    
    
