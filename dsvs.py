#Digital Source Video Splicer
"""
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 he Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.

 If this software benefits you directly for more than casual use, although it is certainly not neccessary, I ask that you donate. Please email joelbowalia@gmail.com with any questions. Thank you.

"""


#ffmpeg -f concat -i mylist.txt -c copy output.avi
#ffmpeg -ss [start] -i in.mp4 -t [duration] -c copy out.mp4   TO CUT UP VIDS
#file 'C:\1.avi'
#file 'C:\2.avi'
"""
MAYBE OF USE, LATER
http://superuser.com/questions/138331/using-ffmpeg-to-cut-up-video



As other people mentioned, putting -ss before (much faster) or after (more accurate) the -i makes a big difference. The section "Fast And Accurate Seeking" on the ffmpeg seek page tells you how to get both, and I have used it, and it makes a big difference. Basically you put -ss before AND after the -i, just make sure to leave enough time before where you want to start cutting to have another key frame. Example: If you want to make a 1-minute clip, from 9min0sec to 10min 0sec in Video.mp4, you could do it both quickly and accurately using:

ffmpeg -ss 00:08:00 -i Video.mp4 -ss 00:01:00 -t 00:01:00 -c copy VideoClip.mp4

The first -ss seeks fast to (approximately) 8min0sec, and then the second -ss seeks accurately to 9min0sec, and the -t 00:01:00 takes out a 1min0sec clip.

Also note this important point from that page: "If you use -ss with -c:v copy, the resulting bitstream might end up being choppy, not playable, or out of sync with the audio stream, since ffmpeg is forced to only use/split on i-frames."

This means you need to re-encode the video, even if you want to just copy it, or risk it being choppy and out of sync. You could try just -c copy first, but if the video sucks you'll need to re-do it.

"""


#Libraries & Global Variables
import os
import re
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

global incr
incr = 1

global slices
slices = []

global howmanyparts
howmanyparts= 0

global saved
saved = False

global directory
directory = ''

global ext
ext = 'avi'

global crf
crf = '18'

global preset
preset = 'veryslow'



#Function Section Begin



def combine(*args):
	global directory
	global howmanyparts
	#howmanyparts = 5
	global ext
	global saved
	if directory == '':
		directory = os.getcwd()
	if saved == False:
		getsave()
	parts = []
	for x in range(howmanyparts):
		parts.append(directory + '/out' + str(x+1) + '.' + ext)
		#print(parts)

	f = open('mylist.txt', 'w')
	for x in range(len(parts)):
		f.write('file ' + "'" + parts[x]+ "'" + '\n')

	f.close()






	os.system('ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.' + ext + ' -y')
	os.remove('mylist.txt')

	PCNT.set('100% Done (Output)')
	Tk.update(root)
	#print('-------------------------------')
	#print("DONE")
	#print('-------------------------------')

	#file 'C:\1.avi'
	#file 'C:\2.avi'



