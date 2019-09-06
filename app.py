from flask import Flask, jsonify, request
from flask_socketio import SocketIO

users = [
	{
		"id" : 2,
		"name": "Anne",
		"age" : 23
	},
	{
		"id" : 3,
		"name": "Bill",
		"age" : 21
	},
	{
		"id" : 1,
		"name": "Cathy",
		"age" : 22
	}
]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	return app.send_static_file('index.html')


@socketio.on('msg')
def handleMsg(data):
	socketio.emit('push', data, broadcast = True, include_self = False)
	

@app.route('/users')

def getUsers():
	return jsonify(users)


@app.route('/users/<id>')


def getUser(id):
	user = [u for u in users if str(u['id'])==id]
	return jsonify(user)


# /users/sort?field=id
@app.route('/users/sort')

def getUsersSorted():
	field = request.args.get('field')
	usersSorted = sorted(users, key=lambda u: u[field])
	return jsonify(usersSorted)

if __name__ == "__main__":
	socketio.run(app)

















































# from flask import Flask, jsonify, request

# users = [
# 	{
# 		"id" : 2,
# 		"name": "Anne",
# 		"age" : 23
# 	},
# 	{
# 		"id" : 3,
# 		"name": "Bill",
# 		"age" : 21
# 	},
# 	{
# 		"id" : 1,
# 		"name": "Cathy",
# 		"age" : 22
# 	}
# ]


# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return app.send_static_file('index.html')

# @app.route('/users')

# def getUsers():
# 	return jsonify(users)


# @app.route('/users/<id>')


# def getUser(id):
# 	user = [u for u in users if str(u['id'])==id]
# 	return jsonify(user)


# # /users/sort?field=id
# @app.route('/users/sort')

# def getUsersSorted():
# 	field = request.args.get('field')
# 	usersSorted = sorted(users, key=lambda u: u[field])
# 	return jsonify(usersSorted)

# if __name__ == "__main__":
# 	app.run(debug = True)