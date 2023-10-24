# open file and read data within file
with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

# initialize variable for lower and uppercase letter counts as 0
lowercase_count = 0
uppercase_count = 0

# initialize variable for numbers in file 
number_count = 0

#split data in file 
lines = data.split("\n")
key_value_ini = dict()

for line in lines:
    
    for char in line:
        # counter for if character is lowercase
        if char.islower():
            lowercase_count += 1
        # counter for if character is uppercase
        elif char.isupper():
            uppercase_count += 1
    for number in line:
        if number.isnumeric():
            number_count += 1
# print the ouput
print (f"There are {number_count} number(s) in the file")
print (f"There are {uppercase_count} uppercase letters in the file")
print (f"There are {lowercase_count} lowercase letters in the file")
#print(key_value_ini)
