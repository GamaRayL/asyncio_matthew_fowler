import asyncio
from asyncio import Future
from util import delay
import aiohttp
import asyncio
import time
import socket

async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'


async def hello_every_second() -> None:
    for i in range(2):
        await asyncio.sleep(1)
        print('пока я жду, исполняется другой код')

def measure_time_async(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@measure_time_async
async def main() -> None:
    # TODO Конкурентное выполнение нескольких задач
    # sleep_for_three = asyncio.create_task(delay(3))
    # sleep_again = asyncio.create_task(delay(3))
    # sleep_more = asyncio.create_task(delay(3))
    # await sleep_for_three, sleep_again, sleep_more

    # TODO Выполнение кода пока другие операции работают в фоне
    # first_delay = asyncio.create_task(delay(3))
    # second_delay = asyncio.create_task(delay(3))
    # await hello_every_second()
    # await first_delay
    # await second_delay

    # TODO Снятие задачи
    # long_task = asyncio.create_task(delay(10))
    # seconds_elapsed = 0
    # while not long_task.done():
    #     print('Задача не закончилась, следующая проверка через секунду.')
    #     await asyncio.sleep(1)
    #     seconds_elapsed += 1
    #
    #     if seconds_elapsed > 4:
    #         long_task.cancel()
    # try:
    #     await long_task
    # except asyncio.CancelledError:
    #     print('Наша задача была снята')

    # # TODO Задание тайм-аута для задачи с помощью wait_for
    # delay_task = asyncio.create_task(delay(2))
    #
    # try:
    #     result = await asyncio.wait_for(delay_task, 1)
    #     print(result)
    # except asyncio.TimeoutError:
    #     print('Тайм-аут!')
    #     print(f'Задача была снята? {delay_task.cancelled()}')

    # # TODO Защита задачи от снятияx
    # task = asyncio.create_task(delay(10))
    #
    # try:
    #     result = await asyncio.wait_for(asyncio.shield(task), 5)
    #     print(result)
    # except asyncio.TimeoutError:
    #     print('Задача заняла более 5с, скоро она закончится!')
    #     result = await task
    #     print(result)
    #     print(f'Задача была снята? {task.cancelled()}')

    # async with aiohttp.ClientSession() as session:
    #     tasks = [
    #         asyncio.create_task(session.get('http://httpbin.org/get')),
    #         asyncio.create_task(session.get('http://httpbin.org/get'))
    #     ]
    #
    #     responses = await asyncio.gather(*tasks)
    #
    #     for resp in responses:
    #         print(await resp.text())

    pass




# asyncio.run(main(), debug=True)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f'Получен запрос на подключение от {client_address}!')

    buffer = b''

    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f'Получены данные: {data}!')
            buffer += data
    print(f'Все данные: {buffer}')
finally:
    server_socket.close()