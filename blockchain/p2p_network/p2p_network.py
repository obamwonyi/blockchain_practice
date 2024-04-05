import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import asyncio
from blockchain.connection_pool.connection_pool import ConnectionPool


async def handle_connection(reader, writer):
    """
    This will handle the p2p communication
    reader : 
    writer : 
    """
    # Get a nickname for the new client
    writer.write("> Choose your nickname: ".encode())

    response = await reader.readuntil(b"\n")
    writer.nickname = response.decode().strip()

    connection_pool.add_new_user_to_pool(writer)
    connection_pool.send_welcome_message(writer)

    # Announce the arrival of this new user
    connection_pool.broadcast_user_join(writer)

    while True:
        try:
            data = await reader.readuntil(b"\n")
        except asyncio.exceptions.IncompleteReadError:
            connection_pool.broadcast_user_quit(writer)
            break
        message = data.decode().strip()
        if message == "/quit":
            connection_pool.broadcast_user_quit(writer)
        elif message == "/list":
            connection_pool.list_users(writer)
        else:
            connection_pool.broadcast_new_message(writer, message)

        await writer.drain()
        if writer.is_closing():
            break
    # Close connection and clean up
    writer.close()
    await writer.wait_closed()
    connection_pool.remove_user_from_pool(writer)


async def main():
    """
    Entry point of the code
    """
    server = await asyncio.start_server(handle_connection, "0.0.0.0", 8888)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    connection_pool = ConnectionPool()
    asyncio.run(main())

