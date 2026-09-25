# 10-3. Simpler Code: The program file_reader.py in this section uses a temporary variable, lines, to show how splitlines() works. You can skip the temporary variable and loop directly over the list that splitlines() returns:
# for line in contents.splitlines():
# Remove the temporary variable from each of the programs in this section, to make them more concise.

from pathlib import Path



for line in Path.read_text(Path("1_Basics/10_Files_And_Exceptions/learning_python.txt")).splitlines():
    if line:
        print(line.replace("pyhon", "C"))