#!/usr/bin/python3.7

from tkinter import*
from PIL import ImageTk, Image
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os, sys, wolframalpha, subprocess
import smtplib
import pyautogui

client = wolframalpha.Client('PV6W78-VGP8HYL2UK')

print("Initializing Elvis...")

MASTER = "Abdu"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
engine.setProperty('rate', 140)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#function to wish on corresponding time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("how may i help you?")

#function to take commands from microphone

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-us')
        print(f"user said: {query}\n")
    except Exception as e:
        speak("Sir i'm unable to hear you, can you say that again...? ")
        
        query = None

    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abduzabi20@gmail.com', '')
    server.sendmail("abdulsabiq20@gmail.com", to, content)

#main program

def wish():
    speak("Initializing Elvis....")
    wishMe()

class Widget:
    def __init__(self):
        root = Tk()
        root.wait_visibility(root)
        root.wm_attributes('-alpha',0.8)
        root.title('Elvis.Ai')
        root.config(background='firebrick1')
        root.geometry('490x280')
        root.resizable(0, 0)
        icon = PhotoImage(file='icon.gif')   
        root.tk.call('wm', 'iconphoto', root._w, icon)

        self.compText = StringVar()

        compFrame = LabelFrame(root, text="El'vis v2.0",  font=('Black ops one', 9, 'bold'))
        compFrame.pack(fill="both", expand="yes")

        left1 = Message(compFrame, textvariable=self.compText, bg='snow',fg='grey1')
        left1.config(font=("Comic Sans MS", 9, 'bold'))
        left1.pack(fill='both', expand='yes')

        left1 = Label(compFrame, text="Devt: abdu_zaabi", bg='snow',fg='grey1', justify='left')
        left1.config(font=("Comic Sans MS", 10, 'bold'))
        left1.pack(fill='both', expand='no')

        btn = Button(root, text='Speak..', font=('Black ops one', 10, 'bold'), bg='snow', fg='ghostwhite', command=self.clicked).pack(fill='x', expand='no')

        btn2 = Button(root, text='Close', font=('Black Ops One', 10, 'bold'), bg='snow', fg='white smoke', command=root.destroy).pack(fill='x', expand='no')

        root.bind("<Return>", self.clicked, root.destroy)

        root.mainloop()

    def clicked(self):
            query = takeCommand()
            query = query.lower()
            self.compText.set(query)
            

    #Logic for executing task as per query

            if 'wikipedia' in query.lower():
                speak('Searching wikipedia....')
                query = query.replace("wikipedia", "")
                results =wikipedia.summary(query, sentences =2)
                speak(results)
                self.compText.set(results)

            elif 'open youtube' in query.lower():
                 webbrowser.open("youtube.com")
                 url = "youtube.com"
                 webbrowser.get('firefox').open(url)
                 speak('opening youtube....')
                 self.compText.set('opening youtube')

            elif 'open browser' in query.lower():
                 webbrowser.open("google.com")
                 url = "google.com"
                 webbrowser.get('firefox').open(url)
                 speak('opening browser...')
                 self.compText.set('opening browser...')

            elif 'open reddit' in query.lower():
                 webbrowser.open("reddit.com")
                 url = "reddit.com"
                 webbrowser.get('firefox').open(url)
                 speak('opening reddit....')

            elif 'open gaana' in query.lower():
                webbrowser.open("gaana.com")
                url = "gaana.com"
                webbrowser.get('firefox').open(url)
                speak('opening gaana....')

            elif 'open terminal' in query.lower():
                self.compText.set('opening terminal...')
                speak("Opening terminal")
                os.system("konsole -e 'su -l'")

            elif 'the time' in query.lower():
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"{MASTER} the time is {strTime}")


            elif 'send email' in query.lower():
                try:
                    speak("what should i send")
                    content = takeCommand()
                    to = takeCommand()
                    sendemail(to, content)
                    speak("Email has been send successfully")
                except Exception as e:
                    print(e)

            elif 'google search' in query.lower():
                query = query.replace("google search", "")
                url = 'https://www.google.com/search?client=firefox-b-e&q='
                search_url = url + query
                webbrowser.open(search_url)
                speak('Searching Google...')
                self.compText.set('Searching Google...')

            elif 'youtube play' in query.lower():
                query = query.replace("youtube", "")
                url = 'https://www.youtube.com/results?search_query= '
                search_url = url + query
                webbrowser.open(search_url)
                speak('Searching Youtube..')
                self.compText.set('Searching Youtube...')

            elif 'tell me' in query.lower():
                query = query.replace("tell me"," ")
                client = wolframalpha.Client('PV6W78-VGP8HYL2UK')
                res = client.query(query)
                output = next(res.results).text
                print(output)
                speak(output)
                self.compText.set(output)
                return

            elif 'shutdown' in query.lower():
                speak('System shutting down')
                os.system("shutdown now -h")

            elif 'reboot' in query.lower():
                speak('Rebooting System')
                os.system("systemctl reboot -i")

            elif 'introduce yourself' in query.lower():
                speak("Hai, i am Elvis. i am an Artificial Intelligence and a personal assistant"
                      "developed by Abdul Sabiq... i call him as Abdu,"
                      "i was developed using python... and i am under development...")

            elif 'bye' in query.lower():
                speak("okay..")
                exit()

            elif 'update' in query.lower():
                speak("System Updating")
                os.system("konsole -e 'sudo apt-get update'")
                speak("Update Completed..")
            

            elif 'upgrade' in query.lower():
                speak("System Upgrading")
                os.system("konsole -e 'sudo apt-get upgrade'")
                speak("Upgrade Completed..")

            elif 'security mode' in query.lower():
                speak("switching to security mode...")
                pyautogui.hotkey('winleft', 'tab')              
                speak("...turning on anonymity tools..")
                speak("...changing IP..")
                speak("...system has been secured..")

            elif 'default mode' in query.lower():
                speak("switching to default mode...")
                pyautogui.hotkey('winleft', 'shift', 'tab')

            else:
                speak("unable to recognize")
                return

if __name__ == '__main__':
    wish()
    widget = Widget()
