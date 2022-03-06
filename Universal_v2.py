# v0 -> v1 new instance 시에 생성된 인스턴스를 반환
# v1 -> v2 address 를 각 인스턴스 필드에도 저장 하도록 , DB 저장,불러오기 기능 추가
from pickle import *
class Universal:
    data_type = 'Universal'
    data_types = set()
    data_keys = []
    instances = {}

    def __init__(self, datas=None):
        self.datas = {'data1':'value1'}
        self.data1 = 'value1'

    def __repr__(self):
        return f'{self.datas}'

    def get_data(self, key):
        return self.datas[key]

    def set_data(self, key, data):
        self.datas[key] = data

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
        cls.instances[address].set_data('address', address)
        cls.data_types.update([cls.data_type])
        return cls.instances[address]


class Manager(Universal):
    @classmethod
    def find_address(cls, key, value):
        result_lis = []
        for i in cls.instances:
            if cls.instances[i].get_Data(key) == value:
                result_lis.append(cls.instances[i].get_data('address'))
        return result_lis

    @classmethod
    def get_instance(cls, address):
        return cls.instances[address]

    @classmethod
    def get_all_instance(cls):
        return cls.instances

    @classmethod
    def loaddata(cls):
        try:
            openfile = open(f'{cls.data_type}.p', 'rb')
        except:
            newfile = open(f'{cls.data_type}.p', 'wb')
            dump(cls.instances, newfile)
            newfile.close()
            openfile = open(f'{cls.data_type}.p', 'rb')
        finally:
            cls.instances.update(load(openfile))
            openfile.close()

    @classmethod
    def savedata(cls):
        savefile = open(f'{cls.data_type}.p', 'wb')
        dump(cls.instances, savefile)
        savefile.close()

