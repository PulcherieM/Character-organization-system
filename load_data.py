
#==========================================#
# Place your character_occupation_list function after this line
def character_occupation_list (file_name: str, occupation: str) -> list[dict]:
    """
    Return the name of characters and its corresponding occupation in a list  
    with dictionary values.
    Precondition: The file must exist and the occupation must exist. File must
    include ["Strength", "Agility", "Stamina", "Personality", " Intelligence", 
    "Luck", "Armor", "Weapon"]
    
    >>> character_occupation_list ("characters-mat.csv", "EB")
    [{"Strength": 14, "Agility" : 5, "Stamina": 8, "Personality": 11, 
    " Intelligence": 5,"Luck": 0.67, "Armor": 9, "Weapon":Dart}, 
    {Another Element},
    ...
    ]
    
    >>> character_occupation_list ("characters-mat.csv", "H")
    [{"Strength": 12, "Agility" : 9, "Stamina": 4, "Personality": 6, 
    " Intelligence": 12,"Luck": 0.61, "Armor": 10, "Weapon":Club},
    {Another Element},
    ...
    ]
    
    >>> character_occupation_list ("characters-mat.csv", "HG")
    [{"Strength": 16, "Agility" : 4, "Stamina": 7, "Personality": 12, 
    " Intelligence": 9,"Luck": 0.61, "Armor": 9, "Weapon":Handaxe}],
    {Another Element},
    ...
    ]
    """
    
    character_list = [] #creates an empty list
    in_file = open (file_name, "r") #opens the file
    first_line = True # assignning a value to first_line
    for line in in_file: #itterates over each line in the file
        line = line.strip().split(",") #removes any spaces and punctuations
        if first_line:
            first_line = False # make it not true so that the header doesnt get read again
            header = line
        character_dict = {}
        if occupation == line [0]:
            character_dict[header[1]] = int(line [1])
            character_dict[header[2]] = int(line[2])
            character_dict[header[3]] = int(line[3])
            character_dict[header[4]] = int(line[4])
            character_dict[header[5]] = int(line[5])
            character_dict[header[6]] = float(line[6])
            character_dict[header[7]] = int(line[7])
            character_dict[header[8]] = str(line[8])
            character_list.append(character_dict)
   
    in_file.close()
    return character_list


#==========================================#
# Place your character_strength_list function after this line
def character_strength_list(file_name: str, strength_range: tuple) -> list:
    """Returns the wizards that fall within the given strength range and removes the strength value from the output
    
    Preconditions: file_name is not empty
                   file_name must be valid
                   strength_range must be a valid range of integers
                   file_name has the following columns: occupation, strength agility, stamina, personality, intelligence, luck, armor, weapon
    
    
    character_strength_list('characters-mat.csv', (20,21)
    >>>{'occupation': 'at', 'agility': 7, 'stamina': 2, 'personality': 11, 'intelligence': 8, 'luck': 0.67, 'armor': 10, 'weapon': 'staff'}
       {Another element}
       ...
    
     character_strength_list('characters-mat.csv', (0,0)
    >>> []
    
     character_strength_list('characters-mat.csv', (4,7)
    >>> {'occupation': 'at', 'agility': 5, 'stamina': 9, 'personality': 12, 'intelligence': 14, 'luck': 0.78, 'armor': 9, 'weapon': 'dagger'}
        {Another element}
        ...
    """
    
    in_file = open(file_name, 'r')

    strength_min, strength_max = strength_range

    wizards_n = []

    wizard_list = []

    first_line = True

    for line in in_file:

        line = line.strip()
        line = line.split(',')

        if first_line:

            first_line = False

            table_header = line

        else:

            wizards = {}
            wizards[table_header[0]] = line[0]
            wizards[table_header[2]] = int(line[2])
            wizards[table_header[3]] = int(line[3])
            wizards[table_header[4]] = int(line[4])
            wizards[table_header[5]] = int(line[5])
            wizards[table_header[6]] = float(line[6])
            wizards[table_header[7]] = int(line[7])
            wizards[table_header[8]] = line[8]

            wizard_list += [wizards]   


            if strength_min <= int(line[1]) <= strength_max:

                wizards_n.append(wizards)

        
    in_file.close() 

    return wizards_n

