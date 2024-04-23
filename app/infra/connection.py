import asyncio

import aiomysql


class Connection:
    def __init__():
        loop = asyncio.get_event_loop()

        config = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "",
            "db": "mysql",
            "loop": loop,
        }

        async def test_example():
            conn = await aiomysql.connect(**config)

            cur = await conn.cursor()
            await cur.execute("SELECT Host,User FROM user")
            print(cur.description)
            r = await cur.fetchall()
            print(r)
            await cur.close()
            conn.close()

        loop.run_until_complete(test_example())
