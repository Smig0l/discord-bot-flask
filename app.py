from flask import Flask, request, send_file
import yt_dlp
import os
from dotenv import load_dotenv

load_dotenv()


from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>utilizzo: /api/download?q={youtubeurl} </p>"

@app.route('/api/download')
def download():
    url = request.args.get('q')
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info_dict)

    filename, ext = os.path.splitext(filename)
    filename = f"{filename}.mp3"

    response = send_file(filename, as_attachment=True)
    response.direct_passthrough = False  # Prevents flask from closing the file descriptor before we delete the file
    os.remove(filename)
    return response 

def start_flask_app():
    app.run(host='0.0.0.0', port=8000)

flask_thread = Thread(target=start_flask_app)
flask_thread.start()

# This example requires the 'message_content' privileged intent to function.
yt_dlp.utils.bug_reports_message = lambda: ''
import asyncio
import discord
from discord.ext import commands
description = '''somedescription.'''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(os.getenv("DISCORD_TOKEN"))
