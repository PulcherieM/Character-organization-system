# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Carmen Pan, Alex Rusu, Pulcherie Mbaye, Agi Louis"

# Update "" with your team (e.g. T102)
__team__ = "T113"

#==========================================#
# Place your sort_characters_agility_bubble function after this line
def sort_characters_agility_bubble (list_agility: list[dict], order: str) -> list[dict]:
    """
    Returns an ordered list in ascending or descending order based on the letter passed to the function
    
    Precondition: A sting and a letter A or D must be passed to the function
    
    >>>sort_characters_agility_bubble({'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 13, 'Agility': 3, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
 'Armor': 8, 'Weapon': 'Staff'}, "A")
 
 {'Occupation': 'AT', 'Strength': 13, 'Agility': 3, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
 'Armor': 8, 'Weapon': 'Staff'}
 
 >>>sort_characters_agility_bubble({'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 13, 'Agility': 3, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
 'Armor': 8, 'Weapon': 'Staff'}, "D")
 
 {'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 13, 'Agility': 3, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
 'Armor': 8, 'Weapon': 'Staff'}
 
    
    """
    empty = []
    for line in list_agility:  
        if 'Agility' not in line:
            print ('"Agility" key is not present')
            return list_agility
    
        elif list_agility == []:
            return empty
    
        if order == 'A':
            swap = True
            while swap:
                swap = False
                for i in range(len(list_agility) - 1 ):
                    if list_agility[i]['Agility'] > list_agility[i+1]['Agility']:
                        store = list_agility[i]
                        list_agility[i] = list_agility[i + 1]
                        list_agility[i + 1] = store
                        swap = True 
    
        elif order == 'D':
            swap = True
            while swap:
                swap = False
                for i in range(len(list_agility) - 1 ):
                    if list_agility[i]['Agility'] < list_agility[i+1]['Agility']:
                        store = list_agility[i]
                        list_agility[i] = list_agility[i + 1]
                        list_agility[i + 1] = store
                        swap = True     
    
    
                
                
                
                
    return list_agility

#==========================================#
# Place your sort_characters_intelligence_selection function after this line
def sort_characters_intelligence_selection(value: list[dict], inputs: str)-> list:
    
    """ The function uses Sorting algorithm to return a list of Intelligence key, values in a list. If “Intelligence” is a key in the dictionary, the function returns the sorted list. If “Intelligence” is not a key in the dictionary, the function prints a message stating the key is not in the dictionary
    precondition: The second parameter must be "A" or "D"
    
    >>> sort_characters_intelligence_selection([{'Occupation': 'EB', 'Intelligence': 9}, {'Occupation': 'H', 'Intelligence': 12}], "D")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB', 'Intelligence': 9}]
    
    >>> sort_characters_intelligence_selection([{'Occupation': 'EB', 'Intelligence': 9}, {'Occupation': 'H', 'Intelligence': 12}], "A")
    [{'Occupation': 'EB', 'Intelligence': 9}, {'Occupation': 'H', 'Intelligence': 12}]
    
    >>> sort_characters_intelligence_selection([{'Occupation':'EB'}, {'Occupation': 'M'}], "D")
    "Intelligence" key is not present
    [{'Occupation': 'EB'},{'Occupation': 'M'}]

    """
    
   # check to see if intelligence is in the dict that is in the list
    
    for i in value: # we set i in value, so like i is each dictionary in the list, when we run that for loop each i is a dictionary
        if 'Intelligence' in i.keys(): # if string intelligence . if intelligence is in the dictionary
            if inputs =='A':
                for i in range(len(value)):
                    min_idx = i
                    for j in range(i+1, len(value)):
                        if value[min_idx]['Intelligence'] > value[j]['Intelligence']:
                            min_idx = j
                    value[i],value[min_idx] = value[min_idx], value[i]
           
            
            elif  inputs =='D':
                for i in range(len(value)):
                    max_idx = i
                    for j in range(i+1, len(value)):
                        if value[max_idx]['Intelligence'] < value[j]['Intelligence']:
                            max_idx = j
                    value[i],value[max_idx] = value[max_idx], value[i]
                    
        else:
            print(' "Intelligence" key is not present')
            return value
        
    return value #so that the values we want to print get printed


