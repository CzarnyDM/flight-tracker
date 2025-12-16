

from discordwebhook import Discord

DISCORD_URL = "https://discordapp.com/api/webhooks/1450293001510326344/0CUDF63bAYDPWOF0_mPjiHN2Q5cAkUY5LWbrgZwaNEz9jT-YUyd_NZbqO2J3DLR0K7fE"


def send_notification(alert):
    discord = Discord(url=DISCORD_URL)
    discord.post(content=alert)