def parts(*args):
	global howmanyparts
	global incr
	if (splicer1.get() != ' ' and splicer2.get() != ' ' and splicer3.get() != ' '):
		slices.append(str(int(splicer1.get())))
		slices.append(str(int(splicer2.get())))
		slices.append(str(float(splicer3.get())))
		slices.append(str(int(splicer4.get())))
		slices.append(str(int(splicer5.get())))
		slices.append(str(float(splicer6.get())))


	if incr == 1:
		PARTLABEL1.set('1: From ' + str(int(slices[0])) +  ':' + str(int(slices[1])) + ':' + str(float(slices[2])) + ' to ' + str(int(slices[3])) +  ':' + str(int(slices[4])) + ':' + str(float(slices[5])) + ',')
		howmanyparts += 1
	elif incr == 2:
		PARTLABEL2.set('2: From ' + str(int(slices[6])) +  ':' + str(int(slices[7])) + ':' + str(float(slices[8])) + ' to ' + str(int(slices[9])) +  ':' + str(int(slices[10])) + ':' + str(float(slices[11])) + ',')
		howmanyparts += 1
	elif incr == 3:
		howmanyparts += 1
		PARTLABEL3.set('3: From ' + str(int(slices[12])) +  ':' + str(int(slices[13])) + ':' + str(float(slices[14])) + ' to ' + str(int(slices[15])) +  ':' + str(int(slices[16])) + ':' + str(float(slices[17])) + ',')
	elif incr == 4:
		howmanyparts += 1
		PARTLABEL4.set('4: From ' + str(int(slices[18])) +  ':' + str(int(slices[19])) + ':' + str(float(slices[20])) + ' to ' + str(int(slices[21])) +  ':' + str(int(slices[22])) + ':' + str(float(slices[23])) + ',')
	elif incr == 5:
		howmanyparts += 1
		PARTLABEL5.set('5: From ' + str(int(slices[24])) +  ':' + str(int(slices[25])) + ':' + str(float(slices[26])) + ' to ' + str(int(slices[27])) +  ':' + str(int(slices[28])) + ':' + str(float(slices[29])) + ',')
	elif incr == 6:
		howmanyparts += 1
		PARTLABEL6.set('6: From ' + str(int(slices[30])) +  ':' + str(int(slices[31])) + ':' + str(float(slices[32])) + ' to ' + str(int(slices[33])) +  ':' + str(int(slices[34])) + ':' + str(float(slices[35])) + ',')
	elif incr == 7:
		howmanyparts += 1
		PARTLABEL7.set('7: From ' + str(int(slices[36])) +  ':' + str(int(slices[37])) + ':' + str(float(slices[38])) + ' to ' + str(int(slices[39])) +  ':' + str(int(slices[40])) + ':' + str(float(slices[41])) + ',')
	elif incr == 8:
		howmanyparts += 1
		PARTLABEL8.set('8: From ' + str(int(slices[42])) +  ':' + str(int(slices[43])) + ':' + str(float(slices[44])) + ' to ' + str(int(slices[45])) +  ':' + str(int(slices[46])) + ':' + str(float(slices[47])) + ',')
	elif incr == 9:
		howmanyparts += 1
		PARTLABEL9.set('9: From ' + str(int(slices[48])) +  ':' + str(int(slices[49])) + ':' + str(float(slices[50])) + ' to ' + str(int(slices[51])) +  ':' + str(int(slices[52])) + ':' + str(float(slices[53])) + ',')
	elif incr == 10:
		howmanyparts += 1
		PARTLABEL10.set('10: From ' + str(int(slices[54])) +  ':' + str(int(slices[55])) + ':' + str(float(slices[56])) + ' to ' + str(int(slices[57])) +  ':' + str(int(slices[58])) + ':' + str(float(slices[59])))
	elif incr >= 11:
		howmanyparts += 1


	splicer1.set('0')
	splicer2.set('0')
	splicer3.set('00.00')
	splicer4.set('0')
	splicer5.set('0')
	splicer6.set('00.00 ')



	incr += 1
	#print(splice)
	#Tk.update(root)
	return incr,howmanyparts

def load_file(*args):
	global filename
	global ext
	splicer1.set('0')
	splicer2.set('0')
	splicer3.set('00.00')
	splicer4.set('0')
	splicer5.set('0')
	splicer6.set('00.00')
	thecrf.set('18')
	thepreset.set('slow')
	filename = filedialog.askopenfilename()
	ext = filename[-3:]
	FN.set('File: ' + filename)
	theext.set(ext)
	Tk.update(root)
	return filename,ext

def placeparts(*args):
	global directory
	directory = filedialog.askdirectory()
	os.chdir(directory)
	DN.set('Folder: ' + directory)
	Tk.update(root)
	return directory

