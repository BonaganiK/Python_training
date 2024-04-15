print("Wlcome to my quiz game")

playing = input("Do you want play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play ")  
score = 0

answer = input(" what is the capital city of india? ")
if answer.lower() == "new delhi":
    print ("Correct")
    score += 1  #(+=)component operator
else:
    print ("Incorrect!")  

answer = input (" what is the capital city of South Africa? ")
if answer.lower() == "cape town":
    print("correct!")
    score += 1
else:
    print ("Incorrect!")  


answer = input (" what is the capital city of USA? ")
if answer.lower() == "washington":
    print("correct!")
    score += 1
else:
    print ("Incorrect!")  


answer = input (" what is the capital city of China? ")
if answer.lower() == "beijing":
    print("correct!")
    score += 1
else:
    print ("Incorrect!")  

answer = input (" what is the capital city of Japan? ")
if answer.lower() == "tokyo":
    print("correct!")
    score += 1
else:
    print ("Incorrect!")  

print("You got " + str(score) + " question correct!")  

# integer converting to string (Concatenation operators join multiple strings into a single string. There are two concatenation operators, + and & .)

