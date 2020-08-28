from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def namex(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)