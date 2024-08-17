#this code is writing test 
print("test")
#this code end here

#This is code to make digital clock
import tkinter as tk
from tkinter import font
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

clock_font = font.Font(family='Helvetica', size=60, weight='bold')

clock_label = tk.Label(root, font=clock_font, bg='black', fg='white')
clock_label.pack(anchor='center')

update_time()

root.mainloop()
#this code end here

