

from tkinter import *
from tkinter import ttk
from Tag_Builder import *
from module_template import *
from Vid_Handle import *
from functools import partial


class VisualObject:

    def __init__(self, a_x, a_y, b_x, b_y):
        self.p1_x = a_x
        self.p1_y = a_y
        self.p2_x = b_x
        self.p2_y = b_y

        self.obj_tags = []

        self.file = None
