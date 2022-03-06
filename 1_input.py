import pygame.midi
from midiutil.MidiFile import MIDIFile
import pygame

pressed = []
state = False

def readInput(input_device, channel):
    count = 0
    degrees =[] # MIDI note number
    while True:
        if input_device.poll():
            event = input_device.read(1)[0] # [state, note(음), velocity(속도), something(always 0 for me)]
            print(event)
            print("//")
            data = event[0]
            print(data)
            timestamp = event[1]
            note = event[0][1]
            print(note)
            degrees.append(event[0][1])
            count += 1
            '''' # [state, note, velocity, something(always 0 for me)]
            if data[0] == 128 + channel:  # note off on channel data[0]-128
                if data[1] in pressed:
                    pressed.remove(data[1])
            if data[0] == 144 + channel:  # note on on channel data[0]-144
                if not data[1] in pressed:
                    pressed.append(data[1])

            if all(el in pressed for el in [36, 40, 43, 46]):
                print("chord = Cmaj7")
                '''
        if count == 10 :
            print(degrees)
            midi_generator(degrees)
            break

def midi_generator(degrees) : #https://midiutil.readthedocs.io/en/1.2.1/를 들어가서 git clone 후 setup.py 설치 요망
    # degrees = [] # MIDI note number
    track = 0
    channel = 1 # piano
    time = 0  # In beats
    duration = 1  # In beats
    tempo = 60  # In BPM
    volume = 100  # 0-127, as per the MIDI standard
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track
    # automatically created)
    MyMIDI.addTempo(track, time, tempo)
    for pitch in degrees:
        MyMIDI.addNote(track, channel, pitch, time, duration, volume)
        time = time + 1
    with open("major-scale.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)
    print("done!")

#def midi_saver(result) :

if __name__ == '__main__':
    pygame.midi.init()
    my_input = pygame.midi.Input(1)
    readInput(my_input,0)
    pygame.init()
    pygame.mixer.music.load("major-scale.mid")
    pygame.mixer.music.set_volume(0.8)
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024  # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)
    try:
        pygame.mixer.music.load("major-scale.mid")
        print("Music file {} loaded!".format("major-scale.mid"))
    except pygame.error:
        print("File {} not found! {}".format("major-scale.mid", pygame.get_error()))
    pygame.midi.quit()