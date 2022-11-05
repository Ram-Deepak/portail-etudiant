from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
  return "hi"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))
  