from time import struct_time
import pyttsx3
import datetime
import speech_recognition as sr
import  pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices)
# print(voices[2].id) #zira coming
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): 
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening!")

    speak("i am Smarty Sir. please tell me, how may help you")

def takeCommand():
    # takes microfon input from user and returns string output 
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.energy_threshold = 100
        r.pause_threshold = 0.8
        audio= r.listen(source)
    try:
        print("Recognizing.....")
        query= r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")
   
    except Exception as e:
        print(e)

        print("Sorry say that Again!")
        return "None"
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("tilvadhruv8@gmail.com","frnknipbhyszedeg")
    server.sendmail("tilvadhruv8@gmail.com",to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query=takeCommand().lower()
    # logic for executing task based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            # print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'who are you' in query:
            speak("i am Smarty Sir and i am your assistant, ask me anything you want!, and  i am created by Dhruv Tilva")


        elif 'play music' in query:
            music_dir= 'D:\\songs'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"sir,the time is {strTime}")
       
        elif 'open code' or 'vs studio' or 'vs code' in query:
            codePath= ("C:\\Users\\Dhruv Tilva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            os.startfile(codePath)
        
        elif 'send email to' in query:
            try:
                speak("what should i say?")
                content= takeCommand()
                to= "card.managment.helpdesk@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("sorry i am not able to sent email at this moment try again later!")
                






 