from http.server import HTTPServer


class MyServer(HTTPServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__messages = dict()
        
        # временно
        self.message_to('234', 'Привет, Вася')
        self.message_to('234', 'Как поживаешь?')
        self.message_to('46', 'Спасибо, хорошо')
        
    def message_to(self, client, message):
        if client in self.__messages:
            self.__messages[client].append(message)
        else:
            self.__messages[client] = [ message ]

    @property
    def clients_count(self):
        return len(self.__messages)
        
    @property
    def all_clients(self):
        return list(self.__messages.keys())
        
    @property
    def messages_count(self):
        N = 0
        for v in self.__messages.values():
            N += len(v)
        return N
        
    def count_msg_for(self, client):
        return len(self.__messages.get(client,[]))
        
    def take_next(self, client):
        if client in self.__messages:
            result = self.__messages[client].pop(0)
            if not self.__messages[client]:
                del self.__messages[client]
            return result
        return None