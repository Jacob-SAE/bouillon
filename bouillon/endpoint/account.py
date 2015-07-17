import bouillon
from bouillon import Server
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

@bouillon.Server.route('/')
def index():
    return render_template('home.html')

@bouillon.Server.route('/layout')
def home():
    return render_template('layout.html')
