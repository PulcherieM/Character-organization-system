
#==========================================#

# Place test_return_list function here 
file_name = "characters-test.csv"

def test_return_list():
    #Complete the function with your test cases
    
    #test that character_occupation_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.character_occupation_list(file_name,"AT"), list), True)
    check.equal(isinstance(load_data.character_occupation_list(file_name,"DB"), list), True)
    check.equal(isinstance(load_data.character_occupation_list(file_name,"EB"), list), True)
    
    #test that character_strength_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.character_strength_list(file_name,(8,11)), list), True)
    check.equal(isinstance(load_data.character_strength_list(file_name,(3,4)), list), True)
    check.equal(isinstance(load_data.character_strength_list(file_name,(2,7)), list), True)    

    #test that character_luck_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.character_luck_list(file_name, 0.5), list), True)
    check.equal(isinstance(load_data.character_luck_list(file_name, 0.67), list), True)
    check.equal(isinstance(load_data.character_luck_list(file_name, 0.33), list), True)
    
    #test that character_weapon_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.character_weapon_list(file_name,"Staff"), list), True)
    check.equal(isinstance(load_data.character_weapon_list(file_name,"Dart"), list), True)
    check.equal(isinstance(load_data.character_weapon_list(file_name,"Dagger"), list), True)
    
    #test that load_data returns a list (6 different test cases required)
    check.equal(isinstance(load_data.load_data(file_name, ("Strength", (3,7))), list), True)
    check.equal(isinstance(load_data.load_data(file_name, ("Occupation", "EB")), list), True)
    check.equal(isinstance(load_data.load_data(file_name, ("Weapon", "Club")), list), True)
    check.equal(isinstance(load_data.load_data(file_name, ("Strength", (13,15))), list), True)
    check.equal(isinstance(load_data.load_data(file_name, ("Luck", 0.5)), list), True)
    check.equal(isinstance(load_data.load_data(file_name, ("Occupation", "AT")), list), True)
    
    #test that calculate_health returns a list (3 different test cases required)
    check.equal(isinstance(load_data.calculate_health([{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,'Armor': 8, 'Weapon': 'Staff'}]), list), True)
    
    check.equal(isinstance(load_data.calculate_health([{'Occupation': 'DB', 'Strength': 17, 'Agility': 5, 'Stamina': 10, 'Personality': 11, 'Intelligence': 11, 'Luck': 0.67,'Armor': 9, 'Weapon': 'Staff'}]), list), True)
    
    check.equal(isinstance(load_data.calculate_health([{'Occupation': 'EB', 'Strength': 9, 'Agility': 8, 'Stamina': 9, 'Personality': 4, 'Intelligence': 2, 'Luck': 0.56, 'Armor': 10, 'Weapon': 'Dart'}]), list), True)
    
    check.summary()


# Do NOT include a main script in your submission
test_return_list()



# Place test_return_list_correct_length function here

