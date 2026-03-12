from flask import Flask, render_template

# Lab 12- Robert Schleicher
# Flask needs to know the name of this file to find templates and static files
app = Flask(__name__)

# ============================================================
#  ROUTE 1 — Home page
#  Visit: http://YOUR_IP:8080/
# ============================================================
@app.route('/')
def home():
    # render_template loads templates/home.html and sends it to the browser
    return render_template('home.html', page_title="My Flask Site")
#Testing

# ============================================================
#  ROUTE 2 — Hello page with a URL variable
#  Visit: http://YOUR_IP:8080/hello/YourName/
#  Anything you put after /hello/ becomes the `name` variable
# ============================================================
@app.route('/hello/<name>/')
def hello(name):
    return render_template('hello.html', name=name)


# ============================================================
#  YOUR ROUTES GO BELOW THIS LINE
#  Each exercise asks you to add a new @app.route here
# ============================================================
#exercise s

@app.route('/analyze/<word>')
def analyze(word):

    # Exercise 1
    num_chars = len(word)

    # Exercise 2
    num_vowels = 0
    for letter in word.lower():
        if letter in "aeiou":
            num_vowels += 1

    return render_template('analyze.html',
                           word=word,
                           num_chars=num_chars,
                           num_vowels=num_vowels)


# ============================================================
#  These two lines always stay at the bottom of the file.
#  host='0.0.0.0' means "listen on all network interfaces"
#  so the server is reachable from outside EC2, not just locally
# ============================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
