import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, g
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

DATABASE = './'

@app.route("/")
def home():
    return "Hello, Flask!"