''' Conditional Basics

Q1 a) prompt the user for a day of the week, print out whether the day is Monday or not

b) prompt the user for a day of the week, print out whether the day is a weekday or a weekend

c) create variables and make up values for

the number of hours worked in one week
the hourly rate
how much the week's paycheck will be
write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours '''

#Lets create variables

day_of_the_week = input('Please enter the day of the week : ')

if day_of_the_week == 'monday' or 'monday'.capitalize():
    print('The day is ',day_of_the_week)

# Q1 b) prompt the user for a day of the week, print out whether the day is a weekday or a weekend
days = ['monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday ']



day_of_the_week = input('Please enter the day of the week : ')

weekdays = days[:5]
weekends = days[5:7]

if day_of_the_week in weekdays:
    print(day_of_the_week, " is a weekday")
else:
    print(day_of_the_week,' is a weekend')

#Q1 c) write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours '''

hourly_rate = 30 
reg_hours_per_week = 40
 

over_time_pay = hourly_rate * 1.5


user_hours_per_week = int(input(" Enter your number of hours "))
if user_hours_per_week > reg_hours_per_week:
    over_time = user_hours_per_week - reg_hours_per_week
    weekly_pay = (reg_hours_per_week * hourly_rate) + (over_time * over_time_pay)
    print('Your weekly Pay is ', weekly_pay)
    
else:
    weekly_pay = user_hours_per_week * hourly_rate
    print(' Your wekkly pay is ', weekly_pay)


#Q2 Loop Basics
#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15

#Q2 a) While
 
 i = 5

while i < 15:
    print(i)
    i += 1




#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0

while i <= 100:
    print(i)
    i += 2
    

#Alter your loop to count backwards by 5's from 100 to -10.
i = 100 

while i >= -10:
    print(i)
    i = i - 5
    

#Create a while loop that starts at 2, 
#and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2 

while i < 1000000:
    print(i)
    i *= i



# Write a loop that uses print to create the output shown below.
i = 100 

while i > 5:
    print(i)
    i = i - 5 
    
    


#Q2 b For Loops 
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

user_num = int(input(" Enter your number : "))
for i in range(1,11):
    print(f'{user_num} * {i} = {user_num * i}')



# b 2)Create a for loop that uses print to create the output shown below.

for i in range(1,10):
    print(i*str(i))

#Q 2c break and continue
usernum = int(input(' Enter a positive number '))
while usernum >=0 and usernum < 50:
    for i in range(1, 50):
        if usernum == i :
            print(f'Yikes! Skipping number: {i}')
        elif i % 2 ==0:
            continue
        else:
            print(f'Here is an odd number: {i}')
            
       
    
    break



#Q2 d) 
user_input = int(input(' Enter a positive number : ')) 
while user_input >=0:
    for i in range(0, user_input +1):
        print(i)
    break    

#Q 2 e)Write a program that prompts the user for a positive integer.
usernum = int(input(' Enter a positive number '))

i = usernum 

while i > 0:
    print(i)
    i = i - 1 

#Q3 One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory,
# the test is designed to test basic looping and conditional logic skills.
'''Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz"'''

for i in range(1, 101):
    if i % 3 ==0 and i % 5 ==0:
        print('FizzbBuzz!')
        
    elif i % 3 ==0 :
        print('Fizz')
    elif i % 5 ==0:
        print('Buzz')
    else:
        print(i)


#Q4 Display a table of powers.

#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.

user_num = int(input("What number would you like to go up to? : "))
print('Here is your table')
print("Number  ", " Square ", " Cube ")
i = 1
while i <= user_num:
    print(i,"        ", i*i,"      ",i*i*i )
    i +=1
    



 






