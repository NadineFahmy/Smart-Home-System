from tkinter import *
import serial

bluetooth_device = 'COM15'
baud_rate = 9600
ser = serial.Serial(bluetooth_device, baud_rate)

root = Tk()
root.title('Smart Home App')
root.geometry('360x640')
root.configure(bg='#fff')
root.resizable(False, False)

def lampon() :
    ser.write(b'Lamp on')

def lampoff() :
    ser.write(b'Lamp off')

def fanon() :
    ser.write(b'Fan on')

def fanoff() :
    ser.write(b'Fan off')

def ledon() :
    ser.write(b'LED on')

def ledoff() :
    ser.write(b'LED off')


Label(root, text='Smart Home', fg='#3EB489', bg='#fff', font=('Microsoft YaHei UI Light', 23, 'bold')).place(relx = 0.5, rely = 0.1, anchor = CENTER)
frame = Frame(root, bg='#fff')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

Button(frame, text='Lamp on', width=10, pady=5, bg='#3EB489', fg='#fff', command= lampon).grid(row= 0, column= 0, padx= 10, pady= 10)
Button(frame, text='Lamp off', width=10, pady=5, bg='#3EB489', fg='#fff', command= lampoff).grid(row= 0, column= 2, padx = 10)

Button(frame, text='Fan on', width=10, pady=5, bg='#3EB489', fg='#fff', command= fanon).grid(row= 2, column= 0)
Button(frame, text='Fan off', width=10, pady=5, bg='#3EB489', fg='#fff', command= fanoff).grid(row= 2, column= 2)

Button(frame, text='LED on', width=10, pady=5, bg='#3EB489', fg='#fff', command= ledon).grid(row= 4, column= 0, padx= 10, pady= 10)
Button(frame, text='LED off', width=10, pady=5, bg='#3EB489', fg='#fff', command= ledoff).grid(row= 4, column= 2, padx = 10)


root.mainloop()