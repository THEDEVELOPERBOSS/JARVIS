import librosa
import numpy as np
# file path is path to .wav audio file
def load_audio(file_path, sr=16000): # sr(sampling rate) = 16000 is 16kHz standard for speech
    """Load an audio file as a waveform."""
    y, = librosa.load(file_path, sr=sr) # librosa.load reads the audio file and resamples it to 16,000 Hz 
    return y # y is the raw audio waveform

def extract_mfcc(y, sr=16000, n_mfcc=13): 
    """Extract MFCC features from waveform"""
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfcc.T # shape: (frames, features)