import pyttsx4
import pypdf
import os

os.chdir(r"C:\Users\DELL\Documents\Python3\Six_Project")
sach = open("Concepts of Programming Languages.pdf", "rb")   # read binary
pdfReader = pypdf.PdfReader(sach)
pages = len(pdfReader.pages)
print(pages)

bot = pyttsx4.init()
voices = bot.getProperty('voices')
bot.setProperty('rate', 80)
bot.setProperty('voice', voices[1].id)
for num in range(7, pages):   
    page = pdfReader._get_page(num)
    text = page.extract_text()
    bot.say(text)
    bot.runAndWait()


