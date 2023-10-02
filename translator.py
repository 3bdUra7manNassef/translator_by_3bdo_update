from tkinter import *
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.argosopentech.com/")

def dark_mode():
    root.config(bg='black')

def light_mode():
    root.config(bg='white')

def close():
    exit()

root = Tk()
root.geometry('700x400')

menu_bar = Menu(root)
sitting_menu = Menu(menu_bar, tearoff=0)
sitting_menu.add_command(label='dark mode', command=dark_mode)
sitting_menu.add_command(label='light mode', command=light_mode)
menu_bar.add_cascade(label='setting', menu=sitting_menu)
sitting_menu.add_separator()
sitting_menu.add_command(label='close', command=close)
root.config(menu=menu_bar)

label_input_sign = Label(root, text='enter text', font='arial 15 bold')
label_input_sign.place(x=80, y=45)

text_input = Text(root, width=30, height=11)
text_input.place(x=15, y=100)

language_data = lt.languages()
language_names = [lang['name'] for lang in language_data]
language_codes = {lang['name']: lang['code'] for lang in language_data}

input_language = ttk.Combobox(root, values=language_names, state='readonly')
input_language.place(x=55, y=75)

def btn_translate():
    translated_text = lt.translate(text_input.get('1.0', 'end-1c'), language_codes[input_language.get()], language_codes[output_language.get()])
    text_output.delete('1.0', END)
    text_output.insert('1.0', translated_text)

btn_translate = Button(root, text='translate', font='arial 15 bold', command=btn_translate)
btn_translate.place(x=275, y=180)

lb_sign_translator_app = Label(root, text='TRANSLATOR BY 3BDO', font='arial 15 bold')
lb_sign_translator_app.place(x=250, y=0)

label_output_sign = Label(root, text='output translate', font='arial 15 bold')
label_output_sign.place(x=460, y=45)

text_output = Text(root, width=30, height=11)
text_output.place(x=400, y=100)

output_language = ttk.Combobox(root, values=language_names, state='readonly')
output_language.place(x=440, y=75)

root.mainloop()
