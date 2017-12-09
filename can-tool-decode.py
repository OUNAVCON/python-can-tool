from pyvit.file import jsondb
from pyvit.hw import socketcan

parser = jsondb.JsonDbParser()
print("Opening can signal json database")
b = parser.parse("can-db.json")
print("Opening can socket")
dev = socketcan.SocketCanDev("can0")
print("starting can device")
dev.start()
print("waiting on data")
while True:
    frame = dev.recv()
    signals = b.parse_frame(frame)
    if signals:
        for s in signals:
            print(s)
