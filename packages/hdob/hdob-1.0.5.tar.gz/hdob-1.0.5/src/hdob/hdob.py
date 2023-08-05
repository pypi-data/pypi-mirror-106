#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a tool to convert Hex/Dec/Oct/Bin
"""

import os
import time
import sys
import argparse
import re
import inspect
from functools import wraps
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

__author__ = "House Chou"
verbose = False
g_font = 'Hack'


class IntSubject():

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, caller, result):
        for observer in self.observers:
            if not isinstance(observer, type(caller)):
                if result.valid:
                    self.value = result.value
                observer.update(result)

    def clear(self):
        for observer in self.observers:
            observer.clear()

    def get_val(self):
        return self.value


class Str2Int():
    def __init__(self, value=0, valid=True):
        self.value = value
        self.valid = valid

    def convert(self, str, base):
        self.str = str
        try:
            self.value = int(str, base)
            self.valid = True
        except ValueError as e:
            self.valid = False
            if verbose:
                print("{}.{}:{}".format(self.__class__.__name__,
                                        inspect.currentframe().f_code.co_name,
                                        e))


class BinView(tk.Frame):

    def __init__(self, master, subject):
        tk.Frame.__init__(self,
                          master,
                          highlightbackground='grey',
                          highlightthickness=1)
        self.master = master
        self.subject = subject
        self.bits = []
        self.value = 0
        for i in range(0, 32):
            header = tk.Label(self, text=31 - i)
            bit = ToggleLabel(
                self,
                '1',
                '0',
                command=self.notify,
                highlightbackground='grey',
                highlightthickness=1,
            )
            self.bits.append(bit)
            header.grid(row=1, column=i, padx=5, pady=5)
            bit.grid(row=2, column=i, padx=5, pady=5)

    def notify(self):
        str2int = Str2Int()
        bitstr = ''
        for bit_label in self.bits:
            bit = bit_label['text']
            if bit == '1':
                bit_label.config(state=True, background='yellow')
            else:
                bit_label.config(state=False, background='#d9d9d9')
            bitstr += bit
        str2int.convert(bitstr, 2)
        self.subject.notify(self, str2int)

    def clear(self):
        self.update(Str2Int(0))

    def update(self, result):
        if result.valid:
            self.value = val = result.value
            # iterate from MSB to LSB
            for i in range(0, 32):
                s = (val >> (31 - i) & 0x1)
                if s == 1:
                    self.bits[i].config(state=True, background='yellow')
                else:
                    self.bits[i].config(state=False, background='#d9d9d9')


class HexView(tk.Frame):

    def __init__(self, master, subject):
        tk.Frame.__init__(self, master)
        self.master = master
        self.subject = subject
        self.value = 0
        self.prefix = ""
        self.hex_label = tk.Label(self, text='Hex')
        self.strvar = tk.StringVar()
        self.traceid = self.strvar.trace("w", self.notify)
        self.main_entry = tk.Entry(self,
                                   width=10,
                                   textvariable=self.strvar,
                                   font=(g_font, 12))
        self.main_entry.focus()
        self.hex_label.grid(row=0, column=0)
        self.main_entry.grid(row=0, column=1)

    def notify(self, *args):
        hex_str = self.strvar.get()
        if hex_str != "":
            self.prefix = "0x" if hex_str.startswith("0x") else ""
            str2int = Str2Int()
            str2int.convert(hex_str, 16)
            self.subject.notify(self, str2int)

    def clear(self):
        self.strvar.trace_vdelete("w", self.traceid)
        self.main_entry.delete(0, 'end')
        self.traceid = self.strvar.trace("w", self.notify)

    def update(self, result):
        if result.valid:
            self.value = result.value
            # disable tracer to prevent trigger the notify
            self.strvar.trace_vdelete("w", self.traceid)
            self.main_entry.delete(0, 'end')
            self.main_entry.insert(0, '{:s}{:x}'.format(self.prefix,
                                                        self.value))
            # recover the tracer
            self.traceid = self.strvar.trace("w", self.notify)


class DecView(tk.Frame):

    def __init__(self, master, subject):
        tk.Frame.__init__(self, master)
        self.master = master
        self.subject = subject
        self.value = 0
        self.dec_label = tk.Label(self, text='Dec')
        self.strvar = tk.StringVar()
        self.traceid = self.strvar.trace("w", self.notify)
        self.main_entry = tk.Entry(self,
                                   width=10,
                                   textvariable=self.strvar,
                                   font=(g_font, 12))
        self.dec_label.grid(row=0, column=0)
        self.main_entry.grid(row=0, column=1)

    def notify(self, *args):
        dec_str = self.strvar.get()
        if dec_str != "":
            str2int = Str2Int()
            str2int.convert(dec_str, 10)
            self.subject.notify(self, str2int)

    def clear(self):
        self.strvar.trace_vdelete("w", self.traceid)
        self.main_entry.delete(0, 'end')
        self.traceid = self.strvar.trace("w", self.notify)

    def update(self, result):
        if result.valid:
            self.value = result.value
            self.strvar.trace_vdelete("w", self.traceid)
            self.main_entry.delete(0, 'end')
            self.main_entry.insert(0, '{:d}'.format(self.value))
            self.traceid = self.strvar.trace("w", self.notify)


class OctView(tk.Frame):

    def __init__(self, master, subject):
        tk.Frame.__init__(self, master)
        self.master = master
        self.subject = subject
        self.value = 0
        self.oct_label = tk.Label(self, text='Oct')
        self.strvar = tk.StringVar()
        self.traceid = self.strvar.trace("w", self.notify)
        self.main_entry = tk.Entry(self,
                                   width=10,
                                   textvariable=self.strvar,
                                   font=(g_font, 12))
        self.oct_label.grid(row=0, column=0)
        self.main_entry.grid(row=0, column=1)

    def notify(self, *args):
        oct_str = self.strvar.get()
        if oct_str != "":
            str2int = Str2Int()
            str2int.convert(oct_str, 8)
            self.subject.notify(self, str2int)

    def clear(self):
        self.strvar.trace_vdelete("w", self.traceid)
        self.main_entry.delete(0, 'end')
        self.traceid = self.strvar.trace("w", self.notify)

    def update(self, result):
        if result.valid:
            self.value = result.value
            self.strvar.trace_vdelete("w", self.traceid)
            self.main_entry.delete(0, 'end')
            self.main_entry.insert(0, '{:o}'.format(self.value))
            self.traceid = self.strvar.trace("w", self.notify)


class Shift(tk.Frame):

    def __init__(self, master, subject):
        tk.Frame.__init__(self, master)
        self.master = master
        self.subject = subject
        self.rbtn = tk.Button(self, text='Shift >>', command=self.right_shift)
        self.lbtn = tk.Button(self, text='<< Shift', command=self.left_shift)
        self.shift_text = tk.StringVar()
        self.shift_text.set('1')
        self.shift_entry = tk.Entry(self,
                                    width=2,
                                    textvariable=self.shift_text,
                                    font=(g_font, 12))
        self.lbtn.grid(row=0, column=0, padx=2)
        self.shift_entry.grid(row=0, column=1, padx=2)
        self.rbtn.grid(row=0, column=2, padx=2)

    def get_shift_val(self):
        shift = self.shift_text.get()
        try:
            shift = int(shift, 10)
            return shift
        except ValueError as e:
            if verbose:
                print("{}.{}:{}".format(self.__class__.__name__,
                                        inspect.currentframe().f_code.co_name,
                                        e))
            return None

    def right_shift(self):
        shift = self.get_shift_val()
        if shift is not None:
            val = self.subject.get_val() >> shift
            self.subject.notify(self, Str2Int(val))

    def left_shift(self):
        shift = self.get_shift_val()
        if shift is not None:
            val = self.subject.get_val() << shift
            self.subject.notify(self, Str2Int(val))


class Status(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.status_label = tk.Label(self, text='Status:')
        self.status = tk.Label(self)
        self.status_label.grid(row=0, column=0)
        self.status.grid(row=0, column=1)

    def clear(self):
        self.status.config(text='')

    def update(self, result):
        if result.valid:
            self.status.config(text='OK', fg='green')
        else:
            self.status.config(text='FAIL', fg='red')


class ClearButton(tk.Frame):

    def __init__(self, master, subject):
        tk.Frame.__init__(self, master)
        self.master = master
        self.subject = subject
        self.btn = tk.Button(self, text='Clear', command=self.clear)
        self.btn.grid(row=0, column=0)

    def clear(self):
        self.subject.clear()


class ToggleLabel(tk.Label):

    def __init__(self,
                 master,
                 show_on,
                 show_off,
                 default_state=False,
                 command=None,
                 **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        # bind to mouse left button
        self.bind("<Button-1>",
                  lambda event: self.toggle(command))
        self.show_on = show_on
        self.show_off = show_off
        self.config_show_type()
        self.current = default_state
        self.config(default_state)

    def config_show_type(self):
        self.on_use_img = False
        self.on_use_str = False
        self.off_use_img = False
        self.off_use_str = False
        if type(self.show_on) == PhotoImage:
            self.on_use_img = True
        elif type(self.show_on) == str:
            self.on_use_str = True
        else:
            raise TypeError

        if type(self.show_off) == PhotoImage:
            self.off_use_img = True
        elif type(self.show_off) == str:
            self.off_use_str = True
        else:
            raise TypeError

    def toggle(self, func):
        self.current = not self.current
        self.config(self.current)
        if func is not None:
            func()

    def config(self, state, **kwargs):
        if state:
            if self.on_use_img:
                super().config(text='', image=self.show_on, **kwargs)
            elif self.on_use_str:
                super().config(text=self.show_on, image='', **kwargs)
        else:
            if self.off_use_img:
                super().config(text='', image=self.show_off)
            elif self.off_use_str:
                super().config(text=self.show_off, image='', **kwargs)
        self.current = state


def main():
    root = tk.Tk()
    root.title("HDOB Converter")
    status = Status(root)
    subject = IntSubject()
    bin_view = BinView(root, subject)
    hex_view = HexView(root, subject)
    dec_view = DecView(root, subject)
    oct_view = OctView(root, subject)
    shift = Shift(root, subject)
    clear = ClearButton(root, subject)
    subject.attach(bin_view)
    subject.attach(hex_view)
    subject.attach(dec_view)
    subject.attach(oct_view)
    subject.attach(status)
    hex_view.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    dec_view.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    oct_view.grid(row=0, column=2, padx=5, pady=5, sticky='e')
    bin_view.grid(row=1, columnspan=3, padx=5, pady=5, sticky='news')
    shift.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    status.grid(row=2, column=1, padx=5, pady=5, columnspan=1, sticky='w')
    clear.grid(row=2, column=2, padx=5, pady=5, columnspan=2, sticky='e')
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    if verbose:
        print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-V":
        verbose = True
    main()
