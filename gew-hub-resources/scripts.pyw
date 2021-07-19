from tkinter import *
import pynput
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
global spammer
global volume_mixer
spammer = 0
volume_mixer = 0
def script_1(gui):
    global spammer
    def script_1_proccesing():
        global spammer
        global volume_mixer
        spammer = spammer + 1
        if volume_mixer == 1:
            WIP.destroy()

        global warning, background_canvas10,spam_text_header,spammer_start_button,spam_text
        def spam_message():
            message = spam_text.get()
            time.sleep(5)
            while True:
                time.sleep(1)
                keyboard.type(message)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
        global warning, background_canvas10,spam_text_header,spammer_start_button,spam_text
        warning = Label(
            gui,
            text = 
            '''**WARNING**\nRunning this spammer WILL \nFreeze the program\nMake sure you have a way of \nclosing the program \nafter its run, this will be \nfixed in the future.\nthanks for your patience''',
            bg = '#6e6e6e',
            fg = '#ff4e3b',
            font = ("ariel", 9, 'bold'))
        warning.place(
            x = 215,
            y = 90)
        background_canvas10 = Canvas(
            gui,
            bg = "#6e6e6e",
            height = '31',
            width='149')
        background_canvas10.place(
            x=221.3,
            y=232.3)
        spam_text_header = Label(
            gui,
            text = 'Enter Text Below:',
            bg = '#6e6e6e',
            fg = 'white',
            font = ('ariel', 12, 'bold'))
        spammer_start_button = Button(
            gui,
            text = 'Start Spamming',
            bg = '#5C5E5D',
            fg = 'white',
            width = 14,
            bd = 0,
            font  = ('ariel', 12, 'bold'),
            command = spam_message)
        spammer_start_button.place(
            x = 225,
            y = 235) 
        spam_text_header.place(
            x = 225,
            y = 35)
        spam_text  = Entry(
            gui,
            width = 25,
            bd = 0,
            bg = 'white')
        spam_text.place(
            x = 225,
            y= 55)
    Message_spammer_button = Button(
        gui,
        text = 'Message_spammer.py ',
        bg = '#5C5E5D',
        width = 24,
        fg = 'white',
        bd = 0,
        command = script_1_proccesing)
    Message_spammer_button.place(
        x = 5.5,
        y = 33)
def script_2(gui):
    global volume_mixer
    def volume_mixer_start():
        global spammer 
        global volume_mixer
        global WIP
        volume_mixer = volume_mixer + 1
        if spammer == 1:
            global warning, background_canvas10,spam_text_header,spammer_start_button,spam_text
            warning.destroy()
            spam_text.destroy()
            background_canvas10.destroy()
            spam_text_header.destroy()
            spammer_start_button.destroy()
            spammer = spammer - 1
        WIP = Label(
            gui,
            text = 'Coming soon',
            bg = '#6e6e6e',
            fg = 'White',
            font = ("ariel", 15, 'bold'))
        WIP.place(
            x = 235,
            y = 40)
            
    Message_spammer_button = Button(
        gui,
        text = 'Volume_Mixer.py',
        bg = '#5C5E5D',
        width = 24,
        fg = 'white',
        bd = 0,
        command = volume_mixer_start)
    Message_spammer_button.place(
        x = 5.5,
        y = 57)