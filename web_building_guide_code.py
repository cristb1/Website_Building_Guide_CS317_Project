# Project Name: Web Building Guide
# Author: Bethany Crist
# Libraries Used: MariaDB, tabulate

import mariadb as sql
from tabulate import tabulate

db = sql.connect(
    host='localhost',
    user='root',
    password='root',
    database='web_building_guide'
)

cursor = db.cursor()

print('Web Building Guide')

def main_menu():

    # Display options
    print('What would you like to look up?')
    print('1. Print all web hosting services and their information in database\n2. Print all programming languages and their information in database\n3. Search for web hosting services\n4. Print tiers of a web hosting service\n5. Add a Web Hosting Service to the Database')
    
    # Get user's choice
    user_input = input()
    if user_input == '1':
        option_1() # Printing services with their info
    if user_input == '2':
        option_2() # Printing programming languages with their info
    if user_input == '3':
        option_3() # Searching for services based on one of the options
    if user_input == '4':
        option_4() # Picking a service to see the tiers of
    if user_input == '5':
        option_5()
    else:
        print("Please input a number that corresponds to one of the options")
        main_menu()    


# Option 1 - Finished
def option_1():
    print('All Web Hosting Services and Their Info\n')

    # Get web hosting service information
    query = 'SELECT * FROM WebHostingService'
    cursor.execute(query)
    result = cursor.fetchall()

    # Display information
    table = []
    for t in result:
        t_list = list(t)
        # Change 1s and 0s to TRUEs and FALSEs
        for z in range(1,4):
            if t[z] == 0:
                t_list[z] = 'FALSE'
            elif t[z] == 1:
                t_list[z] = 'TRUE'
        t = tuple(t_list)
        table.append(t)
        
    print_table = tabulate(table, headers=["Service","Is Codable","Has Pre-Built Tools", "Has Free Tier", "Description"])
    print(print_table)

    go_back()


# Option 2 - Finished
def option_2():
    print('All Programming Languages and Their Info\n')

    # Get programming language information
    query = 'SELECT * FROM ProgrammingLanguage'
    cursor.execute(query)
    result = cursor.fetchall()

    # Display information
    table = []
    for t in result:
        t_list = list(t)
        # Change 1s and 0s to TRUEs and FALSEs
        if t[2] == 0:
            t_list[2] = 'FALSE'
        elif t[2] == 1:
            t_list[2] = 'TRUE'
        t = tuple(t_list)
        table.append(t)

    print_table = tabulate(table, headers=["Name", "Type of Language", "Requires Server Side Communication"])
    print(print_table)

    go_back()

# Option 3 - Finished
def option_3(): 
    # Display options
    print('Search for Web Hosting Services')
    print('What would you like to search by')
    print('1. Codable Web Hosting Services\n2. Supported Programming Languages\n3. Web Hosting Services with a Free Tier\n4. Web Hosting Services with Prebuilt Design Tools\n5. Search based on name')
    
    # Get user's choice
    user_input = input()
    if user_input == '1':
        option_3_1() # Codable Web Hosting Services
    if user_input == '2':
        option_3_2() # Supported Programming Languages
    if user_input == '3':
        option_3_3() # Web Hosting Services with a Free Tier
    if user_input == '4':
        option_3_4() # Web Hosting Services with Prebuilt Design Tools     
    if user_input == '5': # Search by Matching Pattern in Service Name
        option_3_5()
    else:
        print("Please input a number that corresponds to one of the options")
        option_3() 


def option_3_1():
    print('Codable Web Hosting Services')
    query = 'SELECT serviceName FROM WebHostingService WHERE isCodable=TRUE'
    cursor.execute(query)
    result = cursor.fetchall()
    table = []
    for t in result:
        table.append(t)

    print_table = tabulate(table)
    print(print_table)

    go_back()

def option_3_2():
    print('Supported Programming Languages')

    # List of services with their supported programming languages
    query = "SELECT serviceName, GROUP_CONCAT(languageName SEPARATOR ', ') AS languageList FROM ServiceSupports GROUP BY serviceName"
    cursor.execute(query)
    result = cursor.fetchall()
    table = []
    for t in result:
        table.append(t)

    print_table = tabulate(table)
    print(print_table)    
    
    
    go_back()

def option_3_3():
    print('Web Hosting Services with a Free Tier')

    query = 'SELECT serviceName FROM WebHostingService WHERE hasFreeTier=TRUE'
    cursor.execute(query)
    result = cursor.fetchall()
    table = []
    for t in result:
        table.append(t)

    print_table = tabulate(table)
    print(print_table)

    go_back()

def option_3_4():
    print('Web Hosting Services with Prebuilt Design Tools') 

    query = 'SELECT serviceName FROM WebHostingService WHERE hasPreBuilt=TRUE'
    cursor.execute(query)
    result = cursor.fetchall()
    table = []
    for t in result:
        table.append(t)

    print_table = tabulate(table)
    print(print_table)    

    go_back()

