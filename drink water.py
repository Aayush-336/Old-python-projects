import time
from plyer import notification
count=0
if __name__=="__main__":
    while True:
        notification.notify(
            title="Drink water now!!",
            message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = "D:\Aayush Download\icon.ico",
            timeout=10


        )
        break