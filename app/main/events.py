from flask import session
from flask.ext.socketio import emit, join_room, leave_room
from .. import socketio
from bot import Bot
import uuid


bot_rooms = {"10":"eliza", "20": "sun", "30": "iesha", "40": "zen", "50": "rude", "60": "Copycat", "70": "deepqa"}  # These codes map to bots.
active_bots = {}


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    with_bot = False
    if room in bot_rooms.keys():
        with_bot = True
        # Store previous ID
        bot_room = room
        room = str(uuid.uuid4())  # Create private room
        session["room"] = room  # Update session
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)
    if with_bot:
        # Reverse name for CopyCat bot
        if bot_room == "60":
            bot_name = session.get('name')[::-1]
        # Keep instance of bot
        else:
            bot_name = bot_rooms[bot_room]
        b = Bot(bot_name)
        b.setup()
        active_bots[room] = b
        # Greet user
        emit('status', {'msg': b.name() + ' [BOT] has entered the room.'}, room=room)
        emit('message', {'msg':  b.name() + ': ' + b.greet()}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ': ' + message['msg']}, room=room)
    if room in active_bots.keys():
        b = active_bots[room]
        # Respond to user
        response = b.respond(message['msg'])
        response_delay = (len(response) / 5.0) * 100
        # Write the input
        emit('delay', {'msg': b.name() + ': ' + response, 'delay': response_delay}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    if room in active_bots.keys():
        active_bots[room] = None
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

