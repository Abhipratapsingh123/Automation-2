from pathlib import Path

p1=  Path('Segment-3/abc.txt')
if p1.exists():
  with open(p1,'r') as file:
    print(file.read(),"\n")

# To print all the files of a folder

p2 = Path('Segment-2')

for item in p2.iterdir():
  print(item.stem)
  print(item.suffix)
  print(item.name)

