from flask import Flask
from flask import request
import sqlite3


app = Flask(__name__)


@app.route('/shop/items/<item_id>', methods=['GET'])
def item_info(item_id):
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM items where id ={item_id}')
        item = cursor.fetchone()
        my_db.close()
        return str(item)
    else:
        pass


@app.route('/shop/items/<item_id>/review', methods=['GET', 'POST'])
def item_review(item_id):
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM feedbacks where item_id ={item_id}')
        feedbacks = cursor.fetchall()
        my_db.close()
        return str(feedbacks)
    elif request.method == 'POST':
        pass


@app.route('/shop/items/<item_id>/review/<review_id>', methods=['GET', 'PUT'])
def review_info(item_id, review_id):
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM feedbacks where item_id ={item_id} and feedback_id ={review_id}')
        feedback = cursor.fetchone()
        my_db.close()
        return str(feedback)
    elif request.method == 'PUT':
        pass


@app.route('/shop/items', methods=['GET'])
def all_items():
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM items')
        items = cursor.fetchall()
        my_db.close()
        return str(items)
    else:
        pass


@app.route('/shop/cart/<cart_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def cart(cart_id):
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM cart where cart_id ={cart_id}')
        cart = cursor.fetchall()
        my_db.close()
        return str(cart)
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/shop/favorites/<list_id>', methods=['GET', 'PUT'])
def favorite(list_id):
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM wishlist where list_id ={list_id}')
        wishlist = cursor.fetchone()
        my_db.close()
        return str(wishlist)
    elif request.method == 'PUT':
        pass


@app.route('/shop/waitlist/<list_id>', methods=['GET', 'PUT'])
def wailtist(list_id):
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM waitlist where list_id ={list_id}')
        waitlist = cursor.fetchone()
        my_db.close()
        return str(waitlist)
    elif request.method == 'PUT':
        pass


@app.route('/admin/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM items')
        items = cursor.fetchall()
        my_db.close()
        return str(items)
    elif request.method == 'POST':
       pass


@app.route('/admin/items/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def item(item_id):
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM items where id ={item_id}')
        item = cursor.fetchone()
        my_db.close()
        return str(item)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/admin/orders', methods=['GET'])
def orders():
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM orders')
        orders = cursor.fetchall()
        my_db.close()
        return str(orders)
    else:
        pass


@app.route('/shop/compare/<cmp_id>', methods=['GET', 'PUT'])
def compare(cmp_id):
    if request.method == 'GET':
        my_db = sqlite3.connect('identifier.sqlite')
        cursor = my_db.cursor()
        cursor.execute(f'SELECT * FROM compare where compare_id ={cmp_id}')
        cmp_list = cursor.fetchone()
        my_db.close()
        return str(cmp_list)
    elif request.method == 'PUT':
        pass


app.run()
