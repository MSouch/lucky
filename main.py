with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

# initialize variable for lower and uppercase letter counts as 0
lowercase_count = 0
uppercase_count = 0
number_count = 0

lines = data.split("\n")
key_value_ini = dict()
for line in lines:
    if "=" in line:
        fields = line.split("=")
        key_value_ini[fields[0]] = fields[1]
# iterate through the characters in each line
    for char in line:
        # counter for if character is lowercase
        if char.islower():
            lowercase_count += 1
        # counter for if character is uppercase
        elif char.isupper():
            uppercase_count += 1
# print the ouput
print (f"There are {uppercase_count} uppercase letters")
print (f"There are {lowercase_count} lowercase letters")
#print(key_value_ini)
