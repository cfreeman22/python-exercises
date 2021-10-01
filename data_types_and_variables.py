# You have rented some movies for your kids: The little mermaid (for 3 days), 
#Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
#If price for a movie per day is 3 dollars, how much will you have to pay?

movies_for_kids = [{"Title": "The little mermaid", "days": 3, "Price": 3},
                   {"Title": "Brother Bear ", "days": 5, "Price": 3},
                   {"Title": "Hercules", "days": 1, "Price": 3}

]
# Lets ffind how much i would have to pay
Lmermaid_rent_price = (movies_for_kids[0]['Price'] * movies_for_kids[0]['days'])

Bbear_rent_price = (movies_for_kids[1]['Price'] * movies_for_kids[1]['days'])

Hercules_rent_price = (movies_for_kids[2]['Price'] * movies_for_kids[2]['days'])

total_price = Lmermaid_rent_price + Bbear_rent_price + Hercules_rent_price 

print("Total price I would have to Spend is $", total_price)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour Google pays 400 dollars per hour, Amazon 380, and Facebook 350.
# How much will you receive in payment for this week? 
#You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

# lets Define our variables

google_pay = 400
amazon_pay = 380
facebook_pay = 350

total_pay = (google_pay * 6) + (amazon_pay * 4) + (facebook_pay * 10)

print(" The Total pay for this week is $", total_pay)

#A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

class_full = True

Schedule_conflict = True

if class_full and Schedule_conflict:
    print("The Student cannot enroll")

else:
    print("Student can enroll")


#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

offer_not_expired = True

item_bought = 2

premiun_member = True

if premiun_member or (offer_not_expired and item_bought == 2):
    print("Apply product offer")

else:
    print("No product offer! ")



#Use the following code to follow the instructions below:

#username = 'codeup'
#password = 'notastrongpassword'
#Create a variable that holds a boolean value for each of the following conditions:

password = 'notastrongpassword'
username = 'codeup'

pass_greater_than_five = len(password) >= 5
uername_no_more_than20 = len(username) <=20
password_not_username = password == username

print(pass_greater_than_five)
print(uername_no_more_than20)
print(password_not_username)

#bonus neither the username or password can start or end with whitespace

print(password.startswith(' '))
print(username.startswith(' '))

 

