import zmq
import struct
import ormsgpack

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")

while True:
    socket.send(b"Test")

    mesg = socket.recv()
    print(f"recv: {ormsgpack.unpackb(mesg)}")

    
