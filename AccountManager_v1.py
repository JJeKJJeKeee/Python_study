from Universal_v2 import *
from tkinter import *
from pickle import *

class Bank(Manager):
    data_type = 'Bank'
    data_keys = ['Person']

    # Logic_Method
    # 신규 계좌 생성 Person,Account,History 객체를 생성 하여 각각 Person<-Account<-History 연결
    # 예금 Account 객체에 address 입력받아 value 변경
    # 출금 Account 객체에 address 입력받아 value 변경
    # 송금 자신의 Account 객체 address 입력받고 보낼 상대의 Account 객체 address 입력하여 두 Account 의 value 변경
    # 내역 Account 객체의 value 변경되는 동작시 같이 동작하여 str 데이터로 저장
    # 데이터 삭제 객체 삭제 시에는 연결된 하위 객체 전체 삭제
    # --> 1. 신규 데이터 생성 / 2. Account 객체의 value 변경 / 3. Account


    # 데이터 출력 / ui ?


class User(Universal):
    data_type = 'Person'
    data_keys = ['name', 'Account']

class Account(Universal):
    data_type = 'Account'
    data_keys = ['value','History']

class History(Universal):
    data_type = 'History'
    data_keys = ['histories']
