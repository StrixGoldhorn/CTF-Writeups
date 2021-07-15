from flask import Flask, render_template, request, make_response
import os

flag = open("flag.txt", "r").read()
app = Flask('app')

items = {"bagel": 50, "toasted_bagel": 70, "bread": 30, "toast": 50, "wheat": 20, "water": 10}

@app.route('/')
def index():
  resp = make_response(render_template('index.html'))
  resp.set_cookie('item', 'gone', max_age=0)
  resp.set_cookie('money', 'gone', max_age=0)
  return resp

@app.route('/shop')
def shop():
  buy = request.args.get("buy")
  money = request.args.get("money")
  if(buy == None and money == None):
    return render_template("shop.html")
  else:
    try:
      item_price = items[buy]
      try:
        if(item_price > int(money)):
          resp = make_response("You don't have enough money to buy this item!")
          if(buy):
            resp.set_cookie('item', buy, max_age = 10)
          if(money):
            resp.set_cookie('money', money, max_age= 10)
          return resp
        else:
          resp = make_response(f"Congratulations! You are now the owner of {buy}. You have {int(money) - item_price} fake coins left, which means absolutely nothing!")
          if(buy):
            resp.set_cookie('item', buy)
          if(money):
            resp.set_cookie('money', money)
          return resp
      except ValueError:
        return "Please enter a valid money amount!"
    except KeyError:
      return "Not a valid item! Please enter a valid item."

@app.errorhandler(404)
def not_found(e):
  return render_template('404.html', message="Page not found"), 404

@app.errorhandler(500)
def error(e):
  if(request.cookies.get('item') == request.cookies.get('money') and request.cookies.get('add') == "1"):
    return render_template('500.html', message="Internal Server Error", flag=flag), 500
  else:
    return render_template('500.html', message="Internal Server Error.", flag=os.getenv("FLAG")), 500
  
app.run(host='0.0.0.0', port=8080)