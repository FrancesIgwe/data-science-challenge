#--------------------------------------------------------------------------------
#SHOPIFY DATA SCIENCE INTERN  CHALLENGE 2022
#
#Exercise number: 1
#
# Purpose of code:  To compute a better way to find average order of value of sales
#                   from a spreadsheet table
#
# Author: Frances Igwe
#-------------------------------------------------------------------------------
import csv

#introductory comment
print('Choose from the following options a, b or c to get the  answers to their respective questions below.',
      '\nTo Terminate the program, press the enter key at the prompt\n')

# exercise question
print("""question a: Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.
question b: What metric would you report for this dataset?
question c: What is its value?""")


#user is required to enter an option a, b or c
option = input("\n What question would you like an answer to? a, b or c. Press enter to exit: ")


#loop to keep the program asking questions unless the user exits
while option != '':
    
    #answer to question a
    if option == 'a':
        print('\n The result $3145.13 was calculated with the total order amount divided by the number of orders in the last 30 days.\n',
        'The problem with this formula applied here, is that there are 100 different stores each selling their sneakers at different prices.\n',
        'The number of different customers that buy sneakers, and the sneaker prices for each store are two possible factors to be considered\n',
        'for the low average order value. A better idea would be to calculate the average order value for each store individually rather\n', 
        'than all 100 stores at once.') 
                
                
    #answer to question b
    elif option =='b':
        print('\n I propose the option of finding the average order in a month.\n', 
              'This is done by calculating the sum total of order_amount divided by 30 days.\n',
              'By obtaining the average order, we get to see how much all 100 stores perform in a month.')
    
    #answer to question c
    elif option == 'c':
        
        #opens and reads data from provided shopify spreadsheet 
        with open('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv', newline='') as csvfile:
            data_rows = csv.reader(csvfile, delimiter=' ', quotechar='|')
            
            order_list =[]
            #collects order_amount values from provided data and stores them in a new order list
            for row in data_rows:
                items = row[0].split(",")
                order_list.append(items[3])
                
            #removes the heading - 'order-amount'  from the order_list
            order_list.pop(0)
            
            #calculates the sum of orders
            total_orders = sum(map(int, order_list))
        
            #finds and prints the average of total orders in last 30 days.
            num_days = 30
            print(' \n The average order for all 100 stores in 30 days = $',total_orders /num_days)
          
    
    #handles incorrect user inputs
    else:
        print(" Invalid input. Try again with options a, b or c")
        
    option = input("\nWhat question would you like an answer to? a, b or c. Press enter to exit: " ) 

#statement after program termination
print('...program terminated, Thank you for viewing.')