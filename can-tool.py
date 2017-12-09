from pyvit import can
from pyvit.hw import socketcan

print("opening can socket")
dev = socketcan.SocketCanDev("can0")
print("starting device")
dev.start()
print("Waiting on data")
while True:
    print(dev.recv())
