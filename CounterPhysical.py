from Counter import Counter

class CounterPhysical(Counter):
   def __init__(self, lines): 
       self.lines = lines
       self.logical_lines = self._count_lines()
   
   def _count_lines(self) -> int:
       logical = 0
       in_docstring = False
       triple_quotes = ('"""', "'''")
       
       for line in self.lines:
           stripped = line.strip()
           
           # Manejar docstrings multilínea
           if in_docstring:
               if any(stripped.endswith(quote) for quote in triple_quotes):
                   in_docstring = False
               continue
           
           # Detectar inicio de docstring    
           if any(stripped.startswith(quote) for quote in triple_quotes):
               in_docstring = True
               # Si la docstring termina en la misma línea
               if any(stripped.endswith(quote) and len(stripped) > len(quote) 
                     for quote in triple_quotes):
                   in_docstring = False
               continue
           
           # Ignorar líneas en blanco y comentarios
           if not stripped or stripped.startswith('#'):
               continue
           
           logical += 1
       
       return logical
   
   def is_ignorable(self, line: str) -> bool:
       stripped = line.strip()
       return not stripped or stripped.startswith('#')
   
   def get_number_of_lines(self):
       return self.logical_lines
