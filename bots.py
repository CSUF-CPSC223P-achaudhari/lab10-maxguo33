import threading
import time

def bot_clerk(items):

    cart = []
    lock = threading.Lock()

    

    rfList = {1: [], 2: [], 3: []}

    for i, item in enumerate(items):
        rfList[(i % 3) + 1].append(item)

    def robot_fetcher(robot_list, cart, lock):
        for item in robot_list:
            with lock:
                cart.append(item)

    threads = []
    for robot_num, robot_list in rfList.items():
        thread = threading.Thread(target=robot_fetcher, args=(robot_list, cart, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return cart

def bot_fetcher(items, cart, lock):
    for item in items:
        time.sleep(int(item))
        with lock:
            cart.append([item, "description for item"])
        print("robot fetched", item)

    