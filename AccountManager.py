from Universal_v1 import *
from tkinter import *


class Bank(Manager):
    data_type = 'Bank'
    data_keys = ['Person']


class Person(Universal):
    data_type = 'Person'
    data_keys = ['name', 'Account']

    def __init__(self, datas):
        super().__init__(datas)


class Account(Universal):
    data_type = 'Account'
    data_keys = ['address', 'value', 'History']

    def __init__(self, datas):
        super().__init__(datas)


class History(Universal):
    data_type = 'History'
    data_keys = ['historys']

    def __init__(self, datas):
        super().__init__(datas)


def newaccountframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()
    laddress = Label(mainframe, text='계좌번호 : ')
    laddressgenerated = Label(mainframe, text='')
    lname = Label(mainframe, text='계좌주 : ')
    lvalue = Label(mainframe, text='초기입금액 : ')
    laddress.grid(row=0, column=0)
    laddressgenerated.grid(row=0, column=1)
    lname.grid(row=1, column=0)
    lvalue.grid(row=2, column=0)
    ename = Entry(mainframe)
    ename.grid(row=1, column=1)
    evalue = Entry(mainframe)
    evalue.grid(row=2, column=1)

    def makenewinstance():
        newaccount = Account.new_instance({})
        for i in Bank.instances:
            if Bank.instances[i] is newaccount:
                address = i
        laddressgenerated['text'] = address
        Account.instances[address].set_data('address', address)
        Account.instances[address].set_data('value', evalue.get())
        Account.instances[address].set_data('History',
                                            History.new_instance({'historys': [f'created!! val:{evalue.get()}']}))
        Person.new_instance({'name': ename.get(), 'Account': Account.instances[address]})

    def makenewdummy():
        from random import randint
        newaccount = Account.new_instance({})
        for i in Bank.instances:
            if Bank.instances[i] is newaccount:
                address = i
        laddressgenerated['text'] = address
        Account.instances[address].set_data('address', address)
        Account.instances[address].set_data('value', f'{randint(0, 10000)}')
        Account.instances[address].set_data('History', History.new_instance(
            {'historys': [f'created!! val:{Account.instances[address].get_data("value")}']}))
        Person.new_instance({'name': f'name{randint(0, 99)}', 'Account': Account.instances[address]})

    Button(mainframe, text='더미 생성', command=makenewdummy).grid(row=3, column=0)
    Button(mainframe, text='데이터 생성', command=makenewinstance).grid(row=3, column=1)


def showaccountframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    mainlb = Listbox(mainframe, width=100, height=20)
    mainlb.grid()
    for i in Bank.get_all_instance():
        if Bank.instances[i].data_type == 'Person':
            mainlb.insert(END, Bank.instances[i])


def showallframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    mainlb = Listbox(mainframe, width=100, height=20)
    mainlb.grid()
    for i in Bank.get_all_instance():
        mainlb.insert(END, f'{i},{Bank.instances[i].data_type},{Bank.instances[i]}')


def depositframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    laddress = Label(mainframe, text='계좌번호 : ')
    eaddress = Entry(mainframe)
    lvalue = Label(mainframe, text='잔액 : ')
    lvaluedata = Label(mainframe, text='')
    ldeposit = Label(mainframe, text='예금액 : ')
    edeposit = Entry(mainframe)
    laddress.grid(row=0, column=0)
    eaddress.grid(row=0, column=1)
    lvalue.grid(row=1, column=0)
    lvaluedata.grid(row=1, column=1)
    ldeposit.grid(row=2, column=0)
    edeposit.grid(row=2, column=1)

    def getaccount():
        tempaccount = Bank.instances[eaddress.get()]
        lvaluedata['text'] = tempaccount.get_data('value')

    def deposit():
        tempaccount = Bank.instances[eaddress.get()]
        tempaccount.set_data('value', str(eval(lvaluedata['text'] + '+' + edeposit.get())))
        tempaccount.get_data('History').get_data('historys').append(
            f'value changed!! val:{tempaccount.get_data("value")}')
        getaccount()

    Button(mainframe, text='계좌 확인', command=getaccount).grid(row=3, column=0)
    Button(mainframe, text='예금', command=deposit).grid(row=3, column=1)


def withdrawframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    laddress = Label(mainframe, text='계좌번호 : ')
    eaddress = Entry(mainframe)
    lvalue = Label(mainframe, text='잔액 : ')
    lvaluedata = Label(mainframe, text='')
    lwithdraw = Label(mainframe, text='출금액 : ')
    ewithdraw = Entry(mainframe)
    laddress.grid(row=0, column=0)
    eaddress.grid(row=0, column=1)
    lvalue.grid(row=1, column=0)
    lvaluedata.grid(row=1, column=1)
    lwithdraw.grid(row=2, column=0)
    ewithdraw.grid(row=2, column=1)

    def getaccount():
        tempaccount = Bank.instances[eaddress.get()]
        lvaluedata['text'] = tempaccount.get_data('value')

    def withdraw():
        tempaccount = Bank.instances[eaddress.get()]
        if eval(lvaluedata['text'] + '-' + ewithdraw.get()) >= 0:
            tempaccount.set_data('value', str(eval(lvaluedata['text'] + '-' + ewithdraw.get())))
            tempaccount.get_data('History').get_data('historys').append(
                f'value changed!! val:{tempaccount.get_data("value")}')
            getaccount()
        else:
            lvaluedata['text'] = '잔고가 부족합니다.'

    Button(mainframe, text='계좌 확인', command=getaccount).grid(row=3, column=0)
    Button(mainframe, text='출금', command=withdraw).grid(row=3, column=1)


def transferframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    laddress = Label(mainframe, text='계좌번호 : ')
    eaddress = Entry(mainframe)
    lvalue = Label(mainframe, text='잔액 : ')
    lvaluedata = Label(mainframe, text='')
    ltoaddress = Label(mainframe, text='송금할 계좌번호 : ')
    etoaddress = Entry(mainframe)
    ltransfer = Label(mainframe, text='송금액 : ')
    etransfer = Entry(mainframe)
    laddress.grid(row=0, column=0)
    eaddress.grid(row=0, column=1)
    lvalue.grid(row=1, column=0)
    lvaluedata.grid(row=1, column=1)
    ltoaddress.grid(row=2, column=0)
    etoaddress.grid(row=2, column=1)
    ltransfer.grid(row=3, column=0)
    etransfer.grid(row=3, column=1)

    def getaccount():
        tempaccount = Bank.instances[eaddress.get()]
        lvaluedata['text'] = tempaccount.get_data('value')

    def transfer():
        tempaccount = Bank.instances[eaddress.get()]
        if eval(lvaluedata['text'] + '-' + etransfer.get()) >= 0:
            tempaccount.set_data('value', str(eval(lvaluedata['text'] + '-' + etransfer.get())))
            tempaccount.get_data('History').get_data('historys').append(
                f'value changed!! val:{tempaccount.get_data("value")}')
            getaccount()
            tempaccount2 = Bank.instances[etoaddress.get()]
            tempaccount2.set_data('value', str(eval(lvaluedata['text'] + '+' + etransfer.get())))
            tempaccount2.get_data('History').get_data('historys').append(
                f'value changed!! val:{tempaccount2.get_data("value")}')
            getaccount()
        else:
            lvaluedata['text'] = '잔고가 부족합니다.'

    Button(mainframe, text='계좌 확인', command=getaccount).grid(row=4, column=0)
    Button(mainframe, text='송금', command=transfer).grid(row=4, column=1)


def showhistoryframe():
    global mainframe
    for i in mainframe.grid_slaves():
        i.destroy()

    subframe = Frame(mainframe)
    laddress = Label(subframe, text='계좌번호 : ')
    eaddress = Entry(subframe)
    laddress.grid(row=0, column=0)
    eaddress.grid(row=0, column=1)
    subframe.grid(row=0,column=0)

    def checkhistory():
        tempaccount = Bank.instances[eaddress.get()]
        for i in tempaccount.get_data('History').get_data('historys'):
            mainlb.insert(END, i)

    Button(subframe, text='내역확인', command=checkhistory).grid(row=1, column=1)
    mainlb = Listbox(mainframe, width=100, height=20)
    mainlb.grid(row=1,column=0)


main = Tk()
mainframe = Frame(main)
buttonframe = Frame(main)

Button(buttonframe, text='1.계좌 생성', command=newaccountframe).pack()
Button(buttonframe, text='2.계좌 목록', command=showaccountframe).pack()
Button(buttonframe, text='3.예금', command=depositframe).pack()
Button(buttonframe, text='4.출금', command=withdrawframe).pack()
Button(buttonframe, text='5.송금', command=transferframe).pack()
Button(buttonframe, text='6.내역', command=showhistoryframe).pack()
Button(buttonframe, text='7.전체 데이터 목록', command=showallframe).pack()

buttonframe.grid(row=0, column=0)
mainframe.grid(row=0, column=1)
main.mainloop()
