string="Hellow to string my gmail 1 2 5 0 & $ is abc@gmal.com # programming "
for i in range(len(string)):
    # print(string[i])
    find_ascii=ord(string[i])
    if find_ascii>=33 and find_ascii<=47:
        print("special char is :-",string[i])
    elif find_ascii>=48 and find_ascii<=57:
        print("digit is :- ",string[i])
    else:
        print("other symbol is :- ",string[i])
     
