from flask import Flask, render_template, Response, request

app = Flask(__name__)
frame_r = 0

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)