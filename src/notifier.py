import requests
import logging

TOKEN = "acdq1x3cy1u4gkvckqxoe89j1g6v7k"
USER_KEY = "u2i3tny2nc7deaktnr41ur5ier3d1k"

def send_notification(alert, islogo):
    print('*' * 100)
    print(f"Alert: {alert}")
    print(f"Alert type {type(alert)}")

    print(f"islogo: {islogo}")


    # if alert['logo'] is not None:
    #     logging.info(f"Sending notification with an image for {alert['number']}")
    #     r = requests.post("https://api.pushover.net/1/messages.json", data = {
    #     "token": TOKEN,
    #     "user": USER_KEY,
    #     "message": alert,
    #     },

    #     files = {
    #     "attachment": (f"./airline_logo.jpg", open(f"./airline_logo.jpg", "rb"), "image/jpeg")
    #     }
    # )
        

    # else:
    #     logging.info(f"Private airline or no logo found. Sending notification without an image for {alert['number']}")
    #     r = requests.post("https://api.pushover.net/1/messages.json", data = {
    #     "token": TOKEN,
    #     "user": USER_KEY,
    #     "message": alert,
    #     }
    # )

    