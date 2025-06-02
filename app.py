from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'anime123'

def get_db():
    conn = sqlite3.connect('anime.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/login')
    query = request.args.get('q', '').strip()
    conn = get_db()
    if query:
        query_like = f'%{query}%'
        animes = conn.execute('''
            SELECT * FROM animes
            WHERE title LIKE ? OR genre LIKE ?
        ''', (query_like, query_like)).fetchall()
    else:
        animes = conn.execute('SELECT * FROM animes').fetchall()
    conn.close()
    return render_template('index.html', animes=animes)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Username already exists"
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect('/')
        else:
            return "Invalid login"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/add/<int:anime_id>/<string:status>')
def add_to_library(anime_id, status):
    if 'user_id' not in session:
        return redirect('/login')
    conn = get_db()
    conn.execute('''
        INSERT OR REPLACE INTO user_animes (user_id, anime_id, status)
        VALUES (?, ?, ?)
    ''', (session['user_id'], anime_id, status))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/library/<string:status>')
def library(status):
    if 'user_id' not in session:
        return redirect('/login')
    conn = get_db()
    animes = conn.execute('''
        SELECT a.* FROM animes a
        JOIN user_animes ua ON a.id = ua.anime_id
        WHERE ua.user_id = ? AND ua.status = ?
    ''', (session['user_id'], status)).fetchall()
    conn.close()
    return render_template('library.html', animes=animes, status=status)

if __name__ == '__main__':
    app.run(debug=True)