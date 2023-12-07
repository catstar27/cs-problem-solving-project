from pydub import AudioSegment
from pydub.utils import mediainfo

accepted_filetypes = [".mp3", ".wav"]


class WaveModel:
    """
    Creates and formats the file which will be referenced by all the graphs,
    while handling errors relating to file loading.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.mono_wav_audio = ''
        self.duration = 0

    def load_file(self):
        try:
            open(self.filepath, 'r')
            if self.filepath[-4::].lower() not in accepted_filetypes:
                return "Unsupported File Type", False
            if not self.validate():
                return "FFMPEG Not Installed Correctly", False
            return "File Loaded Successfully!", True
        except FileNotFoundError:
            return "File Not Found", False
        except PermissionError:
            return "Cannot Access File, No Permission", False

    def validate(self):
        try:
            raw_audio = AudioSegment.from_mp3(self.filepath) if self.filepath[-4::].lower() != ".wav" else AudioSegment.from_file(self.filepath)
            mono_wav = raw_audio.set_channels(1)
            mono_wav.export("file.wav", format="wav")
            self.mono_wav_audio = AudioSegment.from_file("file.wav")
            self.duration = round(float(mediainfo("file.wav")["duration"]), 2)
            return True
        except FileNotFoundError:
            return False
