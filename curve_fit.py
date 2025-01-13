=====================#
# Place your curve_fit function after this line
import numpy as np
import matplotlib.pyplot as plt
def curve_fit(list_dict: list[dict], attribute: str, degree: int)->str:
    """
    Precondition: Return the equation of a curve that best fits when given a data set.
    
    Parameters:
    - list_dict(list[dict]): A list of dictionaries representing data points. Each dictionary
    contains key "Health" and the specified attribute.
    - attribute(str): Another key whos value will be compared to Health's value.
    - degree(int): The degree of the polynomial curve to fit the data.

    Return Value:
    - str: A string representing the equation of the polynomial curve.
           The equation is in the form 'y = ax^n + bx^(n-1) + ... + cx + d'. Where d is a constant.
           
    Examples:
    >>>curve_fit([{"Health": 4, "Stamina": 1}, {"Health": 9, "Stamina": 2}, {"Health": 16, "Stamina": 3}], "Stamina", 3)
        'y= 1.0x^2 + 2.0x + 1.0'
    >>>curve_fit([{"Health": 7, "Stamina": 0}, {"Health": 0, "Stamina": 1}, {"Health": -9, "Stamina": 2}, {"Health": 4, "Stamina": 3]), "Stamina", 5)
        'y = 4.0x^3 - 13.0x^2 + 2.0x + 7.0'
    >>>curve_fit([{"Health": 3, "Stamina": 0}, {"Health": 4, "Stamina": 1}, {"Health": 5, "Stamina": 2}], "Stamina", 1)
         'y= 1.0x + 3.0'
    """


    levels = {}
    for character in list_dict:
        level = character[attribute]
        health = character['Health']
        if level not in levels:
            levels[level] = [health]
        else:
            levels[level].append(health)
    x = list(levels.keys())
    y = []
    for key in x:
        y.append(np.mean(levels[key]))
    
    if len(x)-1< degree:
        degree_final = len(x)-1
    else:
        degree_final = degree
    
    z = np.polyfit(x, y, degree_final)
    
    equation = 'y = '
    power = degree_final
    for coef in z:
        coef = round(coef, 2)
        if power == 1:
            equation += ' +' + str(coef) + ' x '
        elif power == 0:
            equation += ' + ' + str(coef)
        elif power == degree_final:
            equation += str(coef)+ ' x^'+str (power)
        else:
            equation += ' + ' + str(coef)+' x^'+str (power)
        power -= 1
    
    
    return equation
    # Do NOT include a main script in your submission



