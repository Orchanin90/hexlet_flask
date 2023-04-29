from flask import (Flask, json, redirect, render_template, request,
                   make_response, url_for)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    return render_template('cookies_for_cart.html', cart=cart)


@app.post('/cart-items')
def add_items():
    name = request.form.get('item_name', '')
    count = request.form.get('item_id', 0)

    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    if count and name:
        cart[name] = cart.get(name, 0) + int(count)

    encoded_сart = json.dumps(cart)

    response = redirect(url_for('index'))
    response.set_cookie('cart', encoded_сart)
    return response


@app.post('/cart-items/clean')
def clean_cookies():
    resp = redirect((url_for('index')))
    resp.delete_cookie('cart')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
