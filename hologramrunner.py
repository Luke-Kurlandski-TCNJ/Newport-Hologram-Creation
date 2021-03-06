"""
A runner program which can run one of several GUI classes to run experiment.

@author: Luke Kurlandski
@date: December 2019
@copyright: Copyright 2019, Luke Kurlandski, all rights reserved

Special thanks to Daniel Stolz, Matthew Van Soelen, and Dr. David McGee.

Read the Program Guide for detailed information about this program.
"""

import tkinter as tk

from app import App
from singleimage import SingleImage

def single_image():
	root.destroy()
	new_root = tk.Tk()
	app = SingleImage(new_root)
	app.root.mainloop()

root = tk.Tk()
configs = {
    'Window Title':'Hologram Creator -- '
            + 'Copyright 2019, Luke Kurlandski, all rights reserved',
    'Window Width':200,
    'Window Height':200
}
chooser = App(root, configs)
tk.Label(chooser.root, text='Select an Experiment').pack()
button_singleimage = tk.Button(chooser.root, text='Single Image', 
	command=single_image)
button_singleimage.pack()
root.mainloop()