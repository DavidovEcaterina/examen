from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        connection = mysql.connector.connect(
            host='db',
            user='user',
            password='password',
            database='myapp_base'
        )
        return "Conexiune cu baza de date reușită!"
    except Exception as e:
        return f"Eroare la conectare: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