def getsave(*args):
	global preset
	preset = thepreset.get()
	global crf
	crf = thecrf.get()
	global saved
	saved = True
	global ext
	ext = theext.get()


	#ffmpeg -ss [start] -i in.mp4 -t [duration] -c copy out.mp4

	#print(slices)
	#print(slices[3])
	#print(len(slices))
	#print('THIS is IT: ' + str((incr-1)))
	slice = 0


	for part in range(incr-1):
		for x in range(len(slices)):#we need them as integers(floats actually?) at first
			slices[x] = float(slices[x])
		to = float(((((slices[slice+3] * 60) + slices[slice+4]) * 60) + slices[slice+5]))
		#print(to)
		start = float(((((slices[slice] * 60) + slices[slice+1]) * 60) + slices[slice+2]))
		#print(start)
		duration = abs(start - to)
		for x in range(len(slices)):#now we need them as strings.
			slices[x] = str(slices[x])
		#print('DUR: ' + str(duration))
		#print('ffmpeg -ss ' + slices[slice] + ':' + slices[slice+1] + ':' + slices[slice+2] + ' ' + '-i ' + filename + ' -t ' + str(duration) + ' ' + '-c copy out'+str(part+1) + '.' + ext)
		#print(slices[slice])
		#print(slices[slice+1])
		#print(int(float(slices[slice])))
		#print(int(float(slices[slice+1])))
		#print('ffmpeg -ss ' + str(int(float(slices[slice]))) + ':' + str(int(float(slices[slice+1]))) + ':' + slices[slice+2] + ' ' + '-i ' + filename + ' -t ' + str(duration) + ' ' + '-c copy out'+str(part+1) + '.' + ext)
		PCNT.set(str(int((part*100)/(incr-1))) + '% Done    Working ...')
		Tk.update(root)


		#OLD METHOD BELOW
		#ffmpeg -ss [start] -i in.mp4 -t [duration] -c copy out.mp4
		#os.system('ffmpeg -ss ' + str(int(float(slices[slice]))) + ':' + str(int(float(slices[slice+1]))) + ':' + slices[slice+2] + ' ' + '-i ' + filename + ' -t ' + str(duration) + ' ' + '-c copy out'+str(part+1) + '.' + ext + ' -y')


		#NEW METHOD BELOW
		#print('ffmpeg -ss 00:08:00 -i Video.mp4 -ss 00:01:00 -t 00:01:00 -c copy VideoClip.mp4')
		#print('ffmpeg -ss 00:00:00 '+ '-i ' + filename + ' -ss ' + str(int(float(slices[slice]))) + ':' + str(int(float(slices[slice+1]))) + ':' + slices[slice+2] + ' -t ' + str(duration) + ' ' + '-c copy out' +str(part+1) + '.' + ext + ' -y')
		#os.system('ffmpeg -ss 00:00:00 '+ '-i ' + filename + ' -ss ' + str(int(float(slices[slice]))) + ':' + str(int(float(slices[slice+1]))) + ':' + slices[slice+2] + ' -t ' + str(duration) + ' ' + '-c copy out'+str(part+1) + '.' + ext + ' -y')

		#BEST METHOD YET
		#https://trac.ffmpeg.org/wiki/Encode/H.264
		print('ffmpeg -ss 00:00:00 '+ '-i ' + filename + ' -ss ' + str(int(float(slices[slice]))) + ':' + str(int(float(slices[slice+1]))) + ':' + slices[slice+2] + ' -t ' + str(duration) + ' ' + '-c:v libx264 -preset ' + preset + ' -crf ' + crf  + ' -c:a copy ' + 'out'+ str(part+1) + '.' + ext + ' -y')
		os.system('ffmpeg -ss 00:00:00 '+ '-i ' + filename + ' -ss ' + str(int(float(slices[slice]))) + ':' + str(int(float(slices[slice+1]))) + ':' + slices[slice+2] + ' -t ' + str(duration) + ' ' + '-c:v libx264 -preset ' + preset + ' -crf ' + crf  + ' -c:a copy ' + 'out'+ str(part+1) + '.' + ext + ' -y')


		slice += 6


	PCNT.set('Parts Saved (Out1, Out2, etc...)')
	return ext,saved

