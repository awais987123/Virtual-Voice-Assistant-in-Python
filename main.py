import pyttsx3 as p
import speech_recognition as sr

from selenium_web_driver import *
from YT_selenium import *
from News import *
import randfacts
import pyjokes
from weather import *

#intialize voice  
engine = p.init()
#set voice speed
rate= engine.getProperty('rate')
engine.setProperty('rate',150)
#set voice (male/female)
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

# function to speak voice assistent
def speak(text):
    engine.say(text)
    engine.runAndWait()


print("ChatBot :Hello Sir, i am your Bestie.How are you")
speak("Hello Sir, i am your voice assistent.")
speak( "Temprature in Bhalwal is "+str(temp())+"degree celcius"+ " and with " + str(des()))
speak("How are you")
r= sr.Recognizer()
text =[]
audio= []
def listen():
    text=[]
    with sr.Microphone() as source:
      r.energy_threshold=10000
      r.adjust_for_ambient_noise(source,1.2)
      print("listening...")
      audio =r.listen(source)
      text= r.recognize_google(audio)
      print(text)

listen()    

if "what" or "äbout" or "you" in text:
      print("ChatBot :i am also having a good day")
      speak("i am also having a good day")
print("ChatBot :what i can do for you")
speak("what i can do for you")
with sr.Microphone() as source:
      r.energy_threshold=10000
      r.adjust_for_ambient_noise(source,1.2)
      print("listening...")
      audio =r.listen(source)
      text= r.recognize_google(audio)
      print("You :"+text)

if "information"  in text:
    speak("You need information related to which topic")
    with sr.Microphone() as source:
      r.energy_threshold=10000
      r.adjust_for_ambient_noise(source,1.2)
      print("listening...")
      audio =r.listen(source)
      text= r.recognize_google(audio)
      print(text)
 
    speak("searching {} in wikipedia ".format(text))
    assist =infow()
    assist.get_info(text)
     
elif  "song" in text:
    speak("You want to play which song")
    with sr.Microphone() as source:
      r.energy_threshold=10000
      r.adjust_for_ambient_noise(source,1.2)
      print("listening...")
      audio =r.listen(source)
      text= r.recognize_google(audio)
      print(text)
 
    speak("playing {} in youtube ".format(text))
    assist =music1()
    assist.play(text)
    

elif "news" in text:
  arr=news()
  
  print("I am going to read top latest news for you")
  speak("I am going to read top latest news for you")
  print(arr)
  speak(arr)

elif  "facts" in text:
      print("ChatBot :Sur Sir,")
      speak("Sure Sir ,")
      x=randfacts.getFact() 
      print("ChatBot :Did you know that " + x)
      speak("Did you know that "+x)

elif "jokes" in text:
  print("ChatBot :Sure Sir, get ready for some chukkles")
  speak("Sure Sir, get ready for some chukles")
  x=pyjokes.get_joke(language="en", category="twister")
  print("ChatBot :You know Sir")
  speak("You know Sir ," + x)

