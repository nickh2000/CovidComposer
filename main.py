
ronaFile = open("rona.txt", "r")

ronaString = "" #start our string of the bases

for line in ronaFile.readlines(): #go through each line
	words = line.split() #create a list of words in the line
	del words[0] #get rid of the numbers at the beginning of the line
	ronaString += "".join(words) #put all the bases into our string




import mido #library for creating MIDI files
import random #library for using random numbers

file = mido.MidiFile() #create a new MIDI file
track = mido.MidiTrack() #create a new MIDI channel


#pair the nucleobases adedine, thymine, cytosine, and guanine to C, D, E, and G respectively
conversion = {"a": 60, "t": 62, 'c': 64, 'g': 67}


for base in ronaString: #go through each nucleobase

	note = conversion[base] #get the note corresponding to the base
	
	on = mido.Message("note_on", velocity = random.randrange(0, 127), note = note) #create a Note-On MIDI message for our base
	track.append(on) #add MIDI message to our track
	
	off = mido.Message("note_off", time=random.randrange(50,500, 50), note=note) #Note-Off MIDI message gets exectuted after random amount of time
	track.append(off) #add MIDI message to our track


file.tracks.append(track) #add the track to our MIDI FIle
file.save("rona.mid") #save our MIDI file as "rona.mid"




