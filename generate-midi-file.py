#!/usr/bin/env python3
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    p0 = subparsers.add_parser(name="midiutil")
    p0.set_defaults(func=generate_with_midiutil)
    p0.add_argument("file_name", metavar="FILE-NAME")

    p1 = subparsers.add_parser(name="mido")
    p1.set_defaults(func=generate_with_mido)
    p1.add_argument("file_name", metavar="FILE-NAME")

    args = parser.parse_args()
    args.func(args)


def dump_midi_file(file_name):
    from mido import MidiFile

    f = MidiFile(file_name)
    f.print_tracks()


def generate_with_midiutil(args):
    from midiutil.MidiFile import MIDIFile

    # Create MIDI file with 1 track
    midi = MIDIFile(1)
    track = 0

    # Implicitly creates track 0 for metainformation
    midi.addTrackName(track, 0, "Sample Track")
    midi.addTempo(track, 0, 120)

    # And track 1 for notes
    for beat, note in enumerate([60, 62, 64, 65]):
        midi.addNote(track=track, channel=0, pitch=note,
                     time=beat, duration=1, volume=100)

    with open(args.file_name, "wb") as f:
        midi.writeFile(f)


def generate_with_mido(args):
    from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo

    ticks_per_beat = 960

    def add_note(track, note, velocity):
        track.append(Message("note_on", note=note,
                             velocity=velocity, time=0))
        track.append(Message("note_off", note=note,
                             velocity=velocity, time=ticks_per_beat))

    f = MidiFile(ticks_per_beat=960)

    # Tempo track
    t = MidiTrack()
    f.tracks.append(t)
    t.append(MetaMessage("set_tempo", tempo=bpm2tempo(120)))
    t.append(MetaMessage("end_of_track"))

    # Note track
    t = MidiTrack()
    f.tracks.append(t)
    t.append(MetaMessage("track_name", name="Sample Track"))
    for _, note in enumerate([60, 62, 64, 65]):
        add_note(track=t, note=note, velocity=100)

    f.save(args.file_name)


if __name__ == "__main__":
    main()
