console.log(3+1)

var socket = io();
//     socket.on('connect', function() {
//         socket.emit('my event', {data: 'I\'m connected!'});
// });

function send() {
	var inputBox = document.getElementById('inputBox')
	socket.emit('msg', inputBox.value)
	inputBox.value = ''
}


socket.on('push', function(data){
	var chatBox = document.getElementById('chatBox')
	//console.log(data)
	chatBox.innerHTML += "<p>"+data+"</p"
})
	


function getUsers() {
	fetch('/users').then(function(res){
		res.json().then(function(data){
			console.log(data)
		})
	})
}