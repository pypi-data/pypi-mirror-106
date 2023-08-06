import qrcode
import cv2
from pyzbar import pyzbar
import random


def create(text, name):
    """generates qrcode"""

    img = qrcode.make(text)
    img.save(f'{name}.png')


def read(name):
    """reads qrcode"""

    img = cv2.imread(f'{name}.png')
    read_qrcode = pyzbar.decode(img)
    for i in read_qrcode:
        result = i.data.decode('utf-8')
        print(f'Result: {result}')


def generator(alphabet='+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',
              number=1, length=1):

    """creates passwords"""

    number = int(number)
    length = int(length)
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(alphabet)
        print(password)
