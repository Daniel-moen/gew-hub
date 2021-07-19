from tkinter import *
import pynput
import time
from config import transparency, transparency_toggle

from scripts import script_1, script_2
global open_settings
open_settings = 0
global toggle1
toggle1 = 0
global check
check = 0
if transparency_toggle == 0:
    check = 'On'
else:
    check = 'Off'
hub = Tk()
hub.config(bg = '#454545',)
hub.geometry('407x321')
hub.attributes('-topmost',True)
hub.overrideredirect(1)
if transparency_toggle == 0:
    hub.attributes('-alpha',transparency)
if transparency_toggle == 1:
    hub.attributes('-alpha',1)
#make window draggable

class WindowDraggable():

    def __init__(self, label):
        self.label = label
        label.bind('<ButtonPress-1>', self.StartMove)
        label.bind('<ButtonRelease-1>', self.StopMove)
        label.bind('<B1-Motion>', self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self,event):
        x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
        y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
        hub.geometry("+%s+%s" % (x, y))
drag_bar = Label(
    hub,
    text = '\n',
    width =407,
    bg = '#5C5E5D')
drag_bar.place(
    x=0,
    y=-10)
WindowDraggable(drag_bar)
#------------------------
#toolbar
def close_window():
    hub.destroy()
close_image = PhotoImage(file = "close.png")
close_button = Button(
    hub,
    image = close_image,
    bg = '#5C5E5D',
    highlightthickness=0,
    bd = 0,
    command=close_window)
close_button.place(
    x = 383,
    y=4)
def minimize_window():
    hub.withdraw()
    hub.overrideredirect(False)
    hub.iconify()
def check_map(event): # apply override on deiconify.
    if str(event) == "<Map event>":
        hub.overrideredirect(1)
        print ('Deiconified', event)
    else:
        print ('Iconified', event)
minimize_image = PhotoImage(file = "minimize.png")
minimize_button = Button(
    hub,
    image = minimize_image,
    bg = '#5C5E5D',
    highlightthickness=0,
    bd = 0,
    command=minimize_window)
minimize_button.place(
    x = 363,
    y=4)
hub.bind('<Map>', check_map) 
hub.bind('<Unmap>', check_map)
#------------------------------------------
#background elements
background_canvas1 = Canvas(
    hub,
    bg = "#6e6e6e",
    height = "255",
    width='176')
background_canvas1.place(
    y=30,x=3)
background_canvas2 = Canvas(
    hub,
    bg = "#6e6e6e",
    height = "255",
    width='210')
background_canvas2.place(
    y=30,x=190)
background_canvas3 = Canvas(
    hub,
    bg = "#6e6e6e",
    height = "20",
    width='396')
background_canvas3.place(
    y=293,x=3)
#-----------------------------
#settings
def settings_window_open():
    global open_settings
    
    if open_settings == 0:
        def toggle():
            global check
            global toggle1

            if toggle1 == 0:
                toggle1 = 1
                transparency_toggle_button.config(text = 'Off')
            else:
                toggle1 = 0
                transparency_toggle_button.config(text = 'On')

            
            print (toggle1)
        open_settings = 1
        def save():
            config_open = open('config.py', 'w')
            value_write = (transparency_slider.get())
            value_write = value_write / 10
            value_write = str(value_write)
            toggle_final_1 = str(toggle1)
            value_write_final = ('transparency = ' + value_write  + '\ntransparency_toggle = ' + toggle_final_1)
            config_open.write(value_write_final)
            
            if toggle1 == 0:
                hub.attributes('-alpha',value_write)
            if toggle1 == 1:
                hub.attributes('-alpha',1)
        def close_window_settings():
            global open_settings
            open_settings = 0
            background_settings_header.destroy()
            background_settings.destroy()
            close_settings_window.destroy()
            transparency_label.destroy()
            transparency_slider.destroy()
            save_button_settings.destroy()
            transparency_toggle_button.destroy()
        background_settings = Canvas(
            hub,
            bg = '#6e6e6e',
            height = '200',
            width='270')
        background_settings.place(
            x = 70,
            y = 50)
        background_settings_header = Label(
            hub,
            text = 'Settings',
            bg = '#6e6e6e',
            fg = 'white',
            font = ("ariel", 12))
        background_settings_header.place(
            x=73,
            y = 53)
        close_settings_window = Button(
            hub,
            bg = '#5C5E5D',
            text = ' x ',
            highlightthickness=0,
            bd = 0,
            fg = 'white',
            command=close_window_settings)
        close_settings_window.place(
            x = 320,
            y = 55)
        transparency_label = Label(
            hub,
            text = 'Transparency',
            bg = '#6e6e6e',
            fg = 'white',
            font = ("ariel", 9))
        transparency_label.place(
            x = 73,
            y = 80)
        transparency_slider = Scale(
            hub,
            from_=1,
            to=10, 
            orient=HORIZONTAL,
            bg = '#6e6e6e',
            fg = 'white')
        transparency_slider.place(
            x = 73,
            y = 100)
        transparency_toggle_button = Button(
            hub,
            bg = '#5C5E5D',
            text = check,
            highlightthickness=0,
            bd = 0,
            fg = 'white',
            command = toggle)
        transparency_toggle_button.place(
            x = 73,
            y = 150)
        save_button_settings = Button(
            hub,
            bg = '#5C5E5D',
            text = 'Save',
            highlightthickness=0,
            bd = 0,
            fg = 'white',
            command = save)
        save_button_settings.place(
            x = 73,
            y = 230)     
settings_button = Button(
    hub,
    bg = '#5C5E5D',
    text = 'Settings',
    highlightthickness=0,
    bd = 0,
    fg = 'white',
    command = settings_window_open)
settings_button.place(
    y = 295,
    x = 7)
title_label = Label(
    hub,
    text = 'Gew Hub',
    bg = '#5C5E5D',
    fg = 'white',
    font = ("ariel", 12, "bold"))
title_label.place(
    y = 1, x = 1)

#scripts VVV
script_1(hub)
script_2(hub)
#add resources here
hub.mainloop()