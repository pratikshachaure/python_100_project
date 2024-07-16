
char_count=0
letter_count=0
special_char_count=0
string="Hellow to string my gmail 1 2 5 0 & $ is abc@gmal.com # programming "
for i in range(len(string)):
    # print(string[i])
    find_ascii=ord(string[i])
    if find_ascii>=33 and find_ascii<=47:
        special_char_count+=1
    elif find_ascii>=48 and find_ascii<=57:
         letter_count+=1
    else:
         char_count+=1

print("The total special character is :- ",special_char_count)
print("The total digit is ",letter_count)
print("The total characters are : ",char_count)
     

