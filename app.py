from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # 여기에 이메일 전송 로직을 추가할 수 있습니다.
        message = 'Thank you for your message!'
    return render_template('contact.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)