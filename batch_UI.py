
#==========================================#
# Place your script for your batch_UI after this line

from load_data import *
from sort import *
from histogram import * 
import curve_fit
import numpy as py
import matplotlib.pyplot as plt

"""
This function implements a batch user interface for processing data based on commands in a file.

  It expects a file containing commands separated by semicolons (";"). Each command line should be formatted as:

  - First element: Function identifier (one character)
    - "L": Load data from a CSV file.
    - "S": Sort the loaded data.
    - "C": Perform curve fitting on the loaded data (implementation not provided in this example).
    - "H": Create a histogram for the loaded data.
    - "E": Exit the program.
  - Second element (optional for "L"): Name of the CSV file to load.
  - Third element (optional for "L"): Column name to load (default: "All").
  - Fourth element (optional for "S" and unused in others): Ordering direction ("A" for ascending, "D" for descending).
  - Fifth element (optional for "S"): Flag to print the sorted data ("Y" to print, anything else to skip).

  The function reads the file line by line, parses the commands, and calls the corresponding functions with the extracted parameters.
  
  >>>Please enter the name of the file where your commands are stored
: <the user enters response>
Data loaded
Data sorted. <<<You selected not to display>>>
<<<Histograms with Study time will be shown>>>

  """

filename = input("Please enter name of files with commands: ")

with open (filename, "r") as input_file:
    inputfilelines = input_file.readlines()

for line in range (len(inputfilelines)):
    inputfilelines[line] = inputfilelines[line].strip().split(";")

meow = load_data('characters-mat.csv',  ('All', -1))
def Load(lst):
    input_list = load_data(lst[1], (lst[2], lst[3]))
    print("Data Loaded")
    
def Sort(lst):
    meow_list = sort(meow, lst[2], lst[1])
    print("Data Sorted") 
    if lst[3] == 'Y': 
        print(meow)
        
def CurveFit(lst):
    woof_list = curve_fit(meow, lst[1], lst[2])
    
    
def Histogram(lst):
    histogram(meow, lst[1])


def Exit(lst):
    exit(1)
    
def batch_UI() -> None:
    
     
    functions = {"L": Load,
                 "S": Sort, 
                 "C": CurveFit, 
                 "H": Histogram, 
                 "E": Exit
                 }

            
    for line in inputfilelines: 
        functions[line[0]](line)
        
        
batch_UI()
