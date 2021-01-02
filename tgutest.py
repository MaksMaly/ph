
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import functions
from pyrogram.types import ChatPermissions
 
import time, requests, json
from time import sleep
import random
 
app = Client("my_account")

@app.on_message(filters.command("test", prefixes="."))
def test(app, msg):
    msg.edit_text("Работает!")

app.run()
