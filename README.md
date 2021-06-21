# Backend developer position challenge

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone `https://github.com/donovan-vargas/softtek.git`
$ cd softek
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ make
```
Once `pip` has finished downloading the dependencies
activate virtualenv:

```sh
$ source p/bin/activate
```
run flask server softtek:

```sh
$ python softtek.py
```
send POST request on json body
```sh
{
  "orders": [
    {
      "order_number": "ORD_1567",
      "item_name": "LAPTOP",
      "status": "SHIPPED"
    },
    {
      "order_number": "ORD_1567",
      "item_name": "MOUSE",
      "status": "SHIPPED"
    },
    {
      "order_number": "ORD_1567",
      "item_name": "KEYBOARD",
      "status": "PENDING"
    },
    {
      "order_number": "ORD_1234",
      "item_name": "GAME",
      "status": "SHIPPED"
    },
    {
      "order_number": "ORD_1234",
      "item_name": "BOOK",
      "status": "CANCELLED"
    },
    {
      "order_number": "ORD_1234",
      "item_name": "BOOK",
      "status": "CANCELLED"
    },
    {
      "order_number": "ORD_9834",
      "item_name": "SHIRT",
      "status": "SHIPPED"
    },
    {
      "order_number": "ORD_9834",
      "item_name": "PANTS",
      "status": "CANCELLED"
    },
    {
      "order_number": "ORD_7654",
      "item_name": "TV",
      "status": "CANCELLED"
    },
    {
      "order_number": "ORD_7654",
      "item_name": "DVD",
      "status": "CANCELLED"
    }
  ]
}
```
to `http://127.0.0.1:5000/orders_status/`.

## Endpoints 
`http://127.0.0.1:5000/orders_status/` Process orders status and returns final status

## unittest
python -m unittest tests/order_status_test.py

