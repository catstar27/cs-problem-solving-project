
class WaveModel:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_file(self):
        print(self.filepath)
        try:
            with open(self.filepath, 'r') as f:
                return "File Loaded Successfully!", True
        except FileNotFoundError:
            return "File Not Found", False
        except PermissionError:
            return "Cannot Access File, No Permission", False
