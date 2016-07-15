from flask import session
from flask.ext.socketio import emit, join_room, leave_room
from .. import socketio
from bot import Bot


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)
    if int(room) % 10 == 0:
        b = Bot()
        # Greet user
        emit('status', {'msg': b.name() + ' [BOT] has entered the room.'}, room=room)
        emit('message', {'msg':  b.name() + ': ' + b.greet()}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ': ' + message['msg']}, room=room)
    if int(room) % 10 == 0:
        b = Bot()
        # Talk to user
        emit('message', {'msg': b.name() + ': ' + b.respond(message['msg'])}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