def test_return_list_correct_length():
    #Complete the function with your test cases
    
    #test that character_occupation_list returns a list with the correct length (3 different test cases required)

    
    check.equal(len(load_data.character_occupation_list('characters-test.csv','AT')), 3)
    check.equal(len(load_data.character_occupation_list('characters-test.csv','WA')), 5)
    check.equal(len(load_data.character_occupation_list('characters-test.csv','VF')), 3)
    
    #test that character_strength_list returns a list with the correct length (3 different test cases required)
    check.equal(len(load_data.character_strength_list('characters-test.csv',(3,10))), 4)
    check.equal(len(load_data.character_strength_list('characters-test.csv',(4,10))), 4)
    check.equal(len(load_data.character_strength_list('characters-test.csv',(20,21))), 1)
    
    #test that character_luck_list returns a list with the correct length (3 different test cases required)
    check.equal(len(load_data.character_luck_list('characters-test.csv',0.3)), 0)
    check.equal(len(load_data.character_luck_list('characters-test.csv',0.67)), 13)
    check.equal(len(load_data.character_luck_list('characters-test.csv',0.5)), 5)
    
    #test that character_weapon_list returns a list with the correct length(3 different test cases required)
    check.equal(len(load_data.character_weapon_list('characters-test.csv','Staff')), 4)
    check.equal(len(load_data.character_weapon_list('characters-test.csv','Club')), 5)
    check.equal(len(load_data.character_weapon_list('characters-test.csv','Spear')), 2)
    
    
    #test that load_data returns a list with the correct length (6 different test cases required)
    check.equal(len(load_data.load_data('characters-test.csv',('Weapon', 'Staff'))), 4)
    check.equal(len(load_data.load_data('characters-test.csv',('Occupation', 'AT'))), 3)
    check.equal(len(load_data.load_data('characters-test.csv',('Luck', 0.3))), 0)
    check.equal(len(load_data.load_data('characters-test.csv',('All', 'Staff'))), 26)
    check.equal(len(load_data.load_data('characters-test.csv',('Strength', (20,21)))), 1)
    check.equal(len(load_data.load_data('characters-test.csv',('Weapon', 'Spear'))), 2)
    
    #test that calculate_health returns a list with the correct length (3 different test cases required)
    check.equal(len(load_data.calculate_health([])), 0)
    check.equal(len(load_data.calculate_health([{'Occupation':'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2,
 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff' }])),1 )
    check.equal(len(load_data.calculate_health([{'Occupation':'AT', 'Strength': 9, 'Agility': 7, 'Stamina': 2,
 'Personality': 12, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff' }])),1 )    

    
    check.summary()

test_return_list_correct_length()


#Place test_return_correct_dict_inside_list function here

test_file = 'characters-test.csv'
def test_return_correct_dict_inside_list():
    #Complete the function with your test cases
    
    #test that character_occupation_list returns a correct dictionary inside the list (3 different test cases required)
    occ_test = load_data.character_occupation_list(test_file, 'AT') 
    occ_test2 = load_data.character_occupation_list(test_file, 'WA')
    occ_test3 = load_data.character_occupation_list(test_file, 'HG')
    check.equal(occ_test[0], {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'})
    check.equal(occ_test2[2], {'Strength': 15, 'Agility': 12, 'Stamina': 7, 'Personality': 13, 'Intelligence': 7, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dagger'})
    check.equal(occ_test3[1], {'Strength': 12, 'Agility': 7, 'Stamina': 12, 'Personality': 10, 'Intelligence': 7, 'Luck': 0.83, 'Armor': 10, 'Weapon': 'Sling'})
    
    
    #test that character_strength_list returns a correct dictionary inside the list  (3 different test cases required)
    str_test = load_data.character_strength_list(test_file, (8, 9)) 
    str_test2 = load_data.character_strength_list(test_file, (17, 19))
    check.equal(str_test[0], {'Occupation': 'EB', 'Agility': 3, 'Stamina': 10, 'Personality': 8, 'Intelligence': 6, 'Luck': 0.5, 'Armor': 8, 'Weapon': 'Staff'})
    check.equal(str_test[1], {'Occupation': 'WA', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'})
    check.equal(str_test2[0], {'Occupation': 'AT', 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger'})
    
    
    #test that character_luck_list returns a correct dictionary inside the list  (3 different test cases required)
    luck_test = load_data.character_luck_list(test_file, 0.78)
    luck_test2 = load_data.character_luck_list(test_file, 0.8)
    
    check.equal(luck_test[0], {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'})
    check.equal(luck_test[-1], {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Armor': 11, 'Weapon': 'Spear'})
    check.equal(luck_test2[0], {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'})

    
    #test that character_weapon_list returns a correct dictionary inside the list (3 different test cases required)
    wep_list = load_data.character_weapon_list(test_file, 'Staff')
    wep_list2 = load_data.character_weapon_list(test_file, 'Sling')
    
    check.equal(wep_list[0], {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10})
    check.equal(wep_list[-1], {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10})
    check.equal(wep_list2[0], {'Occupation': 'EB', 'Strength': 13, 'Agility': 8, 'Stamina': 8, 'Personality': 14, 'Intelligence': 15, 'Luck': 0.83, 'Armor': 10})
    

    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    load_test = load_data.load_data(test_file,('All', 324))
    load_test2 = load_data.load_data(test_file,('Occupation', 'AT'))
    load_test3 = load_data.load_data(test_file,('Strength', (7, 11)))
    load_test4 = load_data.load_data(test_file,('Luck', 0.43))
    load_test5 = load_data.load_data(test_file,('Weapon', 'Spear'))
    load_test6 =  load_data.load_data(test_file,('Wadkjadjkdak', 'dhjdsfjkdsfjk'))
    
    
    check.equal(load_test[0], {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'})
    check.equal(load_test2[0], {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'})
    check.equal(load_test3[0], {'Occupation': 'DB', 'Agility': 10, 'Stamina': 11, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'})
    check.equal(load_test4[-1], {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Armor': 10, 'Weapon': 'Staff'})
    check.equal(load_test5[-1], {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11})
    check.equal (load_test6, [] )
    #test that calculate_health returns a correct dictionary inside the list  (3 different test cases required)
    health_func = load_data.load_data(test_file, ('All', ""))
    health_test = load_data.calculate_health(health_func)
    
    check.equal(health_test[0],{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff', 'Health': 115.0})
    check.equal(health_test[1],{'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club', 'Health': 90.0})
    check.equal(health_test[2],{'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger', 'Health': 98.0})
    
    
    check.summary()

#Place test_calculate_health function here
def test_calculate_health() -> None:
    #Complete the function with your test cases
  
    
    #test that the function does not change the lenght of the list provided as input parameter (5 different test cases required)
    a_list = load_data.character_occupation_list('characters-test.csv', "AT")
    first_list = load_data.calculate_health(a_list)
    
    check.equal(len(a_list), len(first_list))
    check.summary()

    b_list = load_data.character_luck_list('characters-test.csv', 0.74)
    v_list = load_data.character_luck_list('characters-test.csv', 0.3)
    second_list = load_data.calculate_health(v_list)
    
    try:
        load_data.calculate_health(b_list)
    except: 
        check.equal(False,False)
        check.summary()
    
    
    d_list = load_data.character_weapon_list('characters-test.csv', 'Staff')
    fourth_list = load_data.calculate_health(d_list)

    check.equal(len(d_list), len(fourth_list))
    check.summary()
    
    e_list = load_data.load_data('characters-test.csv',  ('All', -1))
    fifth_list = load_data.calculate_health(e_list)
    
    check.equal(len(e_list), len(fifth_list))
    check.summary()       
    
    
    c_list = load_data.character_strength_list('characters-test.csv', (20,21))
    z_list = load_data.character_strength_list('characters-test.csv', (0,0))
    third_list = load_data.calculate_health(z_list)
    
    try:
        load_data.calculate_health(c_list)
    except: 
        check.equal(False,False)
        check.summary()    
    
    
    #test that the function returns an empty list when it is called whith an empty list
    check.equal(load_data.calculate_health([]), [])
    check.summary()
    
    
    #test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    
    for dictonary in first_list:
        check.equal(len(dictonary), 9)
        check.summary() 
        
    for meow in second_list:
        check.equal(len(meow), 9)
        check.summary()
        
    for woof in third_list:
        check.equal(len(woof), 9)
        check.summary() 
        
    for me in fourth_list: 
        check.equal(len(me), 9)
        check.summary() 
        
        
    for be in fifth_list:
        check.equal(len(be), 10)
        check.summary
    
    
    #test that the Health value is properly calculated  (5 different test cases required)
    
    check.equal(first_list[0]["Health"], 115.0)
    check.summary()
    
    check.equal(fourth_list[0]["Health"], 115.0)
    check.summary()
    
    check.equal(fifth_list[0]["Health"], 115.0)
    check.summary()    
    
    try:
        (b_list[0]["Health"], 115.0)
    except KeyError:
        check.equal(False,False)
    
    try: 
        (c_list[0]["Health"], 115.0)
    except KeyError:
        check.equal(False,False)

# Do NOT include a main script in your submission

test_calculate_health()


# Do NOT include a main script in your submission
