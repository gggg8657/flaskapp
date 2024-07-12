from flask import Flask, render_template, request, redirect, url_for
import random
import requests
import re
import socket

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 컴퓨터 이름, ip
hostname = socket.gethostname()
hostip = socket.gethostbyname(socket.gethostname())

# 외부 IP, 아래 사이트 호출 후 결과에서 추출
req = requests.get("http://ipconfig.kr")
out_ip = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

@app.route('/network_info')
def network_info():
    return ('컴퓨터 이름 : {0}<br>내부 IP : {1}<br>외부 IP : {2}<br><br>당신의 IP : {3}<br><br>Hello'
            .format(hostname, hostip, out_ip, request.remote_addr))

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