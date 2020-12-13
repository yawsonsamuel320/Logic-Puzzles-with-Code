from random import *

# (The Three Alien Gods Logic Puzzle)
# The following Logic Puzzle can be found on Ted-Ed:    https://www.youtube.com/watch?v=LKvjIsyYng8&vl=en

# The Puzzle Conditions



# (Condition 1)
# Unknown meanings of Ozo and Ulu
# Ozo is either True or False
x = choice([True, False])
alien_language = {x:"Ozo", not x : "Ulu" }



# (Condition 2)
# Define the three alien's behaviour as functions
# Questions have yes or no answers

# Tee
def ask_Tee(question):
    return (alien_language[question])

# Eff
def ask_Eff(question):
    return (alien_language[not question])

# Arr
def ask_Arr(question):
    random_answer = choice([True,False])
    return (alien_language[random_answer])



# (Condition 3)
# We don't know the exact position of each alien
# Arrange the aliens in a random sequence
alien = ["Eff","Arr","Tee"]
shuffle(alien)


# Create a list of functions which corresponds to the order in which the aliens stand
# These are functions linked to those that ask each alien a question
ask_alien = [1,2,3]
for i in range(3):
    if alien[i] == "Eff":
        ask_alien[i] = ask_Eff

    elif alien[i] == "Tee":
        ask_alien[i] = ask_Tee  

    elif alien[i] == "Arr":
        ask_alien[i] = ask_Arr              








# (My Solution using code)

# Create a list for a random guess
# This changed whenever a fact is verified
my_guess = ["Tee","Eff","Arr"]


# (Condition 4)
# I have only 3 possible questions
# Think of all the possible answer sequence 



# (Question 1)
# First ask the middle alien if the alien to his left is Arr (Ask using double question intuition)
# If he says "Ozo", either he or the alien to his left is Arr
# In that case, ask the alien to your right next
# Let i equal 2


if ask_alien[1](ask_alien[1](alien[0] == "Arr") == "Ozo") == "Ozo":
    i = 2
    j = 0
    
 

# If he says "Ulu", either he or the alien to his right is Arr
# In that case, ask the alien to your left
# Let i equal 0
else:
    i = 0
    j = 2




# (Question 2)
# Ask that alien at index i (whether 0 or 2) if he is Tee
# If he answers in the affirmative, then he is indeed Tee
if ask_alien[i](ask_alien[i](alien[i] == "Tee") == "Ozo") == "Ozo":

    my_guess[i] = "Tee"



# If he answers in the negative, he is Eff
else:
    my_guess[i] = "Eff"

    
    





# (Question 3)
# Since alien[i] can't trick me, I can find out from him if the middle alien is Arr
# Affirmative => alien[1] == "Arr" 
# In that case the remaining alien is Tee or Eff opposite to the identity of the alien at i
if ask_alien[i]((ask_alien[i](alien[1] == "Arr") == "Ozo")) == "Ozo":
    my_guess[1] = "Arr"



    if my_guess[i] == "Tee":
        my_guess[j] = "Eff"

    else:
        my_guess[j] = "Tee"



# Negative => alien[1] != "Arr" 
else:

# If alien[i] is Tee, and middle alien isn't Arr he's definitely Eff
    if my_guess[i] == "Tee":
        my_guess[1] = "Eff"
        my_guess[j] = "Arr"

# If alien[i] is Eff, and middle alien isn't Arr, he's definitely Tee
    else:
        my_guess[1] = "Tee"
        my_guess[j] = "Arr"






# If my code is write print a note of hearty congratulations
if my_guess == alien:
    print("Chale, you do all!")
    
    print("Our names are: ")
    for alien in my_guess:
        print(alien)


