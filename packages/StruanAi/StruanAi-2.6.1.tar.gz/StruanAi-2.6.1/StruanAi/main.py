import JarvisAI as StruanAi
import time
import webbrowser as web
import re as struan
from pyjokes import get_joke
import pyautogui

obj = StruanAi.JarvisAssistant()

def StruanSpeek(Text_To_Speek):
    obj.text2speech(Text_To_Speek)

def StruanSpeekAndPrint(Text_To_Speek_An_Print):
    StruanSpeek(Text_To_Speek_An_Print)
    print(Text_To_Speek_An_Print)

def StruanLissen():
    StruanLissen.Lissener = obj.mic_input()

def StruanTellMeAbout(Topic_to_Tell_You):
    StruanTellMeAbout.Topic = obj.tell_me(topic=Topic_to_Tell_You)

def StruanTime():
    StruanTime.Time = obj.tell_me_time()

def StruanDate():
    StruanDate.Date = obj.tell_me_date()

def StruanWeather(City):
    StruanWeather.CityWeather = obj.weather(city=City)

def StruanNews():
    StruanNews.News = obj.news()

def StruanWeb(Link_To_The_Site_To_Open):
    web.open(Link_To_The_Site_To_Open)

def StruanWebNewTab(Link_To_The_Site_To_Open):
    web.open_new_tab(Link_To_The_Site_To_Open)

def StruanJoke():
    StruanJoke.Joke = get_joke('en', 'neutral')

def StruanSpam(Word_To_Spam, Times_To_Spam, Website_To_Spam_Url):
    StruanWeb(Website_To_Spam_Url)
    Times_To_Spam = int(Times_To_Spam)
    Word_To_Spam = str(Word_To_Spam)
    for i in range(Times_To_Spam):
        pyautogui.typewrite(Word_To_Spam)