# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Alex Rusu"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101314298"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-113"


import matplotlib.pyplot as plt

#==========================================#
# Place your histogram function after this line
def histogram(lst: list[dict], attribute: str): 
    """Graph a histogram of the given values and attribute
    
    histogram([{'Strength':'13'},{'Strength':'13'}], 'Strength')
    >>>{'13': 2}
    
    histogram([{'Occupation': 'H','Armor':10},{'Occupation': 'E','Armor':11},{'Occupation': 'R','Armor':12}], "Occupation")
    >>>{'H': 1, 'E': 1, 'R': 1}
    
    """
     
    result_dict = {}
    
    for dictionary in lst:
        
        if dictionary[attribute] in result_dict:
            result_dict[dictionary[attribute]] += 1
        else:
            result_dict[dictionary[attribute]] = 1
    
    #print(result_dict)
    
    xaxis = list(result_dict.keys())
    yaxis = list(result_dict.values())
    
    attribute_num = -1
    
    fig = plt.figure()

    if isinstance(xaxis[0], (int, float)):
        max_value = max(xaxis)
        attribute_num = max_value
        interval = max_value / 20
        new_yaxis = []

        for i in range(21):
            new_yaxis.append(i*interval)

        plt.yticks(new_yaxis)
        plt.bar(xaxis, yaxis)  
    else:
        plt.bar(xaxis, yaxis)
       
    
    plt.title("Histogram of "+attribute)    
    plt.xlabel(attribute)
    plt.ylabel("Frequency")  
    plt.show()        
    
    
    return attribute_num    
                
    

# Do NOT include a main script in your submission

#histogram([{'Strength':'13'},{'Strength':'13'}], 'Strength')

#histogram([{'Occupation': 'H','Armor':14},{'Occupation': 'E','Armor':11},{'Occupation': 'R','Armor':12}], "Armor")
