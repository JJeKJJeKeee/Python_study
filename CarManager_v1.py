from Universal_v1 import *
from tkinter import *
from pickle import *


class Car(Universal):
    data_type = 'Car'
    data_keys = ['이름', '엔진가격', '타이어가격', '옵션', '옵션이름', '최고속도', '구매가격']

    def __init__(self, datas):
        super().__init__(datas)


class Manager(Manager):
    @classmethod
    def loaddata(cls):
        try:
            openfile = open('carlis.p', 'rb')
        except:
            newfile = open('carlis.p', 'wb')
            dump(cls.instances, newfile)
            newfile.close()
            openfile = open('carlis.p', 'rb')
        finally:
            cls.instances.update(load(openfile))
            openfile.close()

    @classmethod
    def savedata(cls):
        savefile = open('carlis.p', 'wb')
        dump(cls.instances, savefile)
        savefile.close()


def inputframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()
    inputentries = []
    count = 0
    for i in Car.data_keys:
        if i != '구매가격':
            Label(mainframe, text=i).grid(row=count, column=0)
            inputentries.append(Entry(mainframe))
            inputentries[count].grid(row=count, column=1)
            count += 1

    def makenewinstance():
        datas = {}
        for i in range(len(Car.data_keys)):
            if Car.data_keys[i] != '구매가격':
                datas[Car.data_keys[i]] = f'{inputentries[i].get()}'
        datas['구매가격'] = eval(datas['엔진가격'] + '+' + datas['타이어가격'])
        Car.new_instance(datas)
        Manager.savedata()

    def makenewdummy():
        from random import randint
        datas = {}
        for i in range(len(Car.data_keys)):
            if Car.data_keys[i] != '구매가격':
                datas[Car.data_keys[i]] = f'{randint(0, 999)}'
        datas['구매가격'] = str(eval(datas['엔진가격'] + '+' + datas['타이어가격']))
        Car.new_instance(datas)
        Manager.savedata()

    Button(mainframe, text='데이터 생성', command=makenewinstance).grid(row=count, column=1)
    Button(mainframe, text='더미 생성', command=makenewdummy).grid(row=count, column=0)


def listframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    mainlb = Listbox(mainframe, width=100, height=20)
    mainlb.grid()
    for i in Manager.get_all_instance():
        mainlb.insert(END, Manager.instances[i])


def listframe2():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    mainlb = Listbox(mainframe, width=100, height=20)
    mainlb.grid()
    for i in Manager.instances:
        mainlb.insert(END, f"이름:{Manager.instances[i].get_data('이름')} 구매가격:{Manager.instances[i].get_data('구매가격')}")


def listframe3():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    mainlb = Listbox(mainframe, width=100, height=20)
    mainlb.grid()
    for i in Manager.instances:
        if Manager.instances[i].get_data('옵션') != '없음':
            mainlb.insert(END, f"이름:{Manager.instances[i].get_data('이름')} 옵션이름:{Manager.instances[i].get_data('옵션이름')}")


def listframe4():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    mainlb = Listbox(mainframe, width=100, height=20)
    mainlb.grid()
    templis = []
    for i in Manager.instances:
        templis.append(Manager.instances[i])

    templis = sorted(templis, key=lambda templis: templis.get_data('최고속도'))
    fast = templis[-1]
    slow = templis[0]

    mainlb.insert(END,
                  f"속도차이:{fast.get_data('최고속도')}-{slow.get_data('최고속도')}={eval(fast.get_data('최고속도') + '-' + slow.get_data('최고속도'))}")


def deleteframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    Label(mainframe, text='자동차 이름').grid(row=0, column=0)
    e1 = Entry(mainframe)
    e1.grid(row=0, column=1)

    def delete():
        deleteaddress = None
        for i in Manager.instances:
            if e1.get() == Manager.instances[i].get_data('이름'):
                deleteaddress = i
        if deleteaddress:
            Manager.instances.pop(deleteaddress)
            Manager.savedata()

    Button(mainframe, text='데이터 삭제', command=delete).grid(row=1, column=1)


Manager.loaddata()
main = Tk()
mainframe = Frame(main)
buttonframe = Frame(main)

Button(buttonframe, text='1.자동차 정보 입력', command=inputframe).pack()
Button(buttonframe, text='2.저장된 목록 보기', command=listframe).pack()
Button(buttonframe, text='3.구매 가격 조회', command=listframe2).pack()
Button(buttonframe, text='4.옵션 차량 조회', command=listframe3).pack()
Button(buttonframe, text='5.빠른차 느린차 비교', command=listframe4).pack()
Button(buttonframe, text='6.데이터 삭제', command=deleteframe).pack()
buttonframe.grid(row=0, column=0)
mainframe.grid(row=0, column=1)
main.mainloop()
