import wav
import numpy as np

audio_file = "./original_book_36min.wav"
frame_size = 1000
threadhold = 1e-3

signal, sample_rate = wav.read_wav(audio_file)

num_of_frame, left_over = divmod(len(signal), frame_size)

output = []
for i in range(num_of_frame):
    current_frame = signal[i*frame_size:(i+1)*frame_size]
    energy = np.sum(np.square(current_frame))
    if energy >= threadhold:
        output.extend(current_frame.tolist())

if left_over != 0:
    current_frame = signal[num_of_frame*frame_size:]
    energy = np.sum(np.square(current_frame))
    if energy >= threadhold:
        output.extend(current_frame.tolist())

wav.write_wav(output, audio_file.replace(".wav", "_eliminated.wav"), sample_rate)