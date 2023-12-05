from pydub import AudioSegment


class WaveModel:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_file(self):
        try:
            open(self.filepath, 'r')
            self.validate()
            if self.filepath[-4::] != ".wav" and self.filepath[-4::] != ".mp3":
                return "Unsupported File Type", False
            return "File Loaded Successfully!", True
        except FileNotFoundError:
            return "File Not Found", False
        except PermissionError:
            return "Cannot Access File, No Permission", False

    def validate(self):
        if self.filepath[-4::] != ".wav":
            temp = AudioSegment.from_mp3(self.filepath)
            temp.export("file.wav", format="wav")
        else:
            self.filepath.export("file.wav", format="wav")