def validateTextInputSize(event):
	#print(event)
	global MAXINPUTSIZE
	if (event.widget.index(END) >= MAXINPUTSIZE - 1):
		event.widget.delete(MAXINPUTSIZE - 1)





























#Function Section End


#Gui Section Begin
#EVERYTHING BELOW THIS IS A LOOP! IF YOU WANT TO SET SOMETHING(A LABEL PERHAPS THAT WILL CHANGE) DO SO ABOVE!
root = Tk() # Establishing a root window?
root.title("Digital Source Video Splicer") # Obviously this names it
root.minsize(350,350)






MAXINPUTSIZE = 10

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0,  sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#ttk.Label(mainframe, text="Insert URL into the first textbox, the directory to be downloaded into in the second textbox, and then click Download").grid(column=1, row=1, sticky=N)


ttk.Button(mainframe, text="Combine Parts", command=combine).grid(column=10, row=2000, columnspan=1,rowspan=1,  sticky=(S,W))
ttk.Button(mainframe, text="Save Parts", command=getsave).grid(column=15, row=2000,columnspan=1,rowspan=1,    sticky=(S,W))
ttk.Button(mainframe, text="Add Part", command=parts).grid(column=12, row=0,columnspan=1,rowspan=1,   sticky=W)#done
ttk.Button(mainframe, text="Open File", command=load_file).grid(column=10, row=0,columnspan=1, rowspan=1,  sticky=W)#done
ttk.Button(mainframe, text="Select Folder", command=placeparts).grid(column=11, row=0,columnspan=1,rowspan=1,   sticky=W) #done


CRFL = StringVar()
CRFL.set('CRF: ')
ttk.Label(mainframe, textvariable=CRFL).grid(column=11, row=2100, columnspan=5, sticky=(S,E))

thecrf = StringVar() #Erm, Setting it to a string variable?
thecrf_entry = ttk.Entry(mainframe, width=2, textvariable=thecrf)
thecrf_entry.grid(column=17,row=2100,  sticky=(S,E)) #sticky = (N,W,E) or sticky = N


EXTL = StringVar()
EXTL.set('EXT: ')
ttk.Label(mainframe, textvariable=EXTL).grid(column=11, row=2200, columnspan=5, sticky=(S,E))

theext = StringVar() #Erm, Setting it to a string variable?
theext_entry = ttk.Entry(mainframe, width=4, textvariable=theext)
theext_entry.grid(column=17,row=2200,  sticky=(S,E)) #sticky = (N,W,E) or sticky = N




PRESETL = StringVar()
PRESETL.set('Preset:')
ttk.Label(mainframe, textvariable=PRESETL).grid(column=10, row=2100, columnspan=8, sticky=(S,W))

thepreset = StringVar() #Erm, Setting it to a string variable?
thepreset_entry = ttk.Entry(mainframe, width=10, textvariable=thepreset)
thepreset_entry.grid(column=10,row=2200,  sticky=(S,W)) #sticky = (N,W,E) or sticky = N




HRLABEL= StringVar()
HRLABEL.set('HR:MN:SD')
ttk.Label(mainframe, textvariable=HRLABEL).grid(column=1, row=0, columnspan=9, sticky=(N,W))

HRLABEL2= StringVar()
HRLABEL2.set('HR:MN:SD')
ttk.Label(mainframe, textvariable=HRLABEL2).grid(column=13, row=0, columnspan=9, sticky=(N,W))


#HOURS
splicer1 = StringVar() #Erm, Setting it to a string variable?
splicer1_entry = ttk.Entry(mainframe, width=2, textvariable=splicer1)
splicer1_entry.grid(column=5,row=(2),  sticky=(N,W)) #sticky = (N,W,E) or sticky = N


