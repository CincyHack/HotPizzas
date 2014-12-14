#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import redis

from flask import Flask, Response, request, redirect, jsonify

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=tmpl_dir)

@app.route('/orders', methods=('POST'))
def view_orders():
	pass
