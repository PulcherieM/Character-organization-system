
#==========================================#
# Place your script for your text_UI after this line
import load_data, sort, curve_fit, histogram  



        
def load():
        attribute_value = 0
        file = input("Please enter the name of the file: ")
        attribute = input("Please enter the attribute to use as a filter: ")
        if attribute == 'Strength' or attribute == 'Luck' or attribute == 'Weapon' or attribute == 'Occupation' or attribute == 'All':
                if attribute != 'All':
                        attribute_value = (input("Please enter the value of the attribute: ")) #float
                        att_tup = (attribute, (attribute_value))
                        print (load_data.load_data(file, att_tup))                        
                elif attribute == 'All':
                        att_tup = (attribute, attribute_value)
                        print (load_data.load_data(file, att_tup)) 
                
        elif attribute != 'Strength' or attribute != 'Luck' or attribute != 'Weapon' or attribute != 'Occupation' or attribute != 'All':
                att_check = False
                while att_check == False:
                        print ('Invalid input')
                        attribute = (input("Please enter the attribute to use as a filter: "))
                        if  attribute == 'Strength' or attribute == 'Luck' or attribute == 'Weapon' or attribute == 'Occupation' or attribute == 'All':
                                att_check =True
                
               
                attribute_value = (input("Please enter the value of the attribute: ")) #float
                att_tup = (attribute, attribute_value)                        
                print (load_data.load_data(file, att_tup)) 
        
        file = load_data.calculate_health(load_data.load_data(file, ('All', 0)))
        return file


def text_sort():
        if data == True:
                sort_att = input("Please enter the attribute you want to use for sorting: 'Agility', 'Armor', 'Intelligence' , 'Health' : ")
                if sort_att == 'Agility' or sort_att == 'Armor' or sort_att == 'Intelligence' or sort_att == 'Health':
                
                        order = input("Ascending (A) or Descending (D) order")
                        display = input("Data Sorted. Do you want to display the data?: ")
        
                        if display.upper() == 'Y':
                                print ('Data Loaded')
                                print (sort.sort(data_load, order,sort_att))
                        elif display.upper() == 'N':
                                print("Data will not be displayed")  
                
                elif sort_att != 'Agility' or sort_att != 'Armor' or sort_att != 'Intelligence' or sort_att != 'Health':
                        
                        sort_check = False
                        while sort_check == False:
                                        print ("Inavalid Input")
                                        sort_att = (input("Please enter the attribute to use as a filter: "))
                                        if  sort_att == 'Agility' or sort_att == 'Health' or sort_att == 'Armor' or sort_att == 'Intelligence' :
                                                sort_check = True     
                        order = input("Ascending (A) or Descending (D) order")
                        display = input("Data Sorted. Do you want to display the data?: ")
                                
                        if display.upper() == 'Y':
                                print ('Data Loaded')
                                print (sort.sort(data_load, sort_att, order))
                        elif display.upper() == 'N':
                                print("Data will not be displayed")  
        
                                
        elif data == False:
                print ("File not loaded. PLease, load a file first")



def curve ():
        if data == True:
                cur_att = input("Please enter the attribute you want to use to find the best fit for Health: ")
                if cur_att == 'Strength' or cur_att == 'Agility' or cur_att == 'Stamina' or cur_att == 'Stamina' or cur_att == 'Personality' or cur_att == 'Intelligence'or cur_att == 'Luck' or cur_att == 'Armor':
                        poly_order = int(input ("Please eter the order of the polynomial to be fitted: "))
                        
                        print (curve_fit.curve_fit(data_load, cur_att, poly_order)) 
                        
                else:
                        print("Invalid command")
        
        elif data == False:
                print ("File not loaded. PLease, load a file first")
                
def hist():
        if data == True:
                hist_plot = input("Please enter the attribute you want to use for plotting: ")
                if hist_plot == 'Strength' or hist_plot == 'Agility' or hist_plot == 'Stamina' or hist_plot == 'Stamina' or hist_plot == 'Personality' or hist_plot == 'Intelligence'or hist_plot == 'Luck' or hist_plot == 'Armor' or hist_plot == 'Occupation' or hist_plot == 'Weapon':
                        print(histogram.histogram(data_load, hist_plot))
                
                else:
                        print("Invalid command")
               
#################################################################################################################
data_load = []                       
loop = True
data = False
while loop: 
        print("The available commands are: \n   L)oad Data \n   S)ort Data \n   C)urve Fit \n   H)istogram \n   E)xit")        
        user = input("Please type your command:")


        if user.upper() == 'L':
                data_load = load()
                data = True
                print (data_load)
                
                
                

        if user.upper() == 'S':
                text_sort()
         
        elif user.upper() == 'C':
                curve()
        
        elif user.upper() == 'H':
                hist()
        
        elif user.upper() == 'E':
                loop = False

        
        
