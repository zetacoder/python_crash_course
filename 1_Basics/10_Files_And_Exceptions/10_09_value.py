# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.

from pathlib import Path

try:

    path_catsfile = Path("1_Basics/10_Files_And_Exceptions/data_files/cats.txt")

    path_dogsfile = Path("1_Basics/10_Files_And_Exceptions/data_files/dogs.txt")

    content_catsfile = path_catsfile.read_text()

    content_dogsfile = path_dogsfile.read_text()

    print("Content of Cats file is: \n", content_catsfile)

    print("Content of Dogs file is: \n", content_dogsfile)

except FileNotFoundError:

    pass