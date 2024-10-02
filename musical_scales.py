#Define the chromatic scale for sharp keys.
chromatic_sharp = ('A', 'A#', 'B', 'C', 'C#', 'D', 
                   'D#', 'E', 'F', 'F#', 'G', 'G#')

#Define the chromatic scale for flat keys.
chromatic_flat = ('A', 'Bb', 'B', 'C', 'Db', 'D', 
                  'Eb', 'E', 'F', 'Gb', 'G', 'Ab')

#Define the steps of the major scale
whole_step = 2
half_step = 1
major_scale_steps = [whole_step, whole_step, half_step, whole_step,
	whole_step, whole_step, half_step]

print("What Major Scale would you like to spell?\n" 
    "Type the root note and press [Enter]")

start_note = input("Root: ")
start_note = start_note.title()
chord_functions = ['I', 'ii', 'iii', 'IV', 'V' , 'vi ', 'vii', 'I']

chromatic = []
if 'b' in start_note or 'F' in start_note:
    index_of_start = chromatic_flat.index(start_note)
    for scale in chromatic_flat[index_of_start:] + chromatic_flat[ :index_of_start]:
	    chromatic.append(scale)
else:
    index_of_start = chromatic_sharp.index(start_note)
    for scale in chromatic_sharp[index_of_start:] + chromatic_sharp[ :index_of_start]:
        chromatic.append(scale)

   
#Add the start note to the end to make an octave.
chromatic.append(start_note)

#print the function of the notes.
for func in chord_functions:
	print(f"{func} ", end='     ')
print('\n')

#print the root then the scale.
print(start_note, end=' ')
for x in major_scale_steps:
	print(f"      {chromatic[x]}", end=' ')
	
	if x == 2:
		chromatic.pop(0)
		chromatic.pop(0)
	else:
		chromatic.pop(0)
		
print()
		
