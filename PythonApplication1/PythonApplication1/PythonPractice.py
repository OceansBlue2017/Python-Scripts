# Practice to learn 
'''
# Print

print ("hello Texas")

print (5 + 1000)
print (1000 - 200)
print ("Hi Nancy")

greetings = 'Welcome'
name = "Nancy"
print (greetings + ' ' + name)

##

greetings = 'Welcome'
name = input ('Please enter your name: ' )
print (greetings + ' ' + name)

# Split a string into two lines by using the \n
string1 = 'This String has been split \n by a backslash n'
print (string1)

# Tab a string by using the \t  it causes a tab space
string2 = 'This String has been tabbed  \t by a backslash t'
print (string2)

# Different ways to print a quote inside the string text
print ('Adam says "Hello from inside the qoute" ')  #  this is a method 
print ('Adam says \'Hello from inside the qoute\' ')  #  this is another method 
print ("Adam says \"Hello from inside the qoute\" ")  #  this is another method 

'''

# Udemy "The Complete Python Course"
  # Lecture No. 9  Python strings and String formating

# String with quotes
   # String_with_qoutes = "Hello it's me. "  # Use "double qoutes" because you have a 'single qoute inside the string'
   # String_with_qoutes = 'Hello "You are amazing!" good job' # Use 'single qoute' because you have a "double qoutes inside the string"

# Concatinating in Python 3.6 and above
# instead of creating the under stated
name = 'Nancy Nanoos'
# greeting = 'Hello, ' + name
# print(greeting)

# Instead we can use a new feature called f string
newgreeTing = f'Hellllo, {name}' 
print(newgreeTing)

# an older way to faormat for Python 3.5 or older
# finalgreeTing = "How you are Amar, {}"
# formated_greeting = finalgreeTing.format(name)
# print(formated_greeting)



