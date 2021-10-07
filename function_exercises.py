#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1- Define a function named is_two. It should accept one input and return True 
# if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    return x == 2 or x == str(2)
        
# This Function checks if the input is the interger or the string (number)


# In[2]:


is_two(2)


# In[3]:


is_two(3)


# In[4]:


is_two(5)


# In[5]:


# 2- Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(x):
    return x  in ["a","A", "e", "E", "i", "I", "o", "O", "u", "U"]


# In[6]:


is_vowel('e')


# In[7]:


is_vowel('b')


# In[8]:


#D 3 - Define a function named is_consonant. 
#It should return True if the passed string is a consonant, False otherwise. 
#Use your is_vowel function to accomplish this
def is_consonant(x):
    return x  not in ["a","A", "e", "E", "i", "I", "o", "O", "u", "U"]


# In[9]:


is_consonant('e')


# In[10]:


is_consonant('b')


# In[11]:


is_consonant('o')


# In[12]:


# 4 - Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word 
#if the word starts with a consonant.
def str_capitalize(x):
    vowels = ["a","A", "e", "E", "i", "I", "o", "O", "u", "U"]
    if any([x.startswith(i) for i in vowels]):
        return x
    else:
        return x.capitalize()
        


# In[13]:


str_capitalize('oraNGe')


# In[14]:


str_capitalize('christian')


# In[15]:


str_capitalize('arent')


# In[16]:


str_capitalize('order')


# In[17]:


# 5- Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) and the bill total, 
#and return the amount to tip
def calculate_tip(total_bill,tip_percentage):
    return total_bill * (tip_percentage / 100) 


# In[18]:


calculate_tip(100, 9)


# In[19]:


calculate_tip(2300, 8.75)


# In[20]:


calculate_tip(28.34, 8.75)


# In[21]:


# 6 - Define a function named apply_discount. 
#It should accept a original price, and a discount percentage,
#and return the price after the discount is applied.

def apply_discount(orgn_price, discount):
    return orgn_price - (orgn_price * (discount /100))
    


# In[22]:


apply_discount(100, 10)


# In[23]:


apply_discount(2300,10)


# In[24]:


apply_discount(4000, 2)


# In[25]:


# 7 -Define a function named handle_commas. It should accept a string that is a number
# that contains commas in it as input, and return a number as output.
def handle_commas(x):
    return int(x.replace(',',''))


# In[26]:


handle_commas('100,000')


# In[27]:


handle_commas('1,000,000')


# In[28]:


# 8- Define a function named get_letter_grade. It should accept a number 
#and return the letter grade associated with that number (A-F)
def get_letter_grade(x):
    if x >= 90 :
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    elif x >= 50:
        return 'E'
    else:
        return 'F'
        
    


# In[29]:


get_letter_grade(90)


# In[30]:


get_letter_grade(89)


# In[31]:


get_letter_grade(75)


# In[32]:


get_letter_grade(62)


# In[33]:


get_letter_grade(54)


# In[34]:


get_letter_grade(40)


# In[35]:


# 9- Define a function named remove_vowels that accepts a string 
# and returns a string with all the vowels removed.
def remove_vowels(x):
    vowels = ["a","A", "e", "E", "i", "I", "o", "O", "u", "U"]
    novowels = [ch for ch in x if ch not in vowels]
    novowels =''.join(novowels)
    
    return novowels


# In[36]:


remove_vowels('banana')


# In[37]:


remove_vowels('bouton')


# In[38]:


remove_vowels('poolhouse')


# ### 10 -Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# * for example:
#   * Name will become name
#   * First Name will become first_name
#   * % Completed will become completed

# In[39]:


def normalize_name(x):
    for char in x :
        if (char.isalnum() == False and char != ' '):
            x = x.replace(char,"")
    x = x.lower().strip()
    x = x.replace(' ','_')
    
    return x

    #new_string = x.lower().strip('%#[(])^$@*,;:" "\=/?<|-.!\\~&+`}>//{')
    #final_string = new_string.replace(' ','_')
    #return final_string


# In[40]:


normalize_name(' {com}pleted %Exe%ci!se .')


# In[41]:


normalize_name('Christian Freeman')


# In[42]:


normalize_name("Paige")


# In[43]:


normalize_name("Paige GUajardo")


# In[44]:


normalize_name("#$% Paige")


# In[45]:


normalize_name("Paige Josiah Guajardo")


# In[46]:


normalize_name('%Completed')


# In[47]:


# 11 -Write a function named cumulative_sum that accepts a list of numbers
#and returns a list that is the cumulative sum of the numbers in the list.

def cumulative_sum(x):
    newlist =[]
    y =0
    for i in range(len(x)):
        y +=x[i]
        newlist.append(y)
    return newlist
    
    


# In[48]:


cumulative_sum([1, 2, 3, 4])


# In[49]:


cumulative_sum([1,1,1])


# In[50]:


cumulative_sum([1,2,3,4,5,6,7,8,9])


# In[ ]:




