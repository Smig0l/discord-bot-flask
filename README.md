# README

This is the [Flask](http://flask.pocoo.org/) [quick start](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application) example for [Render](https://render.com).

The app in this repo is deployed at [https://flask.onrender.com](https://flask.onrender.com).

## Deployment

Follow the guide at https://render.com/docs/deploy-flask.

## useful info:

[yt-dlp-guide](https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp)

`pip install -r requirements.txt`

add `export PATH=$PATH:/home/youruser/.local/bin` to `~/.bashrc` , save and `source ~/.bashrc`

run with: `gunicorn app:app`
