#N numbers will be received according to the N values entered by the user.
#The received numbers will be thrown into a function, which will replace the 
#even numbers of the N numbers sent as parameters with an odd number (one more than itself).  
#Then the odd numbers obtained will be printed on the screen in the function and the total 
#number of times the substitution operation is performed will also be printed.

n=int(input("distance of list="))
def odd_numbers(n):
    numbers=[]
    counter=0
    for i in range(n):
        y=int(input("numbers="))
        if y%2==1:
            y+=1
            counter+=1

        numbers.append(y)
    print(numbers)
    print(counter)
    

odd_numbers(n)





#The number of cells in the body of a living being is given as N. In one minute
#all the cells are dividing by mitosis and at the same time in one minute 20% of the existing cells die.
#In one minute, first the cells multiply by mitosis; after the multiplication process is over, death takes place.
#type a program that calculates the total number of cells after 10 minutes after the number of existing cells N 
# is taken from external sources.
 

n=int(input("cell number="))
i=1
total=0
for i in range(1,11):
    first_condition= n*2
    second_condition=first_condition-(first_condition*20/100)
    n= second_condition
    total+=second_condition
print(total)    
