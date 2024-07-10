from flask import Flask, render_template_string, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template_string('''
        <html>
            <head>
                <title>Home</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    nav { margin-bottom: 20px; }
                    nav a { margin-right: 10px; text-decoration: none; color: blue; }
                </style>
            </head>
            <body>
                <nav>
                    <a href="/">Home</a>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                    <a href="/game">Game</a>
                </nav>
                <h1>Welcome to the Home Page</h1>
                <p>Hello WebApp.</p>
            </body>
        </html>
    ''')

@app.route('/about')
def about():
    return render_template_string('''
        <html>
            <head>
                <title>About</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    nav { margin-bottom: 20px; }
                    nav a { margin-right: 10px; text-decoration: none; color: blue; }
                </style>
            </head>
            <body>
                <nav>
                    <a href="/">Home</a>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                    <a href="/game">Game</a>
                </nav>
                <h1>About Us</h1>
                <p>This is DongJu's Pilot flask web.</p>
            </body>
        </html>
    ''')

@app.route('/contact')
def contact():
    return render_template_string('''
        <html>
            <head>
                <title>Contact</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    nav { margin-bottom: 20px; }
                    nav a { margin-right: 10px; text-decoration: none; color: blue; }
                </style>
            </head>
            <body>
                <nav>
                    <a href="/">Home</a>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                    <a href="/game">Game</a>
                </nav>
                <h1>Contact Us</h1>
                <p>email: 010.2757.8506 information goes here.</p>
            </body>
        </html>
    ''')

# @app.route('/game', methods=['GET', 'POST'])
# def game():
#     if 'number' not in session:
#         session['number'] = random.randint(1, 100)
#         session['attempts'] = 0

#     message = ''
#     if request.method == 'POST':
#         guess = int(request.form['guess'])
#         session['attempts'] += 1
#         if guess < session['number']:
#             message = 'Higher! Try again.'
#         elif guess > session['number']:
#             message = 'Lower! Try again.'
#         else:
#             message = f'Congratulations! You guessed it in {session['attempts']} attempts.'
#             session.pop('number')
#             session.pop('attempts')

#     return render_template_string('''
#         <html>
#             <head>
#                 <title>Guess the Number Game</title>
#                 <style>
#                     body { font-family: Arial, sans-serif; margin: 40px; }
#                     nav { margin-bottom: 20px; }
#                     nav a { margin-right: 10px; text-decoration: none; color: blue; }
#                 </style>
#             </head>
#             <body>
#                 <nav>
#                     <a href="/">Home</a>
#                     <a href="/about">About</a>
#                     <a href="/contact">Contact</a>
#                     <a href="/game">Game</a>
#                 </nav>
#                 <h1>Guess the Number Game</h1>
#                 <form method="post">
#                     <label for="guess">Enter your guess (1-100):</label>
#                     <input type="number" id="guess" name="guess" min="1" max="100" required>
#                     <button type="submit">Guess</button>
#                 </form>
#                 <p>{{ message }}</p>
#             </body>
#         </html>
#     ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)