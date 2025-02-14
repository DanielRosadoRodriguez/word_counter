from CounterPhysical import CounterPhysical
from CounterLogical import CounterLogical
from Reader import Reader

class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lines = Reader(self.file_path).lines
        self.logical_lines = CounterLogical(self.lines).get_number_of_lines()
        self.physical_lines = CounterPhysical(self.lines).get_number_of_lines()
        
    def get_formatted_metrics(self):
        return (f"El archivo: {self.file_path}.\n" 
                        "Cuenta con las siguientes métricas:\n"
                        f"Líneas Físicas: {self.physical_lines}\n" 
                        f"Líneas Lógicas: {self.logical_lines}"
                        )
