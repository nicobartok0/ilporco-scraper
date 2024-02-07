from distutils.core import setup
import py2exe
from openpyxl import load_workbook, Workbook
from valuador import Valuador_Andina, Valuador_Maxiconsumo, Valuador_Oscar_David
from lector import Lector
from tkinter import *
from tkinter import ttk
import os
from threading import Thread
from operador import Operador

setup(windows=['ilporco-scraper.py'], packages=['lector', 'operador', 'valuador'])