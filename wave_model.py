
class WaveModel:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_file(self):
        try:
            open(self.filepath, 'r')
            self.validate()
            if self.filepath[::4] != ".wav" and self.filepath[::4] != ".mp3":
                return "Unsupported File Type", False
            return "File Loaded Successfully!", True
        except FileNotFoundError:
            return "File Not Found", False
        except PermissionError:
            return "Cannot Access File, No Permission", False

    def validate(self):
        if self.filepath[::4] != ".wav":
            print("Must Convert")

