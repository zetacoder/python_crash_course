str_filename = "Name Of the File.txt"

str_output = f"Filename without suffix {str_filename.removesuffix(".txt")}.\nFilename without prefix is {str_filename.removeprefix("Name Of the File.")}."

print(str_output)