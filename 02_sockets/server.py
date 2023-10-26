import zmq
import struct
import ormsgpack
import datetime

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

i = 0

while True:
    mesg = socket.recv()
    print(f"recv: {mesg}")

    data = {
        'time': datetime.datetime.now(),
        'count': i
    }

    socket.send(ormsgpack.packb(data))
    i += 1
    
