from flask import Flask, request, jsonify, render_template_string
from datetime import datetime
import os

app = Flask(__name__)

tasks = []
task_id_counter = 1

# Вставь сюда ВЕСЬ свой HTML код из index.html
HTML_CODE = """
<!DOCTYPE html>
... (весь твой html код сюда) ...
"""

@app.route('/')
def index():
    return render_template_string(HTML_CODE)

