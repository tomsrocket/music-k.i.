# T.A.M.P. - Tom's A.I. Music Project

Make music with Artificial Intelligence

## Idea 

* Use all the good songs from Ewan Dobson
* Convert them to Midi
* Train some A.I. with it
* Let it predict
* BINGO

## Version 1 

* Start with https://www.youtube.com/watch?v=AAGpXIis8Hk&list=PLCR4YKje4Zfu5hHFek27lG34pwaQ81Pu7&index=22&t=0s
* Convert to mp3 with https://2conv.com
* Convert to midi with https://www.bearaudiotool.com/mp3-to-midi
* Use timidity to listen to it https://wiki.ubuntuusers.de/MIDI/
 
    timidity [filename]

## Results

* Very interesting result! Conversion to midi actually works .. in a way!
* But the midi contains too many crazy notes. 

## Version 1.1

* filter the midi first, with bandpassfilter so only the main melody is left, and crazy high notes will not be recognized
* Use a  mp3 to midi converter that runs locally on ubuntu. Found "Waon". 
* Convert midi to csv

First, install waon as described here: https://askubuntu.com/questions/1004500/trouble-installing-waon-ubuntu-16-04

### Commands

    # shorten the mp3
    ffmpeg -i some.mp3 -ss 00:00:00 -to 00:00:20  test.mp3

    # filter some frequencies
    ffmpeg -i test.mp3 -filter:a bandpass=f=440:width_type=q:w=1.1 test32.mp3

    # convert to wav (waon understands only wav)
    ffmpeg -i test.mp3 output.wav 

    # convert to midi
    ./WaoN/waon -i output.wav -o bla.mid

    # install midi to csv
    pip3 install py-midicsv

    # run midi2csv
    python3 convert-midi.py

# Status after Version 1.1

* Better, but still too many notes. 
* Maybe try different bandpass filter, 
* or change settings of waon (has quite some command line options)
* or try different song(s)

# Next version

* Convert the weird binary midi format to pandas array 
* Write a training program, maybe like this: https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/
* If it works, ask Thorben, he has ideas for better and newer ways to predict the music :)
