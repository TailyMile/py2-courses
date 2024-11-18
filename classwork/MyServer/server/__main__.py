from MyServer import MyServer
from MyHandler import MyHandler
from threading import Thread
from time import sleep


game_over = False
def testfunc():
    global game_over
    
    while not game_over:
        print('Hi')
        sleep(1)

address = ('', 8000)
server = MyServer(address, MyHandler)

srv_thread = Thread(group=None, target=testfunc, args=(), kwargs={})
srv_thread.start()

x = input('Press ENTER tio stop: ')

game_over = True
sleep(5)

srv_thread.join()

#server.serve_forever()
