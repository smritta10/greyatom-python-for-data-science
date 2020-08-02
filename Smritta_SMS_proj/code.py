# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class = class_1 + class_2
#print('New Class list: ', new_class)

# Append the list
new_class.append('Peter Warden')

# Print updated list
#print('Appended Class list: ', new_class)

# Remove the element from the list
new_class. remove('Carla Gentry')

# Print the list
print('New list: ', new_class)

# Create the Dictionary
courses = {'Math': 65, 'English':70, 'History': 80, 'French': 70, 'Science': 60}

# Slice the dict and stores  the all subjects marks in variable
# Store the all the subject in one variable `Total`
total = 65 + 70 + 80 + 70 + 60
# Print the total
print('Total Marks: ', total)

# Insert percentage formula # Print the percentage
percentage= (total/500)*100
print('Percentage is: ', percentage)


# Create the Dictionary
mathematics = {'Geoffrey Hinton': 78, 'Andrew Ng': 95, 'Sebastian Raschka' : 65, 'Yoshua Benjio': 50, 'Hilary Mason': 70, 'Corinna Cortes': 66, 'Peter Warden': 75}

topper = max(mathematics, key=mathematics.get)
print('max marks scored by: ', topper)

# Given string # Create variable first_name  # Create variable Last_name and store last two element in the list
first_name = topper.split()[0]
last_name = topper.split()[1]

# Concatenate the string
full_name = last_name + ' ' + first_name

# print the full_name
print('Full name is:' , full_name)

# print the name in upper case
certificate_name = full_name.upper()
print('Cert name: ', certificate_name)

# Code ends here


