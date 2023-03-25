from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

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

    return send_file(filename, as_attachment=True)