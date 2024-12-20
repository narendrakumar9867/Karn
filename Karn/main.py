import os

import eel
from engine.features import *

#To point www directiry for knowing there is frontend file locate.
eel.init("www")

playAssistantsound()

#It's a legitimate executable file associated with Microsoft Edge, the default web browser in Windows 10 and later versions. It is responsible for launching and running the Microsoft Edge browser on your system.
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html' , mode='default', host='localhost', block=True) 

