class Universal:
    data_type = 'Universal'
    data_types = set()
    data_keys = []
    instances = {}

    def __init__(self, datas=None):
        self.__datas = datas

    def __repr__(self):
        return f'{self.__datas}'

    def get_data(self, key):
        return self.__datas[key]

    def set_data(self, key, data):
        self.__datas[key] = data

    @classmethod
    def new_instance(cls, datas=None):
        from random import randint
        while True:
            address = f'{randint(0, 999999999):09}'
            if address in cls.instances:
                continue
            break
        if datas is None:
            datas = {}
            for key in cls.data_keys:
                datas[key] = input(f'{key}:')
        cls.instances[address] = cls(datas)
        cls.data_types.update([cls.data_type])
        return cls.instances[address]


class Manager(Universal):
    @classmethod
    def new_type_instance(cls):
        print('data types : ', end='')
        for i in Manager.data_types:
            print(f'[{i}]', end=' ')
        print()
        type = input('type : ')
        for i in Universal.__subclasses__():
            if type == i.data_type:
                i.new_instance()

    @classmethod
    def get_instance(cls, address):
        return cls.instances[address]

    @classmethod
    def get_all_instance(cls):
        return cls.instances

    @classmethod
    def show_instance(cls):
        for i in cls.instances:
            print(cls.instances[i])

    @classmethod
    def manager(cls):
        menus = {'0': {'func_name': 'new data', 'func': cls.new_type_instance},
                 '1': {'func_name': 'show data', 'func': cls.show_instance},
                 '9': {'func_name': 'exit', 'func': lambda: True}}
        for i in menus:
            print(f'{i}.{menus[i]["func_name"]}', end=' ')
        print()
        select = input('select:')
        if select in menus:
            if menus[select]['func']():
                return True
        else:
            print('wrong input')
