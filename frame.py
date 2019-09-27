#created by Memoona Tahira on 25 september 2019 on 15:28
# you need to have ffmpeg instaled and on the path.



import os
import subprocess as sp
import sys
from sys import platform as _platform


#check the platform to detremine how to call ffmpeg library

if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
    FFMPEG_BIN = "fmpeg"
elif _platform == "win32"  or _platform == "win64":
    FFMPEG_BIN = "ffmpeg.exe"
else:
    sys.exit("unknown  Operating system. Terminating program")


# Create directory for storing frames called 'frames'

DIR = os.path.abspath(os.path.dirname(__file__))
FRAMEDIR=os.path.join(DIR, 'frames')
if not os.path.isdir(FRAMEDIR):
    os.mkdir(FRAMEDIR)

# path to directory containing the videos:

VIDDIR= os.path.join(DIR, 'Videos')
if not os.path.isdir(VIDDIR):
    raise Exception("ERROR: no video directory found! (expecting '%s')" % VIDDIR)

#read video folder contents one by one, generate frames using ffmpeg and store as frames in the FRAMEDIR
#folder with 3 digit serial extension. eg 001_002



vidlist = sorted(os.listdir(VIDDIR))
vidlist_wo = sorted([os.path.splitext(filename)[0] for filename in os.listdir(VIDDIR)])
for num  in range (len(vidlist)):

    vidname= vidlist[num]
    vidpath = os.path.join(VIDDIR, "%s" % (vidname))

    vidname_wo= vidlist_wo[num]

    framepath= os.path.join(FRAMEDIR, "%s" % (vidname_wo))

    command = 'ffmpeg -i {vidpath}  {framepath}_%03d.png'.format(vidpath=vidpath, framepath=framepath)
    sp.call(command, shell=True)

