from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this key is a secret'
DATABASE = 'users_cr'
