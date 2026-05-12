# Multiclient Sever

A python server than can handle multiple clients that send basic requests

## Instructions for Build and Use

Steps to build and/or run the software:

1. Install python and asyncio package
2. If using remote networking: change "host" on server.py and client.py to the network server.py will be run on.
3. Change "port" on server.py and client.py to an available port on the device server.py will be running on (if necessary)
4. Run server.py
5. Run client.py

Instructions for using the software:

1. Start server.py
2. Start any number of instances of client.py (if using remote networking, you can also start client.py on remote devices)
3. Use /list on any client device to see other clients

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.14.4
* asyncio 4.0.0

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)
* [Python's asyncio: A Hands-On Walkthrough](https://realpython.com/async-io-python/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add more commands, including a disconnect.
* [ ] Add regular pings from the server to each client
