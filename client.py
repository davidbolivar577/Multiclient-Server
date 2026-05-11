import asyncio
import sys

host = '127.0.0.1'
port = 56000

async def receiver(reader):
    # watching for messages from server

    while True:
        server_message = await reader.readline()
        if server_message == b'':
            break
        else:
            print(server_message.decode())
    pass

async def sender(writer):
    # sending to server

    loop = asyncio.get_event_loop()
    while True:
        user_input = await loop.run_in_executor(None, sys.stdin.readline)
        writer.write(user_input.encode())
        await writer.drain()
    pass

async def main():
    try:
        reader, writer = await asyncio.open_connection(host,port)
        print(f"Connected to {host}:{port}")
        print("Type /list to see current connections")
        await asyncio.gather(
            receiver(reader),
            sender(writer)
        )
    finally:
        # cleanup

        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nClient shutting down.")