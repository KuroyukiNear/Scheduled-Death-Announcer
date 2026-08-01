import discord
import asyncio

import json
from pathlib import Path

import os
from colorama import Fore, Back, Style
from datetime import datetime, timezone

# Tested on Python 3.14.2 and discord.py 2.7.1

# Load message
msg_path = Path(__file__).parent / "message.txt"
with msg_path.open("r", encoding="utf-8") as msgfile:
    msg = msgfile.read()

# Load config
config_path = Path(__file__).parent / "config.json"
with config_path.open("r", encoding="utf-8") as configfile:
    config = json.load(configfile)

channel_id = config["settings"]["announcement_channel"]
message_sent_status = config["settings"]["message_sent_status"]
bot_token = config["settings"]["bot_token"]
countdown_time = config["settings"]["countdown_time"]
exit_or_not = config["settings"]["exit_after_announcement"]

# Discord client setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # Get the announcement channels
    channel_list = [client.get_channel(cid) for cid in channel_id]
    channel = next((ch for ch in channel_list if ch is not None), None)

    # If no valid channel is found, print an error and exit
    if channel is None:
        print("Channel not found.")
        await client.close()
        return

    # Start the countdown and announcement process
    while True:
        if message_sent_status: # Check if the message has already been sent
            print("Status is True. Exiting.")
            await client.close()
            return

        # Print the configs
        print(
            f"{Fore.RED + Style.BRIGHT} Config File: {config_path}\n",
            f"Announcement Channel IDs: {channel_id}\n",
            f"Countdown Time: {countdown_time} seconds\n",
            f"Exit After Announcement: {exit_or_not}"
        )

        # Countdown before sending the message
        for remaining in range(countdown_time, 0, -1):
            print(f"{Fore.CYAN} \rWaiting... {remaining} seconds remaining", end="", flush=True)
            await asyncio.sleep(1)

        # send the message to all channels
        print(Fore.MAGENTA)
        print("\nSending message...")
        for cid in channel_id:
            channel = client.get_channel(cid)
            if channel is not None:
                await channel.send(msg)
                print(f"Message sent to #{channel.name}, ID: {channel.id}")

        # Update status and log the time of sending
        sent_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        config["settings"]["message_sent_status"] = True
        config["settings"]["sent_on"] = sent_time

        with config_path.open("w", encoding="utf-8") as configfile:
            json.dump(config, configfile, indent=4)

        print("Sent status updated to True.")
        print(f"{Fore.GREEN}Message sent on: {sent_time}")

        await client.close() # Close the Discord client after sending the message

        if exit_or_not: # Exit after sending the message if the config is set to True
            exit("Exiting.")
        else:
            print("Announcement completed.")
            message_sent_status == True # Update the local variable to prevent re-sending
            os.system("pause >nul")
            exit()


client.run(bot_token)