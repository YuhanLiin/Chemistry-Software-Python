from p_table import *
corpus = p_table().table

def addto(dicto, key, value):
    #Adds number to dictionary values based on key
    if key in dicto:
        dicto[key] += value
    else: dicto[key] = value
    
def find_elements (multiplier, index, compound):
    #Takes a compound in string form and returns the number of each element inside a element:count dictionary
    elements = {}
    
    while compound != '':
        polyatomic = False
        
        if compound[0] == '(':
            polyatomic = True
            endbracket = compound.find(')')
            chemical = compound[1:endbracket]
            compound = compound[endbracket+1:]
            
        else:
            for n in range(3,0,-1):
                if compound[:n] in index:
                    chemical = compound[:n]
                    compound = compound[n:]
                    break
            
        subscript = ''
        while compound != '':
            if compound[0] >= '0' and compound[0] <= '9':
                subscript += compound[0]
                compound = compound[1:]
            else: break
        if subscript == '':
            subscript = '1'
        subscript = int(subscript)

        if polyatomic:
            polyion = find_elements (multiplier*subscript, index, chemical)
            for e in polyion:
                addto(elements, e, polyion[e])
        else:
            addto(elements, chemical, multiplier*subscript)
    return elements

def molar_mass (elements):
    #Takes output dictionary of previous function and finds molar mass of the compound using database
    total = 0
    for e in elements:
        total += elements[e]*corpus[e]["Atomic mass"]
    return total

        
