import json
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/orders_status/', methods=['POST'])
def orders_status():
    """Orders status process
    :param request; post request json
    :return orders_status: json
    """
    data = request.get_json()
    orders = data.get('orders')
    c = {}
    for order in orders:
        c.setdefault(order['order_number'], []).append(order['status'])
    orders_status = [{'order_number': k, 'order_status': v} for k, v in c.items()]    
    for x in orders_status:
        if 'PENDING' in x['order_status']:
            x['final_status'] = 'PENDING'
        elif 'SHIPPED' in x['order_status']:
            x['final_status'] = 'SHIPPED'
        else:
            x['final_status'] = 'CANCELLED'    
    return data, 200



if __name__ == '__main__':
    app.run()
