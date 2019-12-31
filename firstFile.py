import random
import sys
import time
from art import *

# This fancy code prints out the cool header art! Don't worry if you don't understand it.
total = 0
header = text2art("InCtrl")
print(header)

typing_speed = 350
def slow_type(msg):
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

def print_char(array):
  for each in array:
    print(each)

def print_Options(arr):
  for each in range(len(arr)):
    slow_type(str(each) + " – " + arr[each])

def addTotal(number, amt):
  amt = amt + number
  return total

slow_type("Hey you! Hello hello. You stopped to play. Now it's time to game. My name's BMO and I'll be your narrator today. You are a future computer scientist and will be going through a series of journeys. Choose wisely every step of the way.")

ascii_human = [" o ", "/|\\", "/ \\"]
print_char(ascii_human)
slow_type("hehe das me")
print("")

slow_type("So first thing's first. Who would you like to be?")
characters = ["Ada Lovelace", "Grace Hopper", "Elizabeth Holmes", "Hedy Lemarr"]
print_Options(characters)
print()

name=input()
name=characters[int(name)]

slow_type("Welp! Great to meet you " + name + "! Now it's time to choose an age you'd like to start at. Type in the age you'd like to start with:")
age = int(input())
total = addTotal(age, total)

if (age < 19):
  slow_type("You're doing great so far sweetie! Since you're still young, you have a lot of free time and options to what you can do. Choose one of the following activities you'd like to engage in:")
  activities = ["learn math and science", "explore and wander New York City", "sell C++ compilers to Chinese Universities", "Take acting classes", "be a nerd"]
  print_Options(activities)
  activity = int(input())
  active = activities[activity]
  funnyNote = ["haha nerd", "okurr adventurerr", "Will you give me a discount?", "Can I get your autograph?", "hehe"]
  slow_type("Ahhh okay so you chose the '" + active + "'" + " life. " + funnyNote[activity])

  slow_type("10 years l a t e r...")
  print()

slow_type("Wow you're older now and it's time to choose what you want to do:")
afterHS = ["translate an article on Charles Babbage's analytical engine","Attend college", "Drop out of college", "Begin acting as an Austrian actress"]

print_Options(afterHS)

numAfterHSactivity = int(input())
afterHSactivity = afterHS[numAfterHSactivity]

slow_type("How amazing! It's been a minute, and you've been able to become successful in your field. However, you're getting a little bored. Choose what you'd like to do next.")

boredChoices = ["Commit to my work", "Explore new areas", "Take a break"]
print_Options(boredChoices)
jobNum = int(input())
job = boredChoices[jobNum]

slow_type("Wowww... It's been 15 years since then and you've left your legacy in the world.")

if(name == "Elizabeth Holmes"):
  slow_type("You had created a company called Theranos and were sortaaa succesful but then everyone found out you were scamming people and now you're convicted in jail congrats! :))")
elif(name == "Grace Hopper"):
  slow_type("You're sucessful!! You created the world's first compiler and founded the word bug when you found a moth creating an issue with your computer!")
elif(name == "Ada Lovelace"):
  slow_type("You're sucessful!! You were the first computer programmer!")
else:
  slow_type("You're succesful!! You created a GPS chip used in phones today while becominga famous actress! Thanks for playing!")

finalText = text2art("The End")
slow_type(finalText)