#MINUTES
splicer2 = StringVar() #Erm, Setting it to a string variable?
splicer2_entry = ttk.Entry(mainframe, width=2, textvariable=splicer2)
splicer2_entry.grid(column=6,row=(2),  sticky=(N,W)) #sticky = (N,W,E) or sticky = N

#SECONDS
splicer3 = StringVar() #Erm, Setting it to a string variable?
splicer3_entry = ttk.Entry(mainframe, width=5, textvariable=splicer3)
splicer3_entry.grid(column=7,row=(2), sticky=(N,W)) #sticky = (N,W,E) or sticky = N




#TO
TO = StringVar()
TO.set('---To------------------------------------------>')
ttk.Label(mainframe, textvariable=TO).grid(column=10, row=2, sticky=(S,W))

WARN = StringVar()
WARN.set("WARNING: Replace any spaces in files/folders with an '_'")
ttk.Label(mainframe, textvariable=WARN).grid(column=10, row=1, sticky=(S,W))





#HOURS
splicer4 = StringVar() #Erm, Setting it to a string variable?
splicer4_entry = ttk.Entry(mainframe, width=2, textvariable=splicer4)
splicer4_entry.grid(column=13,row=(2), columnspan=1, sticky=(N,W)) #sticky = (N,W,E) or sticky = N

#MINUTES
splicer5 = StringVar() #Erm, Setting it to a string variable?
splicer5_entry = ttk.Entry(mainframe, width=2, textvariable=splicer5)
splicer5_entry.grid(column=14,row=(2),columnspan=1,  sticky=(N,W)) #sticky = (N,W,E) or sticky = N

#SECONDS
splicer6 = StringVar() #Erm, Setting it to a string variable?
splicer6_entry = ttk.Entry(mainframe, width=5, textvariable=splicer6)
splicer6_entry.grid(column=15,row=(2),columnspan=1, sticky=(N,W)) #sticky = (N,W,E) or sticky = N


FN = StringVar()
ttk.Label(mainframe, textvariable=FN).grid(column=10, row=200, sticky=(S,W))

DN = StringVar()
ttk.Label(mainframe, textvariable=DN).grid(column=10, row=400, sticky=(S,W))

PARTLABEL = StringVar()
PARTLABEL.set('---------PARTS------------------------')
ttk.Label(mainframe, textvariable=PARTLABEL).grid(column=10, row=450, sticky=(S,W))

#--LABELS TO BE FILLED IN. 10 label parts is fine. program still works after 10
PARTLABEL1 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL1).grid(column=10, row=470, sticky=(S,W))

PARTLABEL2 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL2).grid(column=10, row=490, sticky=(S,W))

PARTLABEL3 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL3).grid(column=10, row=510, sticky=(S,W))

PARTLABEL4 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL4).grid(column=10, row=530, sticky=(S,W))

PARTLABEL5 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL5).grid(column=10, row=550, sticky=(S,W))

PARTLABEL6 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL6).grid(column=10, row=570, sticky=(S,W))

PARTLABEL7 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL7).grid(column=10, row=590, sticky=(S,W))

PARTLABEL8 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL8).grid(column=10, row=610, sticky=(S,W))

PARTLABEL9 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL9).grid(column=10, row=630, sticky=(S,W))

PARTLABEL10 = StringVar()
ttk.Label(mainframe, textvariable=PARTLABEL10).grid(column=10, row=650, sticky=(S,W))

PARTLABEL11= StringVar()
PARTLABEL11.set('Only 10 parts displayed, but infinite possible.')
ttk.Label(mainframe, textvariable=PARTLABEL11).grid(column=10, row=670, sticky=(S,W))

PCNT = StringVar()
ttk.Label(mainframe, textvariable=PCNT).grid(column=11, row=2000, sticky=(S,W))



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5) #"walks through all of the widgets that are children of our content frame, and adds a little bit of padding around each, so they aren't so scrunched together. We could have added these options to each "grid" call"



root.bind('<Return>', combine)
root.bind("<Key>", validateTextInputSize)

root.mainloop() #Won't draw without this
#gui section end
