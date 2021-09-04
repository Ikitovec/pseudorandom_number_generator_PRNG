from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox


def open_file():
    txt.delete(1.0, END)
    filename = askopenfilename()
    print(filename)

    with open(filename, "rb") as file:
        inputText = file.read()
        inputText2 = ''
        for i in range(len(inputText)):
            inputText2 += chr(int(inputText[i]))

    txt.insert(INSERT, inputText2)
    print(len(inputText2))
    print('opened')


def save_file():
    txt_original = txt2.get("1.0", 'end-1c')
    filename = asksaveasfilename()
    A = [0] * len(txt_original)
    for i in range(len(txt_original)):
        A[i] = ord(txt_original[i])
    A = bytearray(A)
    with open(filename, "w+b") as file:
        file.write(A)
    print('saved')


def psc_gen():
    txt3.delete(1.0, END)
    txt_original = txt.get("1.0", 'end-1c')
    key = [0]
    x = int(spin.get())
    a = 106
    c = 1283
    m = 6075
    for i in range(len(txt_original)):
        new_x = ((x * a + c) % m) % 256
        key.append(new_x)
        x = new_x

    key.pop(0)
    txt3.insert(INSERT, key)
    txt_original = []
    key = []
    print('gen is end')


def clicked():

    result_text=''
    temp_dec_array = [0]
    txt2.delete(1.0, END)
    txt_original = txt.get("1.0", 'end-1c')
    key = txt3.get("1.0", 'end-1c').split()
    count = 0
    for i in txt_original:
        flag = 0
        current_letter_binary = bin(ord(i))[2:]
        mask_binary = bin(int(key[count]))[2:]
        current_mask_binary = ''
        additional_letter = ''

        if len(current_letter_binary) > len(mask_binary):
            while flag == 0:
                if len(current_mask_binary) + len(mask_binary) == len(current_letter_binary):
                    current_mask_binary += str(mask_binary)
                    mask_binary = current_mask_binary
                    flag = 1
                else:
                    current_mask_binary += '0'

        elif len(current_letter_binary) < len(mask_binary):
            while flag == 0:
                if len(current_letter_binary) + len(additional_letter) == len(mask_binary):
                    additional_letter += str(current_letter_binary)
                    current_letter_binary = additional_letter
                    flag = 1
                else:
                    additional_letter += '0'

        count += 1
        answer=int(current_letter_binary,2)^int(mask_binary,2)
        temp_dec_array.append(answer)
        result_text+=chr(answer)

    txt2.insert(INSERT, result_text)
    print('shifr comleted')

window = Tk()
window.title("Шифрование при помощи псевдослучайного числа")
window.geometry('700x400')

lbl = Label(window, text="Ваше сообщение")
lbl.grid(column=0, row=0)

txt = scrolledtext.ScrolledText(window, width=45, height=5)
txt.grid(column=1, row=0)

lbl = Label(window, text="Результат:")
lbl.grid(column=0, row=4)

txt2 = scrolledtext.ScrolledText(window, width=45, height=5)
txt2.grid(column=1, row=4)

lbl = Label(window, text="Ключ:")
lbl.grid(column=0, row=1)

txt3 = scrolledtext.ScrolledText(window, width=45, height=5)
txt3.grid(column=1, row=1)

btn = Button(window, text="Открыть", command=open_file)
btn.grid(column=0, row=2)
lbl = Label(window)

btn = Button(window, text="Сохранить", command=save_file)
btn.grid(column=1, row=2)
lbl = Label(window)

btn = Button(window, text="сгенерировать ПСЧ", command=psc_gen)
btn.grid(column=2, row=1)
lbl = Label(window)

btn = Button(window, text="преобразовать", command=clicked)
btn.grid(column=5, row=2)
lbl = Label(window)

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=2, row=0)

window.mainloop()
