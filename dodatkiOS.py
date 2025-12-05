import os

# for el in os.listdir("."):

#     if os.path.isfile(el):
#         print(f"{el} jest plikiem")

#     elif os.path.isdir(el):
#         print(f"{el} jest folderem")

# os.mkdir("pliki")
# os.rmdir("pliki")
os.mkdir("pliki/siema.py") # sprawdzić ścieżke
print(f"c")
print("os.rename('staraNazwa', 'nowaNazwa')")

# os.remove("pliki.py")

path = "pliki/01/dane.txt"
print(f"path:{path}")

print(f"dirname: {os.path.dirname(path)}")
print(f"basename: {os.path.basename(path)}")
print(f"abspath: {os.path.abspath(path)}")


os.makedirs(os.path.dirname("pliki/01/dane.txt"))

with open(path, "w") as plik:
    print(f"stworzono: {path}")