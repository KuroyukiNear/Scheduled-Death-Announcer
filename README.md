# Scheduled Death Announcer
`2026-07-08`

*Last Updated:* `2026-08-01`

## How do I use this?
### Configuration
Before using it, you have to edit the `config.json` file.
```json
{
    "settings": {
        "announcement_channel": [1, 2, 3],
        "message_sent_status": false,
        "bot_token": "TOKEN",
        "countdown_time": 300,
        "exit_after_announcement": false,
        "sent_on": ""
    }
}
```
`"announcement_channel"` will be the ID of the channels you want to send the message in.

`"message_sent_status"` determines whether the message has been sent, to avoid repeated messages. It should be set to `false` before using.

`"bot_token"` will be the token of your Discord bot.

`"countdown_time"` will be the time before it sents the message. The time will be in seconds.

`"exit_after_announcement"` determines if the console will be closed after the announcement.

`"sent_on"` logs the time the announcement was sent.

Edit the contents in `message.txt` to the message you want to be sent to the Discord channel.

### Setup
To start using the script, create a shortcut of the `run.bat` file and move it to your startup folder.

Note: Do remember to exit the program everytime your computer is started to avoid it from sending.