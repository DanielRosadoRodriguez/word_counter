class Reader:
    def __init__(self, file_path):
        self.file_path = file_path 
        self.lines = self.get_lines()

    def get_lines(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return lines
