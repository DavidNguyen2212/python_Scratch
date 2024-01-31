# Cài đặt thư viện text to speech: pip3 install pyttsx3, pip3 install pywin32
import pyttsx3

friday = pyttsx3.init()
voice = friday.getProperty('voices')    # getProperty: lấy giọng
friday.setProperty('voice', voice[1].id)  # set để cài đặt. voice[1] là giọng nam, voice[0] là nữ

def speak(audio):
    print('F.R.I.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()     # không có phương thức này sẽ không có tiếng nói
# speak("Hello Youtube")

import datetime
def time():
    Time = datetime.datetime.now().strftime("%I : %M : %p") #I: giờ, M: phút, p: am/pm
    speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Good night Sir")
    speak("How can I help you, Sir?")

# Cài đặt thư viện speech to text, SpeechRecognition (import speech_recognition!!!) và pyaudio
import speech_recognition as sr
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='en-US')
        print("Tony Lèo: "+query)
    except sr.UnknownValueError:
        print('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Your order is: '))
    return query
    
import webbrowser as wb 
import os
# Từ python 3.12 distutils bị loại bỏ 
# chạy python3.12 -m pip install --upgrade setuptools để hỗ trợ lại pyaudio cùng disutils
if __name__ == "__main__":
    welcome()

    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search for, boss?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Google!")

        elif "youtube" in query:
            speak("What should I search for, boss?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Youtube!")

        elif "open video" in query:
            meme = r"C:\Users\DELL\Downloads\Hướng Dẫn Lập Trình 6 Dự Án Python Cơ Bản Trong 1 Video Duy Nhất.mp4"
            os.startfile(meme)
        
        elif "time" in query:
            time()

        elif "quit" in query:
            speak("Friday is cooking, sir. Bye boss!")
            quit()