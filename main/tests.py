from django.test import TestCase
import av
# import asyncio
#
# async def hello_world():
#     while True:
#         print("hello world")
#         await asyncio.sleep(5)
#
#
# async def hello_world2():
#     while True:
#         await asyncio.sleep(2)
#         print("hello world 2")
#
# loop = asyncio.get_event_loop()
# tasks = [
#     hello_world(),
#     hello_world2()
# ]
# # loop.run_until_complete(asyncio.wait(tasks))
# # loop.create_task(hello_world)
# # loop.create_task(hello_world2)
# loop.call_soon(hello_world)
# loop.run_forever()
# # loop.run_until_complete(hello_world(loop))
# # loop.run_until_complete(hello_world2(loop))
# loop.close()

def get_pic():
    container = av.open('rtsp://localhost:5454/test1.webm')
    video = next(s for s in container.streams if s.type == 'video')
    for packet in container.demux(video):
        for frame in packet.decode():
            yield frame

frame = next(get_pic())
frame.to_image().save('tmp/frame-%04d.jpg' % frame.index)


# for stream in video:
#     print(stream.bit_rate)

# for packet in container.demux(video):
#     for frame in packet.decode():

        # frame.to_image().save('tmp/frame-%04d.jpg' % frame.index)
        # print(frame.time)