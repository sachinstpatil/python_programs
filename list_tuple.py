#list

random_list = [1, "apple", 3.14, True] #a list can contain different types of data
print(random_list)

my_list = ["apple", "cherry", "banana"] #square brackets are used to define a list
print(my_list)

print(type(my_list)) #type() function is used to get the type of the variable
print("length of my_list:", len(my_list)) #len() function is used to get the length of the list

print("Sliced list - ", my_list[0:2]) #slicing the list to get the first two elements

my_list.sort()
print("Sorted list - ", my_list)

appended_list = my_list.append("orange")
print(my_list)

appended_list = my_list.remove("orange")
print(my_list)

first_element = my_list[0]  # Access the first element
print(first_element)

print("Concatenating the first two elements of the list", my_list[0]+ "--" + my_list[1]) #concatenating the first two elements of the list

#tuple

my_tuple = ("apple", "banana", "cherry") #parentheses are used to define a tuple
print(my_tuple)

print(type(my_tuple)) #type() function is used to get the type of the variable
print("length of my_tuple:", len(my_tuple))  #len() function is used to get the length of the tuple

#appeended_tuple = my_tuple.append("orange") #tuples are immutable, so this will raise an error