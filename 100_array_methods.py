# Append method:- The append method appends an element to the end of the list.

arr=[10,20,30]
arr.append("Pratiksha")
print("Array :- ",arr)

arr2=[1,2,3,4,5]
arr.append(arr2)
print(arr)


# Clear method:- The clear method removes all the elements from a list...


arr=["Hellow","Hii","Hey"]
arr.clear()
print("Empty array :- ",arr)


# The count() method returns the number of elements with the specified value.


arr=[1,4,3,"Pratiksha",4,6,7,4]
x=arr.count(4)

print("count = ",x)



# Array extend :- Add the elements of a list (or any iterable), to the end of the current list

first_arr=["Hellow","hii","hey"]
second_arr=[1,2,3,4,5,6]
first_arr.extend(second_arr)
print("First Array :- ",first_arr)


# Array_index:- Return the position at the first occurance of the specified value

index1=first_arr.index("hey")
print("The index of the element is :- ",index1)


# The insert element at specific position 
insert_arr=["Pratiksha","Akanksha","Amruta"]
insert_arr=[1,2,3,4,5,6]
insert_arr.insert(4,"Inserted_Element")
print("Inserted_array :",insert_arr)


# pop method :Removes the element at the specified position
pop_array=["laptop","PC","Mobile","Tab"]
pop_array.pop(1)
print("Popped Array :- ",pop_array)



# remove method:- Removes the first item with the specified value...



remove_arr=[1,2,3,4,"Pratiksha"]
remove_arr.remove("Pratiksha")
print("Removed Array :- ",remove_arr)


# reverse method :- Reverses the order of the list...

reverse_arr=[100,200,300,400,500]
reverse_arr.reverse()
print("Reversed Array :- ",reverse_arr)




# sort method:- Sorts the list

sort_arr=["Pratiksha","Amruta","Akshta"]
sort_arr.sort()
print("The sorted array :- ",sort_arr)

