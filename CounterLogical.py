from Counter import Counter

class CounterLogical(Counter):
    def __init__(self, lines):
        self.lines = lines
        self.logical_lines = self._count_lines()
    
    def _count_lines(self) -> int:
        count = 0
        in_docstring = False
        triple_quotes = ('"""', "'''")
        
        for line in self.lines:
            stripped = line.strip()
            
            # Saltar docstrings
            if in_docstring:
                if any(stripped.endswith(quote) for quote in triple_quotes):
                    in_docstring = False
                continue
            
            if any(stripped.startswith(quote) for quote in triple_quotes):
                in_docstring = True
                continue
            
            # Ignorar líneas vacías y comentarios
            if not stripped or stripped.startswith('#'):
                continue
            
            # Contar imports
            if stripped.startswith(('import ', 'from ')):
                count += 1
                continue
            
            # Contar definiciones de clase
            if stripped.startswith('class '):
                count += 1
                continue
            
            # Contar definiciones de método/función
            if stripped.startswith('def '):
                count += 1
                continue
        
        return count
    
    def get_number_of_lines(self):
        return self.logical_lines