def option_3_5():
    print("Search for a Name")

    print("Please input either the whole or partial name of a web service:")
    user_search = input()
    search = '%'+user_search+'%'
    query = "SELECT * FROM WebHostingService WHERE serviceName LIKE %s"
    cursor.execute(query, (search,))
    result = cursor.fetchall()
    if len(result) == 0:
        print("No web hosting services with this name in the database")
    else:
        table = []
        for t in result:
            table.append(t)
            
        print_table = tabulate(table,  headers=["Service","Is Codable","Has Pre-Built Tools", "Has Free Tier", "Description"])
        print(print_table)

    go_back()
    
# Option 4 - Finished
def option_4():
    print('Print Tiers of a Web hosting Service')

    # Get web hosting services
    query = 'SELECT serviceName FROM WebHostingService'
    cursor.execute(query)
    result = list(cursor.fetchall())

    # Get number of web hosting services in database
    count_query = 'SELECT COUNT(serviceName) FROM WebHostingService'
    cursor.execute(count_query)
    count_result = cursor.fetchall()[0][0]

    # Display list of web hosting services
    list_names = []
    list_web_services = []
    for t in range(1, count_result+1):
        list_names.append(result[t-1][0])
        list_web_services.append((t,result[t-1][0]))

        print(list_web_services[t-1][0], ". ", list_web_services[t-1][1], sep='')

    # Get user's choice    
    user_input = int(input())
    choice = list_names[user_input-1]

    option_4_tiers(choice) # Function for displaying tier information          
 
def option_4_tiers(service_name):
    print('Print Tiers of', service_name)

    # Get tier information of chosen web hosting service
    query = "SELECT tierName, CONCAT('$', cost,' ',costUnit) AS cost, features FROM Tier WHERE serviceName = '" + service_name + "'"
    cursor.execute(query)
    result = cursor.fetchall()

    # Display tiers
    # If no tiers in database, display that there are none
    # If tiers exist, display them
    if len(result) == 0:
        print('No Tiers for this Service')
    else:
        table = []
        for t in result:
            table.append(t)

        print_table = tabulate(table, headers=["Tier:", "Cost:", "Info:"], tablefmt="plain", maxcolwidths=[20,30])
        print(print_table)

    go_back()    

# Option 5 - Finished
def option_5():
    print("Add Web Hosting Service to Database")
    # Entering Data
    print("Enter Name of Service:")
    service_name = input()

    print("Is it codable?")
    print("1. Yes\n2. No\n3. Don't Know")
    is_codable_user_input = input()
    is_codable = False # default
    if is_codable_user_input == '1':
        is_codable = True
    elif is_codable_user_input == '2':
        is_codable = False
    elif is_codable_user_input == '3':
        is_codable = None  

    print("Does it have prebuilt design tools?")     
    print("1. Yes\n2. No\n3. Don't Know")
    has_prebuilt_user_input = input()
    has_prebuilt = False # default
    if has_prebuilt_user_input == '1':
        has_prebuilt = True
    elif has_prebuilt_user_input == '2':
        has_prebuilt = False
    elif has_prebuilt_user_input == '3':
        has_prebuilt = None   

    print("Does it have a free tier?")  
    print("1. Yes\n2. No\n3. Don't Know")
    has_freetier_user_input = input()
    has_freetier = False # default
    if has_freetier_user_input == '1':
        has_freetier = True
    elif has_freetier_user_input == '2':
        has_freetier = False
    elif has_freetier_user_input == '3':
        has_freetier = None     

    print("Please write a description of the service (max 500 characters)")
    description = input()


    # Putting Given Data in Tuple
    service_data = (service_name, is_codable, has_prebuilt, has_freetier, description)

    # Insert into Database
    add_service(service_data)          
   
def add_service(service_data):
    query = "INSERT INTO WebHostingService(serviceName, isCodable, hasPreBuilt, hasFreeTier, description) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query,service_data)
    query_2 = "SELECT * FROM WebHostingService WHERE serviceName = %s"
    cursor.execute(query_2,(service_data[0],))
    db.commit()
    result = cursor.fetchall()
    table = []
    for t in result:
        t_list = list(t)
        # Change 1s and 0s to TRUEs and FALSEs
        for z in range(1,4):
            if t[z] == 0:
                t_list[z] = 'FALSE'
            elif t[z] == 1:
                t_list[z] = 'TRUE'
            else:
                t_list[z] = ' ' 
        t = tuple(t_list)
        table.append(t)
             
    print_table = tabulate(table, headers=["Service","Is Codable","Has Pre-Built Tools", "Has Free Tier", "Description"])
    print(print_table)

    print("Would you like to add another service to the database?")
    print("1. Yes\n2. No")
    user_choice = input()
    if user_choice == '1':
        option_5()
    elif user_choice == '2':
        go_back()    

    

# Going Back to Main Menu
def go_back():
    print('\nPress B to Go Back to Main Menu, Press Any Other Button to Exit')
    user_input = input()
    if user_input == 'B' or user_input == 'b':
        main_menu()
    else:
        exit()    

main_menu()    



      
    