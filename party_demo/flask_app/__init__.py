from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'no secrets on github'
DATABASE = 'sept_party'
