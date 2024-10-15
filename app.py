from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # 主页面

@app.route('/map')
def map_page():
    return render_template('map.html')  # 地图页面

@app.route('/wallpaper')
def wallpaper_page():
    return render_template('wallpaper.html')  # 地图页面

@app.route('/avatar')
def avatar_page():
    return render_template('avatar.html')  # 地图页面

@app.route('/message')
def message_page():
    return render_template('message.html')  # 地图页面

if __name__ == '__main__':
    app.run(debug=True)
