from collections.abc import MutableSequence
from dataclasses import dataclass
from datetime import date
from decimal import Decimal


class DeprecatedOperation(Exception):
    pass


@dataclass
class Client(object):
    iid: int = None
    fam_name: str = None
    birth_date: date = None
    money: Decimal = 0
    city: str = None


class ClientsCollection(MutableSequence):

    def __init__(self, sort_by:str='fam_name', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__sort_by = sort_by
        self.__contents = []

    def __len__(self):
        return len(self.__contents)

    def insert(self, index, client):
        for c in self.__contents:
            if c is client:
                return
        for c in self.__contents:
            if c.iid == client.iid:
                raise Exception()  # Создать тип исключения
        self.__contents.append(client)
        self.__contents.sort(key=lambda c: getattr(c, self.__sort_by))

    def __getitem__(self, index: (int, str)) -> Client:
        if isinstance(index, int):
            return self.__contents[index]
        else:
            for c in self.__contents:
                if c.fam_name == index:
                    return c
            raise KeyError(index)

    def __delitem__(self, index: int):
        del self.__contents[index]

    def __setitem__(self, key, value):
        raise DeprecatedOperation('CliensCollection.__setitem__')

    def select(self, *, iid:int=None, index:int=None, **kwargs):
        if iid is not None:
            for c in self.__contents:
                if c.iid == iid:
                    return c
            raise KeyError(iid)
        elif index is not None:
            return self.__contents[index]
        else:
            key = list(kwargs)[0]
            value = kwargs[key]
            # Реализовать оставшуюся часть самостоятельно
