import pyttsx3
import time
from plyer import notification
def speak(n):
    engine = pyttsx3.init()
    engine.say(n)
    engine.runAndWait()
if __name__ == '__main__':
 while True:
     speak("please drink water")
     notification.notify(
            title = "Please Drink Water Now!!",
            message ="Drink water please for your good health",
            timeout= 12
            )
     time.sleep(60*60)
     speak("please do some physical exersice")
     notification.notify(
         title="Please do some physical exersice",
         message="please get up and do some physical activity",
         timeout=12
     )
     time.sleep(60*63)
     speak("please do some eyes exersice")
     notification.notify(
         title="Please do some eyes exersice",
         message="please close your eyes for at least 10 to 15 second and ",
         timeout=12
     )
     time.sleep(60*65)
