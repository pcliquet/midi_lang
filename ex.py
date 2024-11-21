from midiutil import MIDIFile

# Initialize MIDI file
midi = MIDIFile(1)  # Single track
track = 0
current_time = 0  # Start time in beats
channel = 0
default_velocity = 100
current_tempo = 120  # Default tempo in BPM

# Function to calculate note duration in seconds based on tempo
def duration_in_seconds(duration_in_beats, tempo):
    seconds_per_beat = 60 / tempo
    return duration_in_beats * seconds_per_beat

# Function to convert note names to MIDI pitch numbers
def note_to_midi(note):
    note_mapping = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
    octave = int(note[-1])
    base_note = note_mapping[note[0]]
    if "#" in note:
        base_note += 1
    elif "b" in note:
        base_note -= 1
    return (octave + 1) * 12 + base_note

# Parse AST (Example)
ast = [
    {"command": "tempo", "value": 120},
    {"command": "play", "note": "C4", "duration": 4, "velocity": 100},
    {"command": "play", "note": "E4", "duration": 2, "velocity": 80},
    {"command": "play", "note": "G4", "duration": 1, "velocity": 90}
]

# Process AST
for node in ast:
    if node["command"] == "tempo":
        current_tempo = node["value"]
    elif node["command"] == "play":
        # Get note information
        pitch = note_to_midi(node["note"])
        duration_in_beats = node["duration"]
        velocity = node.get("velocity", default_velocity)
        
        # Add the note to the MIDI file
        midi.addNote(track, channel, pitch, current_time, duration_in_beats, velocity)
        
        # Increment the current time based on the duration
        current_time += duration_in_beats

# Save the MIDI file
with open("output.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("MIDI file 'output.mid' created successfully!")
