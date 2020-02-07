#Import Needed Modules
#Code from Various Class Activities
#Gives Access to Miscellaneous OS Actions
import os
#Allows Python to Read & Write CSV Files
import csv

#Give Python Access to the Budget_Data CSV File
#Code from Various Class Activities
csv_path = os.path.join("budget_data.csv")

print("Financial Analysis")
print("-------------------------")
##########Calculate the Total Number of Months Included in the Dataset############
#Read from the Budget_Data CSV File
#Code from Various Class Activities
with open(csv_path,"r") as csv_file:
    #Split the Data by Commas
    csv_reader = csv.reader(csv_file,delimiter=",")
    #Read the header without Printing
    #Code from Section 3.3 Activity 1
    csv_header=next(csv_file)

    #Start with Empty List
    row_compile = []
    #Iterate Through All of the Rows
    for row in csv_reader:
        #Append Month Stamps Onto List
        row_compile.append(row[0])
    #Count the Total Amount of Arguments in the row_compile List
    row_count = len(row_compile)
    #Print the Row Count
    print(f"The total amount of months is: {row_count}.")


##########Calculate the Total Amount of "Profits/Losses" in the Data############
#Read from the Budget_Data CSV File
#Code from Various Class Activities
with open(csv_path,"r") as csv_file:
    #Split the Data by Commas
    csv_reader = csv.reader(csv_file,delimiter=",")
    #Read the header without Printing
    #Code from Section 3.3 Activity 1
    csv_header=next(csv_file)

    #Initialize the Total Amount of "Profits/Losses"
    total_change = 0
    #Iterate Through All of the Rows
    for row in csv_reader:
        #Set the Monthly Profit or Loss to the Running Total
        monthly_profit = int(row[1])
        #Append Monthly Profit or Loss to the Running Total
        total_change = total_change + monthly_profit
    #Print the Total Amount of "Profits/Losses"
    print(f"The total change in value was: ${total_change}.")


###########Calculate the Average of the Monthly "Profits/Losses"################
#Read from the Budget_Data CSV File
#Code from Various Class Activities
with open(csv_path,"r") as csv_file:
    #Split the Data by Commas
    csv_reader = csv.reader(csv_file,delimiter=",")
    #Read the Header without Printing
    #Code from Section 3.3 Activity 1
    csv_header = next(csv_file)
    #Read the First Data Row without Printing
    csv_row1 = next(csv_file)

    #Create the List for Monthly "Profit/Loss" Change
    monthly_change_list = []
    #Initialize the Old Monthly Profit
    old_monthly_profit = 867884
    #Iterate Through All of the Rows for the Current Month
    for row in csv_reader:
        #Pull the Current Month's "Profit/Loss"
        monthly_profit = row[1]
        #Create a Variable for the Monthly Change in "Profit/Loss"
        monthly_change = int(monthly_profit) - int(old_monthly_profit)
        #Append the Monthly Change to the List
        monthly_change_list.append(monthly_change)
        #Pull the Previous Month's "Profit/Loss"
        old_monthly_profit = monthly_profit           
    #Calculate the Average of the Monthly Changes
    #Round function found on https://www.w3schools.com/python/ref_func_round.asp
    #Sum function found on https://www.geeksforgeeks.org/sum-function-python/
    avg_monthly_change = round((sum(monthly_change_list) / (row_count - 1)),2)
    #Print the Average Monthly Change
    print(f"The average monthly change is: ${avg_monthly_change}.")


###########Find the Greatest Increase and Decrease in Monthly Profits############
#Read from the Budget_Data CSV File
#Code from Various Class Activities
with open(csv_path,"r") as csv_file:
    #Split the Data by Commas
    csv_reader = csv.reader(csv_file,delimiter=",")
    #Read the Header without Printing
    #Code from Section 3.3 Activity 1
    csv_header = next(csv_file)
    #Read the First Data Row without Printing
    csv_row1 = next(csv_file)

    #Create the List for Monthly "Profit/Loss" Change
    monthly_change_list = []
    #Create the List for Months
    month_list=[]
    #Initialize the Old Monthly Profit and Change
    old_monthly_profit = 867884
    old_monthly_change = 0
    #Learned About Declaring Empty Variables from https://stackoverflow.com/questions/664294/is-it-possible-only-to-declare-a-variable-without-assigning-any-value-in-python
    old_month = None
    #Initialize the Maximum and Minimum Values
    max_value = -9999999
    min_value = 9999999
    max_value_month = 0
    min_value_month = 0
    #Iterate Through All of the Rows for the Current Month
    for row in csv_reader:
        #Create a Dictionary for Data
        dict1 = {"month":row[0], "monthly_profit":int(row[1])}
        #Calculate the Monthly Change
        monthly_change = dict1["monthly_profit"] - old_monthly_profit
        #Append the Monthly Change to the Monthly "Profit/Loss" List
        monthly_change_list.append(int(monthly_change))
        #Append the Month to the Month List
        month_list.append(dict1["month"])
        #See Whether the Current Change is Highest
        if monthly_change > max_value:
            #Change the Max Change Value
            max_value = monthly_change
            #Change the Corresponding Month
            max_value_month = dict1["month"]
        #See Whether the Current Change is Lowest
        if monthly_change < min_value:
            #Change the Min Change Value
            min_value = monthly_change
            #Change the Corresponding Month
            min_value_month = dict1["month"]
        #Pull the Previous Month's "Profit/Loss"
        old_monthly_profit = dict1["monthly_profit"]
        #Pull the Previous Month's Change
        old_monthly_change = monthly_change
        #Pull the Previous Month
        old_month = dict1["month"]    
    #Find the Greatest Increase in Profits
    print(f"The greatest increase in profits is: {max_value_month} (${max_value}).")
    print(f"The greatest decrease in profits is: {min_value_month} (${min_value}).")

#Print the Results to a txt File
with open("budget_output.txt","w") as txt_file:
    txt_file.write(f"The total amount of months is: {row_count}.\nThe total change in value was: ${total_change}.\nThe average monthly change is: ${avg_monthly_change}.\nThe greatest increase in profits is: {max_value_month} (${max_value}).\nThe greatest decrease in profits is: {min_value_month} (${min_value}).")