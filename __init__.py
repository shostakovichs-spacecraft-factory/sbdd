from server import SBDServer, SBDHandler
from p

HOST, PORT = "localhost", 5555

FMT = "<cI2ih3f2HI3f?"
FIELDS = ("Flag", "Time", "BMPPress", "BMPTemp", "DSTemp", 
    "X", "Y", "Z", "CDMConc", "MQ7Conc", "GeigerTicks", 
    "Longitude", "Latitude", "Height", "HasFix")
SIZE = 1024

URL = "http://172.16.164.221:5000/api"
METHOD = "pushdata"
JSON_RPC = "2.0"

addr = (HOST, PORT)
msg = (FMT, FIELDS, SIZE)
api = (URL, METHOD, JSON_RPC)

Server = SBDServer(addr, SBDHandler, msg, api)
Server.serve_forever()