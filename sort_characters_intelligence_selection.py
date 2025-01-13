# ECOR 1042 Lab 5 - Individual submission for sort_characters_intelligence_selection function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Rami Sabouni)
__author__ = "Pulcherie Mbaye"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101302394"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-113"

#======= ===================================#
# Place your sort_characters_intelligence_selection function after this line

# the function uses selection sort to sort the list of characters by the intelligence attribute

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
           
        




# Do NOT include a main script in your submission
