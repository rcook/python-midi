# Hacking MIDI with Python

## References

* [Standard MIDI file format specification 1.1][midi-file-format]
* [MIDIUtil][midiutil]
* [Mido][mido]

## Set up

```
pip3 install --user MIDIUtil
pip3 install --user mido
```

## Play generated MIDI files

```
fluidsynth -i /usr/local/Cellar/fluid-synth/2.1.7/share/fluid-synth/sf2/VintageDreamsWaves-v2.sf2 file.mid
```

[midi-file-format]: http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html
[midiutil]: https://midiutil.readthedocs.io/en/1.2.1/
[mido]: https://mido.readthedocs.io/en/latest/
