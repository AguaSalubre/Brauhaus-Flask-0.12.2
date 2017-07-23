from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('brauhaus.html')

@app.route('/gaststaette')
def gaststaette():
    return render_template('gaststaette.html')

@app.route('/veranstaltungen')
def veranstaltungen():
    return render_template('veranstaltungen.html')

@app.route('/stammtische')
def stammtische():
    return render_template('stammtische.html')

@app.route('/mediathek')
def mediathek():
    return render_template('mediathek.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True)
