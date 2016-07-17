#!/bin/env python
from app import create_app, socketio
import os


app = create_app(debug=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, port=port)
