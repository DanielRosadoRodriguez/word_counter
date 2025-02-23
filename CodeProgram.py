import os
from CodeFile import CodeFile

class CodeProgram:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.code_files = self._load_code_files()
        self.physical_lines = self.total_physical_lines()
        self.logical_lines = self.total_logical_lines()
    
    def _load_code_files(self):
        code_files = []
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    code_files.append(CodeFile(file_path))
        return code_files
    
    def total_physical_lines(self):
        return sum(code_file._physical_lines for code_file in self.code_files)
    
    def total_logical_lines(self):
        return sum(code_file._logical_lines for code_file in self.code_files)
    
    def report(self):
        return {
            "total_physical_lines": self.physical_lines,
            "total_logical_lines": self.logical_lines,
            "files_analyzed": len(self.code_files)
        }
    
    def __str__(self) -> str:
        return (
            f"The folder: {self.folder_path}\n"
            "Contains the following metrics:\n"
            f"Total Physical Lines: {self.physical_lines}\n"
            f"Total Logical Lines: {self.logical_lines}\n"
            f"Files Analyzed: {len(self.code_files)}"
        )
