import sys
import math

numbers = []

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    file_handle = open(filepath,"r")
    current_line = file_handle.readline()
    while len(current_line) > 0:
        try:
            if math.isnan(float(current_line.split("\t")[column])) == True:
                print("Warning: Data file contained NaN (Not a Number) in a column and its value was omitted.")
                current_line = file_handle.readline() 
            else:
                numbers.append(float(current_line.split("\t")[column]))
                current_line = file_handle.readline()
           
        except ValueError:
            print("Warning: Data file contained a non-numeric value in a column and the value was omitted.")
            current_line = file_handle.readline() 
        except IndexError: # exception for if user inputs non-existent column number, so program will not continue
            print("The entered column number is not present in the data file.")
            sys.exit()
   
    numbers_tuple = (numbers, len(numbers)) # creates tuple containing list of values from column and total number of values in that column
    return numbers_tuple



def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    sum = 0
    for i in numbers:
        sum += i
    if len(numbers) > 0:
        average = sum/len(numbers)
    elif len(numbers) == 0:
        average = "Your column contained too few numeric values to generate a mean average."
    return average



def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    if len(numbers) > 0:
        max_min = (max(numbers), min(numbers))
    elif len(numbers) == 0:
        max_min = "Your column contained too few numeric values to generate a maximum and a mininmum value."
    return max_min



def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    pre_variance = 0
    for i in numbers:
        pre_variance += (i-calculate_average(numbers))**2
    if len(numbers)>1:    
        variance = (1/(len(numbers)-1))*(pre_variance)
    else:
        variance = "Your column contained too few numeric values to generate a variance."
    return variance



def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    try:
        std_dev = math.sqrt(calculate_variance(numbers))
    except:
        std_dev = "Your column contained too few numeric values to generate a standard deviation."
    return std_dev



def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    pre_median = sorted(numbers)
    if len(pre_median) > 0:
        if len(pre_median)%2 == 0: # if numbers list is even
            median = (pre_median[int((len(pre_median)/2)-1)] + pre_median[int(len(pre_median)/2)])/2
        elif len(pre_median)%2 !=0: # if numbers list is odd
            median = pre_median[int(len(pre_median)/2 - 0.5)]
    elif len(pre_median) == 0:
        median = "Your column contained no numeric values."
    return median



filepath = input("Please enter the full name of the file that you want to open: ")
column = int(input("Please enter a valid column number for the file: "))

print("Column number",column,"from", filepath,"has the following list of numbers (the count of valid entries in the list appears after the list):\n", load_data(filepath,column))
print("Average:",calculate_average(numbers))
print("Maximum Value and Minimum Value from column:",get_max_and_min(numbers))
print("Variance:",calculate_variance(numbers))
print("Standard Deviation:",calculate_std_dev(numbers))
print("Median Value:",calculate_median(numbers))