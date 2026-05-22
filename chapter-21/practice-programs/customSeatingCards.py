#! python3
# customSeatingCards.py - Create Custom Seating Cards for every Guest

from PIL import Image, ImageDraw
from pathlib import Path

guestFile = open(Path.cwd() / 'guests.txt')

guestList = guestFile.readlines()

for guest in guestList:
    noNewLineGuest = guest.rstrip('\n')
    im = Image.open('flower.png')
    draw = ImageDraw.Draw(im)
    draw.rectangle((60,0,348,360),outline='black')
    draw.text((70,340),noNewLineGuest,fill='black')
    im.save(f'seating_Card_{noNewLineGuest}.png')