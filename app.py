from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/api/download')
def download():
    url = request.args.get('q')
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return send_file('audio.mp3', as_attachment=True)