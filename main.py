from File import CodeFile

file_path = "my_file.py"
mi_archivo = CodeFile(file_path)

print(mi_archivo.get_formatted_metrics())
