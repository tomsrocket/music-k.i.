# T.A.M.P. - Tom's A.I. Music Project

Make music with Artificial Intelligence

## Idea 

* Use all the good songs from Ewan Dobson
* Convert them to Midi
* Train some A.I. with it
* Let it predict
* BINGO

## Step 1 - generate a midi

* Start with https://www.youtube.com/watch?v=AAGpXIis8Hk&list=PLCR4YKje4Zfu5hHFek27lG34pwaQ81Pu7&index=22&t=0s
* Convert to mp3 with https://2conv.com
* Convert to midi with https://www.bearaudiotool.com/mp3-to-midi
* Use timidity to listen to it https://wiki.ubuntuusers.de/MIDI/
 
    timidity [filename]

## Results

* Very interesting result! Conversion to midi actually works .. in a way!
* But the midi contains too many crazy notes. 

## Ideas for 1.1

* filter the midi first, with bandpassfilter so only the main melody is left, and cray high notes will not be recognized

# Problems to solve

* Convert the weird binary midi format to pandas array 
* Write a training program, maybe like this: https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/
* If it works, ask Thorben, he has ideas for better and newer ways to predict the music :)

