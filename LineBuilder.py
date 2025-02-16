import re
from Line import Line

class LineBuilder:
    def __init__(self, raw_lines: list[str]):
        self._raw_lines: list[str] = raw_lines
        self._built_lines: list[Line] = self._build_lines()

    def _build_lines(self) -> list[Line]:
        result: list[Line] = []
        i: int = 0
        while i < len(self._raw_lines):
            line: str = self._raw_lines[i]
            stripped: str = line.strip()
            if self._is_method_signature(stripped):
                result.append(Line("method signature", 1, 1))
            elif self._is_import_line(stripped):
                result.append(Line("import",1, 1))
            elif self._is_class(stripped):
                result.append(Line("class", 1, 1))
            elif self._is_global_variable(stripped):
                result.append(Line("global variable", 1, 1))
            i += 1
        return result
    
    def _is_import_line(self, stripped: str) -> bool:
        starts_with_import: bool = stripped.startswith("import")
        starts_with_from: bool = stripped.startswith("from")
        return starts_with_import or starts_with_from

    def _is_class(self, stripped: str) -> bool:
        return stripped.startswith("class")

    def _is_method_signature(self, stripped: str) -> bool:
        return stripped.startswith("def ")
    
    def _is_global_variable(self, stripped: str) -> bool:
        pattern:re.Pattern = r'^[a-zA-Z_]\w*\s*(?::\s*\w+\s*)?=(?!=)'
        return bool(re.match(pattern, stripped))

    def get_built_lines(self) -> list[Line]:
        return self._built_lines
