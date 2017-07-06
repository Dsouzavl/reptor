from sys import argv
from shutil import copyfile

import os
import random

name = str(argv[0])
foldername = "clone"+str(random.randint(0,100)*10)


os.mkdir(foldername)
copyfile("payload.txt", foldername + '/' + "payload.txt")
copyfile(name,foldername + '/' + name)
