#Firts homework (var. b)
        #TLDR: Easier to add divisibility rules

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
output=""



#Algorithm 2 (Expendable algorithm for multiple easily addible divisibility rules)


for n in range(runs):
    output=""

    #divisibility rules
    if temp%Fizz==0: output+= "Fizz"
    if temp%Buzz==0: output+= "Buzz"

    #check if anything was added to output
    if output=="": output=f"{temp}"

    print(output)

    temp=temp+1


print("Printing finished")