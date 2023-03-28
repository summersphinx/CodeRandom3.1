from pygame import mixer
from random import choice as r
from os import listdir
import cr3

sett = cr3.Settings()
path = cr3.path + 'audio/'

songs = listdir(path+'music')

print(songs)

mixer.init(channels=3)

bg = mixer.Channel(0)
sfx = mixer.Channel(1)
voice = mixer.Channel(2)

bg.set_volume(float(sett.music_vol))
voice.set_volume(float(sett.voice_vol))
sfx.set_volume(float(sett.sfx_vol))


def Play(sound=None):
    if not bg.get_busy():
        print(r(songs))
        bg.play(mixer.Sound(f'{path}/music/{r(songs)}'), loops=3)
    elif sound is None:
        bg.stop()
        bg.play(mixer.Sound(f'{path}/music/{r(songs)}'))
    else:
        bg.stop()
        bg.play(mixer.Sound(f'{path}/music/{sound}.mp3'))


def Voice(file=None, tts=None):
    pass


def SFX(sound):
    pass


def Volume():
    sett = cr3.Settings()
    bg.set_volume(float(sett.music_vol))
    voice.set_volume(float(sett.voice_vol))
    sfx.set_volume(float(sett.sfx_vol))

