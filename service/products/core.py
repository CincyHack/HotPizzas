#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import redis

from flask import Flask, Response, request, redirect, jsonify

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=tmpl_dir)

@app.route('/products', methods=('POST'))
def view_products():
	return jsonify({
		[{
			"id": "21958c92-40c8-4ca9-b734-c8bb6b951f8d",
			"price": 10.00,
			"price_units": "USD",
			"estimated_time": 10,
			"time_units": "min",
			"product_type": "pizza",
			"product_configs": ["large", "pepperoni"]
		},{
			"id": "93b67a7c-a554-459a-b54a-4808dd466395",
			"price": 10.00,
			"price_units": "USD",
			"estimated_time": 7,
			"time_units": "min",
			"product_type": "pizza",
			"product_configs": ["large", "cheese"]
		},{
			"id": "bcfa592c-7df3-46fc-ab18-a81710960110",
			"price": 15.00,
			"price_units": "USD",
			"estimated_time": 10,
			"time_units": "min",
			"product_type": "pizza",
			"product_configs": ["large", "pepperoni"]
		}]
	})


@app.route('/products/unique', methods('POST'))
def view_unique_products():
	return jsonify({
		[{
			"id": "large-cheese",
			"price": 10.00,
			"price_units": "USD",
			"estimated_time": 15,
			"time_units": "min",
			"product_type": "pizza",
			"product_configs": ["large", "cheese"]
		},{
			"id": "large-pepperoni",
			"price": 15.00,
			"price_units": "USD",
			"estimated_time": 15,
			"time_units": "min",
			"product_type": "pizza",
			"product_configs": ["large", "pepperoni"]
		}]
	})

