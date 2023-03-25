from flask import Flask, request, send_file, redirect, url_for
import yt_dlp
import os

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

app.run(host='0.0.0.0', port=8000)