import py_midicsv

# Load the MIDI file and parse it into CSV format
csv_string = py_midicsv.midi_to_csv("bla32.mid")
print(csv_string)

filee = open("testfile32.csv","w") 
 
filee.write(''.join(csv_string)) 
 
filee.close() 


# Parse the CSV output of the previous command back into a MIDI file
#midi_object = py_midicsv.csv_to_midi(csv_string)

# Save the parsed MIDI file to disk
#with open("example_converted.csv", "wb") as output_file:
#    midi_writer = py_midicsv.FileWriter(output_file)
#    midi_writer.write(midi_object)