#==========================================#
# Place your sort_characters_health_insertion function after this line
def sort_characters_health_insertion (arr: list, sortorder: str) -> None: 
    """
    Return a sorted list of dictionaries by the "Health" key value using insertion sort in the given sorting order.
    Preconditions: list must exist, should enter a sort order. 
   
   >>>sort_characters_health_insertion([{'Occupation': 'EB',
   'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "A")
   [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health':
   62.71}]
   >>>sort_characters_health_insertion([{'Occupation':'EB'},
    {'Occupation': 'M'}], "A")
   "Health" key is not present
   [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    """
    for a in range(len(arr)):
        if "Health" not in arr[a]:
            print("'Health' key is not present in the dictionaries.")
            return arr 
      
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((sortorder == "A" and arr[j]["Health"] > key["Health"]) or (sortorder == "D" and arr[j]["Health"] < key["Health"])):
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
   
    return arr

#==========================================#
# Place your sort_characters_armor_bubble function after this line

def sort_characters_armor_bubble(lst: list[dict], string: str) -> list[dict]:
    """Returns a list with the armor values sorted
    
    Preconditions: lst must be a list of dictionaries
                   string must be one of the keys in the dictionaries
                   
            
    >>>sort_characters_armor_bubble([{'Occupation': 'H'},{'Occupation': 'H'}], "D")
    "Armor" key is not present.
    
    
    >>>sort_characters_armor_bubble([{'Occupation': 'H','Armor':10},{'Occupation': 'H','Armor':11},{'Occupation': 'H','Armor':12}], "D")
    [{'Occupation': 'H', 'Armor': 12}, {'Occupation': 'H', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]
    
    
    
    
    >>>sort_characters_armor_bubble([{'Occupation': 'H','Armor':10},{'Occupation': 'H','Armor':11},{'Occupation': 'H'}], "D")
    "Armor" key is not present.
    """
    
    swap = True
    n_list = []
   
    
    
    for i in range(len(lst)):
        
        if lst[i].get("Armor") == None: 
            
            print("\"Armor\" key is not present.")
            return lst            
              
        
    while swap:
        
        swap = False

        for i in range(len(lst) - 1):    
            
            if lst[i]['Armor'] > lst[i+1]['Armor']:
                        
                aux = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = aux
                swap = True        
        
    
    
    if string == "D":
        #n_list = lst[len(lst)::-1]
        
        #lst = n_list
        
        swap = True
        
        while swap:
            
            swap = False
    
            for i in range(len(lst) - 1):    
                
                if lst[i]['Armor'] < lst[i+1]['Armor']:
                            
                    aux = lst[i]
                    lst[i] = lst[i+1]
                    lst[i+1] = aux
                    swap = True          
    
    return lst


#==========================================#
# Place your sort function after this line

def sort(list_dict: list[dict], sort_order: str, attribute: str)-> None: 
    """Return a sorted list of dictionaries based on a specified attribute and order.
    Preconditions: list of dictionary exists, the sort order is given and attribute is given. 
    >>> sort([{'Occupation': 'EB', 'Agility': 13},
    {'Occupation': 'H', 'Agility': 11}], "D", "Agility")
    [{'Occupation': 'EB', 'Agility': 13},
    {'Occupation': 'H', 'Agility': 11}]
    >>>sort([{'Occupation': 'EB', 'Agility': 13},
     {'Occupation': 'H', 'Agility': 11}], "A", "Stamina"))
    Cannot be sorted by " Stamina "
    [{'Occupation': 'EB', 'Agility': 13},
    {'Occupation': 'H', 'Agility': 11}]
    """
    
    characters = []
    if attribute == 'Agility':
        characters = sort_characters_agility_bubble(list_dict, sort_order) 
    elif attribute == 'Intelligence':
        characters = sort_characters_intelligence_selection(list_dict, sort_order)
    elif attribute == 'Health':
        characters = sort_characters_health_insertion(list_dict, sort_order)
    elif attribute == 'Armor':
        characters = sort_characters_armor_bubble(list_dict, sort_order)
    else: 
        print("Cannot be sorted by" + attribute) 
    return characters 
    

# Do NOT include a main script in your submission


