# Scheduled Death Announcer
`2026-07-08`

## How do I use this?
### Configuration
Before using it, you have to edit the `config.json` file.
```
{
    "settings": {
        "announcement_channel": 0,
        "status": false,
        "bot_token": "TOKEN",
        "countdown_time": 300
    }
}
```
`"announcement_channel"` will be the ID of the channel you want to send the message in.

`"status"` determines whether the message has been sent, to avoid repeated messages. It should be set to `false` before using.

`"bot_token"` will be the token of your Discord bot.

`"countdown_time"` will be the time before it sents the message. The time will be in seconds.

Edit the contents in `message.txt` to the message you want to be sent to the Discord channel.

### Setup
To start using the script, create a shortcut of the `scheduled_death_announcer.py` file into your startup folder.

Note: Do remember to exit the program everytime your computer is started to avoid it from sending.