from flask import Flask, render_template, request, redirect, url_for,
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app= flask(__name__)

@app.route('/todo')
def todo():
    return render_template('todo.html')




if __name__ == '__main__':
    app.run(debug=True)