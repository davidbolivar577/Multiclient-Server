# Multiclient Server
A python server than can handle multiple clients and send basic requests

Use:
0. If using remote networking: change "host" on server.py and client.py to the network server.py will be run on.
1. Change "port" on server.py and client.py to an available port on the device server.py will be running on (if necessary)
2. Start server.py
3. Start any number of instances of client.py (if using remote networking, you can also start client.py on remote devices)
4. Use /list on any client device to see other clients