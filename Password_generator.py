from tkinter import *

window = Tk()
window.title('Login Window')
window.geometry('250x200')


Label(window, text='Login').pack(pady=5)


Label(window, text='Email').pack()
Entry(window).pack()


Label(window, text='Password').pack()
Entry(window, show='*').pack()

window.mainloop()
