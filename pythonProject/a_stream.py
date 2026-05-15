# astream 异步流式传输，可以在不等待整个响应完成的情况下处理数据。
import asyncio
import time

# 同步的方式执行任务，任务之间是串行的，必须等待前一个任务完成后才能执行下一个任务。
#1.烧水
#2. 发消息


# def boil_water():
#     print("正在烧水...")
#     # 模拟烧水的过程
#     time.sleep(5) # 模拟5秒钟的烧水过程  CPU完全空闲,不让出 CPU 的控制权，其他任务无法执行
#     print("水烧好了！")
#
#
# def send_message():
#     print("正在发送消息...")
#     # 模拟发送消息的过程
#     time.sleep(2)
#     print("消息发送成功！")
#
#
# def main():
#     # 1. 烧水
#     boil_water()
#     # 2. 发消息
#     send_message()
#
#
# main()





# 异步的方式执行任务，任务之间是并行的，可以同时执行多个任务，不需要等待前一个任务完成后才能执行下一个任务。
# 1.烧水
# 2. 发消息


# 协程：一种轻量级的线程，可以在单线程中实现并发执行。协程通过 yield 或 async/await 关键字来实现任务的切换和调度。
# 协程的优势
# 1. 轻量级：协程比线程更轻量级，创建和销毁的开销更小，可以同时运行更多的协程。其调度完全由用户端控制，不需要操作系统的参与，因此可以更高效地利用资源。
# 2. 高效：协程通过让出 CPU 的控制权来实现任务的切换，避免了线程切换的上下文切换开销，提高了性能。
# 3. 易于编写：使用 async/await 语法可以更直观地编写异步代码，避免了回调地狱的问题，使代码更清晰易懂。
async def boil_water():
    print("正在烧水...")
    # 模拟烧水的过程
    await asyncio.sleep(5)   # 模拟5秒钟的烧水过程  await 让出 CPU 的控制权，允许其他任务执行
    print("水烧好了！")


async def send_message():
    print("正在发送消息...")
    # 模拟发送消息的过程
    await asyncio.sleep(2)
    print("消息发送成功！")


# 协程： 调度
# 事件循环：一个无限循环，负责调度和执行协程任务。当一个协程遇到 await 关键字时，
# 事件循环会暂停该协程的执行，并将控制权转移给其他可运行的协程。当被等待的操作完成后，事件循环会恢复该协程的执行。
async def main():
    # 1. 烧水（任务）
    task1 = asyncio.create_task(boil_water())  # 创建一个任务，立即执行，但不等待其完成
    # 2. 发消息
    task2 = asyncio.create_task(send_message())  # 创建一个任务，立即执行，但不等待其完成

    await task1  # 等待烧水任务完成
    await task2  # 等待发消息任务完成


# run 方法会自动创建一个事件循环，并运行 main 协程。
asyncio.run(main())


