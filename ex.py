from midiutil import MIDIFile

# Cria um arquivo MIDI com uma única faixa
midi = MIDIFile(1)

# Configuração da faixa
track = 0
time = 0  # Começa no tempo 0
channel = 0
tempo = 120  # BPM
volume = 100  # Volume (0-127)

# Adiciona informações da faixa e do tempo
midi.addTrackName(track, time, "Track 1")
midi.addTempo(track, time, tempo)

# Função para converter notas para números MIDI
def note_to_midi(note):
    note_mapping = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
    octave = int(note[-1])  # Pega a oitava, ex: "4" de "C4"
    base_note = note_mapping[note[0]]  # Nota base (ex: C -> 0)
    if "#" in note:  # Se tiver sustenido
        base_note += 1
    elif "b" in note:  # Se tiver bemol
        base_note -= 1
    return (octave + 1) * 12 + base_note  # Calcula o número MIDI

# Define um acorde (exemplo: C maior = C4, E4, G4)
chord = ["C4", "E4", "G4"]  # Notas do acorde
duration = 2  # Duração do acorde em beats

# Adiciona todas as notas do acorde no mesmo instante
for note in chord:
    pitch = note_to_midi(note)
    midi.addNote(track, channel, pitch, time, duration, volume)

# Salva o arquivo MIDI
with open("chord_example.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("Arquivo MIDI 'chord_example.mid' criado com sucesso!")
