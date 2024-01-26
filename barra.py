from tkinter import *
from tkinter import ttk
import time
window = Tk()
window.title('Progress bar pruebas')
window.geometry('400x400')
abc = IntVar()
current_value = 0
progbar = ttk.Progressbar(window, max=10, variable=abc, length=200)
progbar.grid(row=0, column=0, pady=10, padx=10)
for i in range(10):
    window.update_idletasks()
    abc.set(i+1)
    print(i)
    for j in range(100000):
        print(j)
    print('UPDATE!')
    time.sleep(1)
    
    

if __name__ == '__main__':
    window.mainloop()