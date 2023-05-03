import os
from flask import Flask, request, render_template
import pytube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        youtube = pytube.YouTube(video_url)
        thumbnail_url = youtube.thumbnail_url
        thumbnail_file = os.path.join(app.static_folder, 'thumbnail.jpg')
        pytube.request.urlretrieve(thumbnail_url, thumbnail_file)
        return render_template('index.html', thumbnail_url='/static/thumbnail.jpg')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
