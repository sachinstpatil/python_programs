#for loop

for i in range(2): #for loop to print numbers from 0 to 2
    print("SST")

for i in range(3): #for loop to print numbers from 0 to 2
    print(i)

my_list = ["apple", "banana", "cherry"] #a list of fruits
for i in my_list:
    print(i) #for loop to print each fruit in the list


#break statement

numbers = [1, 2, 3, 4, 5] #a list of numbers
for num in  numbers:
    if num == 3:
        break #break statement to exit the loop when num is 3
    print("Break", num)

#continue statement
for num in numbers:
    if num == 3:
        continue #continue statement to skip the rest of the loop when num is 3
    print("Continue", num)


#while loop

count = 0
while count < 3:
    count += 1 #while loop to print numbers from 1 to 3
    print(count)