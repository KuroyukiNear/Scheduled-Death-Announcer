import discord
import json
from pathlib import Path
import asyncio

# Load message
msg_path = Path(__file__).parent / "message.txt"
with msg_path.open("r", encoding="utf-8") as msgfile:
    msg = msgfile.read()

# Load config
config_path = Path(__file__).parent / "config.json"
with config_path.open("r", encoding="utf-8") as configfile:
    config = json.load(configfile)

channel_id = config["settings"]["announcement_channel"]
message_sent_status = config["settings"]["status"]
bot_token = config["settings"]["bot_token"]
countdown_time = config["settings"]["countdown_time"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    channel = client.get_channel(channel_id)

    if channel is None:
        print("Channel not found.")
        await client.close()
        return

    while True:
        if message_sent_status:
            print("Status is True. Exiting.")
            await client.close()
            return

        print(f"Waiting {countdown_time} seconds...")
        await asyncio.sleep(countdown_time)

        print("Sending message...")
        await channel.send(msg)

        # Update status
        config["settings"]["status"] = True

        with config_path.open("w", encoding="utf-8") as configfile:
            json.dump(config, configfile, indent=4)

        print("Status updated to True.")
        await client.close()
        exit("Message sent. Exiting.")


client.run(bot_token)