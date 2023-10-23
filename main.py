with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()
lowercase_count = 0
uppercase_count = 0

lines = data.split("\n")
key_value_ini = dict()
for line in lines:
    if "=" in line:
        fields = line.split("=")
        key_value_ini[fields[0]] = fields[1]
    for char in line:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
print (uppercase_count)
print (lowercase_count)
print(key_value_ini)
