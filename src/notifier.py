
import requests

TOKEN = "acdq1x3cy1u4gkvckqxoe89j1g6v7k"
USER_KEY = "u2i3tny2nc7deaktnr41ur5ier3d1k"

def send_notification(alert):

    r = requests.post("https://api.pushover.net/1/messages.json", data = {
    "token": TOKEN,
    "user": USER_KEY,
    "message": alert,
    },
     files = {
     "attachment": (f"./airline_logo.jpg", open(f"./airline_logo.jpg", "rb"), "image/jpeg")
     }
    )

