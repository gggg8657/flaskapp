from flask import Flask, render_template_string, request, session
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
                    <a href="/tictactoe">TicTacToe</a>
                    <a href="/flappybird">FlappyBird</a>
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
                <p> 💌 email:  gggg8657@gmail.com</p>
                <p> 📞 phone: 010-2757-8506 </p>
            </body>
        </html>
    ''')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    message = ''
    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1
        if guess < session['number']:
            message = 'Higher! Try again.'
        elif guess > session['number']:
            message = 'Lower! Try again.'
        else:
            message = f'Congratulations! You guessed it in {session["attempts"]} attempts.'
            session.pop('number')
            session.pop('attempts')

    return render_template_string('''
        <html>
            <head>
                <title>Guess the Number Game</title>
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
                <h1>Guess the Number Game</h1>
                <form method="post">
                    <label for="guess">Enter your guess (1-100):</label>
                    <input type="number" id="guess" name="guess" min="1" max="100" required>
                    <button type="submit">Guess</button>
                </form>
                <p>{{ message }}</p>
            </body>
        </html>
    ''', message=message)

# 틱택토 게임 상태 초기화
@app.route('/reset_tictactoe')
def reset_tictactoe():
    session['board'] = [['' for _ in range(3)] for _ in range(3)]
    session['player'] = 'X'
    session['winner'] = None
    return redirect(url_for('tictactoe_game'))

@app.route('/tictactoe', methods=['GET', 'POST'])
def tictactoe_game():
    if 'board' not in session:
        session['board'] = [['' for _ in range(3)] for _ in range(3)]
        session['player'] = 'X'
        session['winner'] = None

    board = session['board']
    player = session['player']
    winner = session['winner']

    if request.method == 'POST' and not winner:
        row, col = int(request.form.get('row')), int(request.form.get('col'))
        if board[row][col] == '':
            board[row][col] = player
            winner = check_winner(board)
            session['winner'] = winner
            if not winner:
                player = 'O' if player == 'X' else 'X'
                session['player'] = player

    return render_template_string('''
        <html>
            <body>
                <h1>틱택토</h1>
                <table border="1">
                    {% for row in range(3) %}
                        <tr>
                            {% for col in range(3) %}
                                <td style="width: 50px; height: 50px; text-align: center; vertical-align: middle;">
                                    {% if session['board'][row][col] == '' and not session['winner'] %}
                                        <form method="post" style="display:inline;">
                                            <input type="hidden" name="row" value="{{ row }}">
                                            <input type="hidden" name="col" value="{{ col }}">
                                            <button type="submit" style="width: 100%; height: 100%;"></button>
                                        </form>
                                    {% else %}
                                        {{ session['board'][row][col] }}
                                    {% endif %}
                                </td>
                            {% endfor %}
                        </tr>
                    {% endfor %}
                </table>
                {% if session['winner'] %}
                    <p>승자: {{ session['winner'] }}</p>
                    <a href="/reset_tictactoe">다시하기</a>
                {% endif %}
            </body>
        </html>
    ''')

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    if all(all(cell != '' for cell in row) for row in board):
        return 'Tie'
    return None

@app.route('/flappybird', methods=['GET', 'POST'])
def flappybird_game():
    if 'bird_position' not in session:
        session['bird_position'] = 250
    gravity = 5
    jump_strength = 50

    if request.method == 'POST':
        session['bird_position'] -= jump_strength

    session['bird_position'] += gravity
    session['bird_position'] = min(max(session['bird_position'], 0), 480)  # Keep bird within screen bounds

    return render_template_string('''
        <html>
            <body>
                <h1>플래피 버드 클론</h1>
                <div style="position:relative; width:400px; height:500px; border:1px solid black;">
                    <div style="position:absolute; top:{{ bird_position }}px; left:50px; width:20px; height:20px; background-color:blue;"></div>
                </div>
                <form method="post">
                    <button type="submit">점프</button>
                </form>
                <a href="/flappybird">다시하기</a>
            </body>
        </html>
    ''', bird_position=session['bird_position'])

if __name__ == '__main__':
    app.run(debug=True)