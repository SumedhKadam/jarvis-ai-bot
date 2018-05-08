#from __future__ import division

from kivy.app import App
from kivy.uix.widget import Widget
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
import subprocess
#from gtts import gTTS
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-80)

class display(Widget):
    #def speak(self,a):
        #engine.say(a)
        #engine.runAndWait()  
    def send(self,instance):
	
            self.bot.text = "Elina listening..."
            r = sr.Recognizer()
            r.energy_threshold = 500
		#self.bot.text = ""
            
            
            engine.say("Elina listening...")
            engine.runAndWait()
            
        #engine.runAndWait()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                data = ""
                data = r.recognize_google(audio)
                data = data.lower()
            except sr.UnknownValueError:
                self.bot.text = "Sorry Sumedh.I could not understand your audio."
            
                engine.say("Sorry Sumedh.I could not understand your audio.")
                engine.runAndWait()
            except sr.RequestError as e:
                self.bot.text = "Could not request results from Google Speech Recognition service"
            
                engine.say("Could not request results from Google Speech Recognition service")
                engine.runAndWait()
            self.bot.text = ""
            if "how are you" in data:
                self.bot.text = "I am fine"
            
                engine.say("I am fine")
                engine.runAndWait()
          
 
            elif "time" in data:
                self.bot.text = str(ctime())
                engine.say(ctime())
                engine.runAndWait()
                
            
 
            elif "where is" in data:
        #data = data.split(" ")
                location = data[8:]
                self.bot.text = "Hold on Sumedh, I will show you where" + str(location) + " is"	
                webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")
                engine.say("Hold on Sumedh, I will show you where " + location + " is.")
                engine.runAndWait()
				
            elif "video" in data:
                subprocess.call([r"C:\Program Files\VideoLAN\VLC\vlc.exe",r"C:\Users\Admin\Documents\cr7.mp4"])	

            elif "microsoft word" in data:
                subprocess.call([r"C:\Program Files\Microsoft Office\Office12\WINWORD.exe"])

            elif "microsoft powerpoint" in data:
                subprocess.call([r"C:\Program Files\Microsoft Office\Office12\POWERPNT.exe"])				
            
            
                
            #engine.say(self.bot.text)
            #engine.runAndWait() 
        		


class chatbotApp(App):
    def build(self):
        return display()
if __name__ == '__main__':
    chatbotApp().run()