from tkinter import *
from tkinter import messagebox
from string import ascii_letters

LOGIN_TOKEN = 0x5678
PASSWORD_TOKEN = 0x1234

MESSAGE = 'Невалидный логин!!!!\nЛогин должен содержать только\nлатинские буквы'
EMPTY = ''

root = Tk()

def generate(login):
    result_sum = 0
    for char in login:
        result_sum += ord(char)
    return (result_sum ^ LOGIN_TOKEN) ^ PASSWORD_TOKEN


def validate_login(login):
    return all(map(lambda c: c in ascii_letters, login))


def get_password():
    login = loginInput.get()
    if validate_login(login):
        result['text'] = 'Твой пароль: ' + str(generate(login.upper()))
    else:
        messagebox.showerror(title='Ошибка', message=MESSAGE)
        result['text'] = EMPTY


root['bg'] = 'white'
root.title = 'keyGen'
root.geometry('350x300')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=350, width=300, bg="white")
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.7)

label = Label(frame, text='Keygen for Crackme', bg='white')
label.pack()

loginInput = Entry(frame, bg='white')
loginInput.place(relx=0.2, rely=0.15, width=170)

button = Button(frame, text='Generate', bg='white', command=get_password)
button.place(relx=0.37, rely=0.35)

result = Label(frame, text='', bg='white')
result.place(relx=0.25, rely=0.55)

root.mainloop()
