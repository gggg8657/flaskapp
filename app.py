from flask import Flask, render_template_string

app = Flask(__name__)

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
                </nav>
                <h1>Welcome to the Home Page</h1>
                <p>Hello Flask.</p>
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
                </nav>
                <h1>About Us</h1>
                <p>Information about the website or company.</p>
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
                </nav>
                <h1>Contact Us</h1>
                <p>Contact information goes here.</p>
            </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)