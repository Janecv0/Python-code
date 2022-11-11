#Firts homework (var.a)

#Fizz buzz
#Made by Vojtěch Janeček

#To change number of runs change this variable
runs=15

#Starting number
start_num=1

#To change rules (when Fizz/buzz is shown) change here
Fizz=3
Buzz=5


#Auxiliary variable
temp=start_num




#Algorithm (Option with changeable outcome for divisibility by both)

for i in range(runs):
    if temp%Fizz==0 and temp%Buzz==0:
        print("Fizz Buzz")

    elif temp%Fizz==0:
        print("Fizz")

    elif temp%Buzz == 0:
        print("Buzz")

    else:print(temp)

    temp=temp+1

print("Printing finished")