import asyncio

clients = set()
host = '127.0.0.1'
port = 56000


async def client_handler(reader, writer):
    # handle each client instance

    address = writer.get_extra_info('peername')
    print(f"New connection: {address}")
    clients.add(writer)
    try:
        while True:
            userInput = await reader.readline()
            if(userInput == b''):
                break
            elif(userInput.decode().strip().lower() == "/list"):
                writer.write(list_clients(writer).encode())
                await writer.drain()
    except Exception as e:
        print(f"Error with client {address}: {e}")
    finally:
        # client cleanup

        clients.remove(writer)
        writer.close()
        await writer.wait_closed()
        print(f"Connection closed: {address}")
    pass


def list_clients(writer):
    client_list = ""
    for client in clients:
        client_list += "{0}:{1}".format(*client.get_extra_info('peername'))
        if(client == writer):
            client_list += " (You)"
        client_list += "\n"
    return client_list


async def main():
    server = await asyncio.start_server(client_handler,host,port)
    print(f"Server is running on {host}:{port}...")
    await server.serve_forever()
    pass

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    pass