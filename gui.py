import os, sys, json, time, threading, math
import tkinter as tk
from colorama import Fore

win = tk.Tk()
win.title("Cookie Clicker")
win.geometry("1280x720")


buyWorkersButtonFrame = tk.Frame(win)
buyWorkersButtonFrame.grid(column=1, row=1)
buyUpgradesButtonFrame = tk.Frame(win)
buyUpgradesButtonFrame.grid(column=1, row=2)
buyWorkersButton = tk.Button(buyWorkersButtonFrame, text="Buy workers")
buyWorkersButton.pack(expand=1)
buyUpgradesButton = tk.Button(buyWorkersButtonFrame, text="Buy workers")
buyUpgradesButton.pack(expand=1)


win.mainloop()