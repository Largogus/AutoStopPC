import os
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
import os


tk = Tk()
tk.geometry("300x130")
tk.title("Авто-Стоп")

label = Label(text='Введите время и выберите параметр', font=('times new roman', 12))
label.place(x=20, y=0)
entry = Entry(font=('times new roman', 12))
entry.place(x=20, y=40)
vlist = ["Секунд", "Минут", "Час(ов)"]

Combo = ttk.Combobox(values=vlist, font=('times new roman', 12))
Combo.set("Параметр")
Combo.place(x=20, y=80)

def result():
    try:
        time = int(entry.get())
        argument = Combo.get()
        if time >= 0:
            if argument == "Секунд":
                def open_info():
                    showinfo(title="Информация", message=f"Компьютер перезапустится через {time} секунд")
                open_info()
                shutdown_cmd = f'shutdown -s -t {time}'
                os.system(f'{shutdown_cmd}')
            elif argument == 'Минут':
                def open_info():
                    showinfo(title="Информация", message=f"Компьютер перезапустится через {time} минут")
                open_info()
                res = time * 60
                shutdown_cmd = f'shutdown -s -t {res}'
                os.system(f'{shutdown_cmd}')
            elif argument == 'Час(ов)':
                def open_info():
                    showinfo(title="Информация", message=f"Компьютер перезапустится через {time} час(ов)")
                open_info()
                res = time * 60 * 60
                shutdown_cmd = f'shutdown -s -t {res}'
                os.system(f'{shutdown_cmd}')
            else:
                label_error = Label(text="Вы в чём то ошиблись!", font=('times new roman', 12), fg='red')
                label_error.place(x=20, y=120)
        else:
            label_error = Label(text="Вы в чём то ошиблись!", font=('times new roman', 12))
            label_error.place(x=20, y=120)
    except:
        label_error = Label(text="Вы в чём то ошиблись!", font=('times new roman', 12), fg='red')
        label_error.place(x=20, y=120)


button = Button(text="Начать", font=('times new roman', 12), command=result)
button.place(x=220, y=58)

tk.mainloop()