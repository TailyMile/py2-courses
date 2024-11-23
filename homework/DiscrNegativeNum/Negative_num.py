import logging

class NoNegative(object):

    def __init__(self):
        self.__name = None
        self.__internal_attr_name = None

    def __set_name__(self, owner, name):
        self.__name = name
        self.__internal_attr_name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        if instance is None:
            return self
        logging.debug(f'Reading descriptor "{self.__name}"')
        if hasattr(instance, self.__internal_attr_name):
            return getattr(instance, self.__internal_attr_name)
        else:
            return 0  # Возвращаем 0, если значение не установлено

    def __set__(self, instance, value):
        logging.debug(f'Setting descriptor "{self.__name}" value {value}')
        if value >= 0:
            setattr(instance, self.__internal_attr_name, value)
        else:
            raise ValueError(f'{self.__name} не может быть отрицательным!')

    def __delete__(self, instance):
        logging.debug(f'Deleting descriptor value {self.__name}')
        if hasattr(instance, self.__internal_attr_name):
            delattr(instance, self.__internal_attr_name)