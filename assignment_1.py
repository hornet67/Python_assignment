#PROGRAM 3
for num1 in range(1,100):
    if num1%3==0:
        print("Fizz")
    elif num1%5==0:
        print("Buzz")
    else:
        print(num1)


#program 1

for numbers in [1,2,88,42,99]:
    if numbers == 42:
        break
    print(numbers)

#problem 2
value = int(input("Enter the number: "))


for i in range(1,value):
    num = 0
    num=num+i
    print(num)
    i+=num
    
     #  try korsi pari nai