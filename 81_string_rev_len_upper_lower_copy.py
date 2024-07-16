# 081. Print string in reverse,its length,in uppercase,lowercase and copy into another string in python


string="Hellow to python and I want to learn it"
string_length=len(string)
string_reversed=''.join(reversed(string))
print("The string length = ",string_length)
print(string_reversed)
strin_uppercase=string.upper()
print("The uppercase is :- ",strin_uppercase)
string_lowercase=string.lower()
print("lowercase is = ",string_lowercase)
copy_string=string
print("copied string :- ",copy_string)
