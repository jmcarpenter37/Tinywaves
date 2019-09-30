import sys
import os
import math
sys.path.append(os.path.join(os.getcwd(),'python'))
# All the sounds are located here:
# http://folk.uio.no/oyvindry/applinalg/sounds/
# Sound pressure and decibals

def DecibelConversion(sound_array):
    # It is common to relate a given sound pressure to the smallest sound pressure
    # that can be perceived, as level onm the decibel scale
    sound_ref = 0.00002 #Pa
    dec = 20*math.log10( sound_array / sound_ref)
    return dec # Returns the sound you pass into decibels. We also can express this as "How much power the sound has"




def main():
    print("done")



if __name__ == '__main__':
    main()