#==========================================#
# Place your character_luck_list function after this line
def character_luck_list (char_list:str, luck: float) -> list[dict]:
    """
    Retrun a list of character stats that has a luck value less than the imput without retruning the luck value in the code.
    
    Precondition: Must call a vaild file name, and value for luck must be a float or int
    
    >>> character_luck_list('characters-mat-test.csv', 0.3)
    []
    >>> character_luck_list('characters-mat-test.csv', 0.74)
    [{'Occupation': 'AT', 'Strength': 13, 'Agility' : 2, 'Stamina': 6, 'Personality' : 7, 'Intelligence' : 7, 'Armor : '8' , 'Weapon' : Staff'}, 
    {'Occupation': 'AT', 'Strength': 12, 'Agility' : 3, 'Stamina': 7, 'Personality' : 13, 'Intelligence' : 11, 'Armor : '8' , 'Weapon' : Staff'}]
    
    """
    file = open(char_list, 'r')
    count = 0
    luck_list = []
    
    for stats in file:
        if count == 0:
            header = stats
            header = header.strip('\n')
            header = header.split(',')
            count += 1
            
        else:
            stats = stats.strip()
            stats = stats.split(',')
            build ={}
            build[header[0]] = stats[0]
            build[header[1]] = int(stats[1])
            build[header[2]] = int(stats[2])
            build[header[3]] = int(stats[3])
            build[header[4]] = int(stats[4])
            build[header[5]] = int(stats[5])
            build[header[6]] = float(stats[6])
            build[header[7]] = int(stats[7])
            build[header[8]] = stats[8]
            
            
            if build['Luck'] < luck:
                del build['Luck']
                
                luck_list.append(build)
            
            
    file.close()
    return luck_list

#==========================================#
# Place your character_weapon_list function after this line
def character_weapon_list(file_name: str, weapon: str) -> dict: 
    """ Return a list of dictionaries of with the attributes associated with the desired weapon.
    Preconditions: must file must exist, weapon parameter must exist, file must include headers.
    >>> character_weapon_list ('characters-mat.csv', 'Staff')
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
    {another element},
    …
    ]
    >>> character_weapon_list ('characters-mat.csv', 'aaa')
    []
    
    """ 
    in_file = open(file_name, 'r')
    game_character_list = [] 
    first_line = True
    count = 0
    for line in in_file:
        count += 1
    
        line = line.strip().split(',')
            
        if first_line:
            first_line = False
            header = line
        elif line[8] == weapon:
            characters = {}    
            characters[header[0]] = line[0]
            characters[header[1]] = int(line[1])
            characters[header[2]] = int(line[2])
            characters[header[3]] = int(line[3])
            characters[header[4]] = int(line[4])
            characters[header[5]] = int(line[5])
            characters[header[6]] = float(line[6])
            characters[header[7]] = int(line[7])

        
            
            game_character_list.append(characters) 
  
    in_file.close()
    return game_character_list


#==========================================#
# Place your load_data function after this line
def load_data(char_list: str, char: tuple) -> dict:
    """Return 
  load_data('characters-mat.csv', ('Weapon', 'Staff'))
  >>>[{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
   'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
  {another element}
  
  load_data('characters-mat.csv',  ('All', -1))
  >>>[{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8,
 'Weapon': 'Staff'},
{another element},

  load_data('characters-mat.csv',  ('Agility', 2))
  >>>Invalid Value //Message displayed on the terminal
  [] //Return value
  >>> load_data('characters-mat.csv', ('Stamina', -1))
  Invalid Value //Message displayed on the terminal
  [] //Return value 
  """
    

    if char[0] == 'All':
            file = open(char_list, 'r')
            count = 0
            empty = []
            
            for stats in file:
                if count == 0:
                    header = stats
                    header = header.strip('\n')
                    header = header.split(',')
                    count += 1
        
                    
                else:
                    stats = stats.strip()
                    stats = stats.split(',')
                    build ={}
                    build[header[0]] = stats[0]
                    build[header[1]] = int(stats[1])
                    build[header[2]] = int(stats[2])
                    build[header[3]] = int(stats[3])
                    build[header[4]] = int(stats[4])
                    build[header[5]] = int(stats[5])
                    build[header[6]] = float(stats[6])
                    build[header[7]] = int(stats[7])
                    build[header[8]] = stats[8]
                    empty.append(build)
                    
            return empty
        
    elif char[0] == 'Strength':
        return character_strength_list(char_list, char[1])
        
    elif char[0] == 'Luck':
        return character_luck_list(char_list, char[1])
        
    elif char[0] == 'Weapon':
        return character_weapon_list(char_list, char[1]) 
        
    elif char[0] == 'Occupation':
        return character_occupation_list(char_list, char[1])   
        
    else:
        print ("Invalid Value")
        return []
                        
    
    file.close()

#==========================================#
# Place your calculate_health function after this line
def calculate_health(characters : list[dict]) -> list[dict]:
    """Returns the calculated health of the character.
  Preconditions: Characters must be a list of dictionaries.
  
>>> calculate_health([{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
 'Armor': 8, 'Weapon': 'Staff'},
 {another element},
 …
 ])
[{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff',
 'Health': 80.8},
{another element},
…
]
  """ 


    for i in range(0, len(characters)):

        health = (characters[i]['Strength'] + characters[i]['Agility'] + characters[i]['Stamina'] + characters[i]['Personality'] + characters[i]['Intelligence']) + (characters[i]['Armor'] ** 2 * characters[i]['Luck'])

        characters[i].update({'Health': health})

    return characters


# Do NOT include a main script in your submission
