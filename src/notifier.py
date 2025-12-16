

from discordwebhook import Discord
import requests


DISCORD_URL = "https://discordapp.com/api/webhooks/1450293001510326344/0CUDF63bAYDPWOF0_mPjiHN2Q5cAkUY5LWbrgZwaNEz9jT-YUyd_NZbqO2J3DLR0K7fE"
TOKEN = "acdq1x3cy1u4gkvckqxoe89j1g6v7k"
USER_KEY = "u2i3tny2nc7deaktnr41ur5ier3d1k"

def send_notification(alert):
    discord = Discord(url=DISCORD_URL)
    discord.post(content=alert)


    r = requests.post("https://api.pushover.net/1/messages.json", data = {
    "token": TOKEN,
    "user": USER_KEY,
    "message": alert
    }
    # files = {
    # "attachment": ("image.jpg", open("your_image.jpg", "rb"), "image/jpeg")
    # }
    )
