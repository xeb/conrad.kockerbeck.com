from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# Assuming your HTML files are in a directory named 'templates'
# and your videos are in a directory named 'videos'
app.template_folder = 'templates'
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html', title="Conrad's Birthday Celebration")

@app.route('/video/<name>')
def serve_video(name):
    # Construct the video URL
    video_src = f"/static/vids/{name}.avi"
    return render_template('player.html', video_src=video_src)

# @app.route('/videos/<path:filename>')
# def serve_video_file(filename):
#     return send_from_directory("vids", filename)

if __name__ == '__main__':
    app.run(debug=True, port=8007, host="0.0.0.0")