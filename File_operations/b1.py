import csv

# Function to read payroll data from the 'Payroll_Jan.txt' file
def read_payroll_data():
    payroll_data = []
    with open('Payroll_Jan.txt', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            payroll_data.append(row)
    return payroll_data

# Function to count number of employees based on department and place
def number_of_employees_by_dept_place(payroll_data):
    dept_place_count = {}
    
    for data in payroll_data:
        # Create a key as a tuple (place, department)d
        key = (data['place'], data['department'])
        
        # If the key is not in the dictionary, initialize it with 0
        if key not in dept_place_count:
            dept_place_count[key] =h 
        
        # Increment the count for this department-place combination
        dept_place_count[key] += 1
    
    return dept_place_count

# Function to ensure all combinations of place and department are included with zero count
def get_all_combinations():
    places = ['Hassan', 'Bangalore', 'Mysore', 'Mangalore', 'Shimoga']
    departments = ['HR', 'Technical', 'Accounts', 'Network', 'Test']
    
    all_combinations = {}
    
    for place in places:
        for dep in departments:
            all_combinations[(place, dep)] = 0
    
    return all_combinations

# Read the payroll data from the file
payroll_data = read_payroll_data()

# Get the count of employees by department and place
employee_counts = number_of_employees_by_dept_place(payroll_data)

# Ensure all combinations are present in the result
all_combinations = get_all_combinations()

# Update the all_combinations dictionary with actual counts from employee_counts
for key, count in employee_counts.items():
    all_combinations[key] = count

# Print the final result in the required format
print(all_combinations)