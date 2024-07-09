# Program: Password Generator
# Author: Quentin (Raijinware)
# File: passwordGenerator.py
# Purpose: The purpose of this application is to generate passwords that can be used.

# Import random for the random generation
import random
# Import tkinter for the GUI
from tkinter import *

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# PASSWORD GENERATOR RESOURCES
# lowercase letters
passwordLowerAlphabetChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# uppercase letters
passwordUpperAlphabetChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# numbers
passwordNumberChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# special characters
passwordSpecialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "`", "~", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "\'","\"", "\\", "|", ",",
                         "<", ".", ">", "/", "?"]

# all characters
passwordAllChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "`", "~", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "\'","\"", "\\", "|", ",",
                    "<", ".", ">", "/", "?"]

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# GUI SETUP

# Instantiate the password generator window
passwordGeneratorWindow = Tk()

# Give the password generator a relavent title
passwordGeneratorWindow.title("Password Generator")

# Set the size of the window
passwordGeneratorWindow.geometry('800x400')

# Ask the user if they want to generate a password
askLabel = Label(passwordGeneratorWindow, text = "Generate a new password", font=("Arial", 26))
askLabel.pack()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# CHECKBOXES
#lowercase
lower = IntVar()
lowercase = Checkbutton(passwordGeneratorWindow, text = 'lowercase', variable=lower, onvalue=1, offvalue=0, font=("Arial", 16))
lowercase.pack()

#uppercase
upper = IntVar()
uppercase = Checkbutton(passwordGeneratorWindow, text = 'uppercase', variable=upper, onvalue=1, offvalue=0, font=("Arial", 16))
uppercase.pack()

#numbers
numbers = IntVar()
numerics = Checkbutton(passwordGeneratorWindow, text = 'numerics', variable=numbers, onvalue=1, offvalue=0, font=("Arial", 16))
numerics.pack()

#special characters
special = IntVar()
specialChar = Checkbutton(passwordGeneratorWindow, text = 'special characters', variable=special, onvalue=1, offvalue=0, font=("Arial", 16))
specialChar.pack()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# FUNCTIONS
# generate a password based on the checkboxes
def generatePassword():
    passwordLength = var.get()
    password = ""
    #1111
    if(lower.get() == 1 and upper.get() == 1 and numbers.get() == 1 and special.get() == 1):
        for x in range(passwordLength):
            passwordChars = random.choice(passwordAllChars)
            password += passwordChars

    #1110
    if(lower.get() == 1 and upper.get() == 1 and numbers.get() == 1 and special.get() == 0):
        passwordChar = passwordLowerAlphabetChars + passwordUpperAlphabetChars + passwordNumberChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars

    #1101
    if(lower.get() == 1 and upper.get() == 1 and numbers.get() == 0 and special.get() == 1):
        passwordChar = passwordLowerAlphabetChars + passwordUpperAlphabetChars + passwordSpecialChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars

    #1011
    if(lower.get() == 1 and upper.get() == 0 and numbers.get() == 1 and special.get() == 1):
        passwordChar = passwordLowerAlphabetChars + passwordNumberChars + passwordSpecialChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    

    #0111
    if(lower.get() == 0 and upper.get() == 1 and numbers.get() == 1 and special.get() == 1):
        passwordChar = passwordUpperAlphabetChars + passwordNumberChars + passwordSpecialChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    

    #0110
    if(lower.get() == 0 and upper.get() == 1 and numbers.get() == 1 and special.get() == 0):
        passwordChar = passwordUpperAlphabetChars + passwordNumberChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    

    #0101
    if(lower.get() == 0 and upper.get() == 1 and numbers.get() == 0 and special.get() == 1):
        passwordChar = passwordUpperAlphabetChars + passwordSpecialChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    

    #0011
    if(lower.get() == 0 and upper.get() == 0 and numbers.get() == 1 and special.get() == 1):
        passwordChar = passwordNumberChars + passwordSpecialChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    
    #1010
    if(lower.get() == 1 and upper.get() == 0 and numbers.get() == 1 and special.get() == 0):
        passwordChar = passwordLowerAlphabetChars + passwordNumberChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    
    #1001
    if(lower.get() == 1 and upper.get() == 0 and numbers.get() == 0 and special.get() == 1):
        passwordChar = passwordLowerAlphabetChars + passwordSpecialChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    
    #1100
    if(lower.get() == 1 and upper.get() == 1 and numbers.get() == 0 and special.get() == 0):
        passwordChar = passwordLowerAlphabetChars + passwordUpperAlphabetChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    
    #0100
    if(lower.get() == 0 and upper.get() == 1 and numbers.get() == 0 and special.get() == 0):
        passwordChar = passwordUpperAlphabetChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    
    #1000
    if(lower.get() == 1 and upper.get() == 0 and numbers.get() == 0 and special.get() == 0):
        passwordChar = passwordLowerAlphabetChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars            
    
    #0010
    if(lower.get() == 0 and upper.get() == 0 and numbers.get() == 1 and special.get() == 0):
        passwordChar = passwordNumberChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    
    #0001
    if(lower.get() == 0 and upper.get() == 0 and numbers.get() == 0 and special.get() == 1):
        passwordChar = passwordSpecialChars
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    
    #0000
    if(lower.get() == 0 and upper.get() == 0 and numbers.get() == 0 and special.get() == 0):
        passwordChar = [" "]
        for x in range(passwordLength):
            passwordChars = random.choice(passwordChar)
            password += passwordChars    

    text = StringVar()
    text.set(password)
    passwordEntry.config(state="normal")
    passwordEntry.config(textvariable = text)
    passwordEntry.config(state="readonly")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# SLIDER
var = IntVar()
slider = Scale(passwordGeneratorWindow, variable = var, from_= 8, to = 25, font=("Arial", 24), orient=HORIZONTAL)
slider.configure()
slider.pack(pady=10)

# GENERATE PASSWORD BUTTON
genPasswordButton = Button(passwordGeneratorWindow, text = "Generate Password", command = generatePassword)
genPasswordButton.pack(pady=10)

# PASSWORD OUTPUT HERE
passwordEntry = Entry(passwordGeneratorWindow, font=("Arial", 24), bd = 0, state="readonly", justify='center', width=30)
passwordEntry.pack(pady=10)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# run the window
passwordGeneratorWindow.mainloop()