from pydub import AudioSegment
from pydub.utils import mediainfo

accepted_filetypes = [".mp3", ".wav"]


class WaveModel:
    def __init__(self, filepath):
        self.filepath = filepath
        self.mono_wav_audio = ''
        self.duration = 0

    def load_file(self):
        if self.filepath[-4::] not in accepted_filetypes:
            return "Unsupported File Type", False
        try:
            open(self.filepath, 'r')
            self.validate()
            return "File Loaded Successfully!", True
        except FileNotFoundError:
            return "File Not Found", False
        except PermissionError:
            return "Cannot Access File, No Permission", False

    def validate(self):
        mono_wav = AudioSegment.from_mp3(self.filepath) if self.filepath[-4::] != ".wav" else AudioSegment.from_file(self.filepath)
        mono_wav.set_channels(1)
        mono_wav.export("file.wav", format="wav")
        self.mono_wav_audio = AudioSegment.from_file("file.wav")
        self.duration = round(float(mediainfo("file.wav")["duration"]), 2)
