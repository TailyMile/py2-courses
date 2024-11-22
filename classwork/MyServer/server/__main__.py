from MyServer import MyServer
from MyHandler import MyHandler
from threading import Thread
from time import sleep

    

address = ('', 8000)
server = MyServer(address, MyHandler)

srv_thread = Thread(group=None, target=server.serve_forever)
srv_thread.start()

x = input('Press ENTER to stop: ')
server.shutdown()

srv_thread.join()
