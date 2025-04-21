import pyttsx3

human = pyttsx3.init()          #Creating an object
say = input("What to say: ")
human.say(say)
human.runAndWait()