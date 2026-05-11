import struct
from .gui import path_of_file_to_upload ,output

def char_to_val(char):
    mapping = {
        " ": 235, ".": 215, ":": 190, "-": 170, "=": 150,
        "+": 130, "*": 110, "#": 90, "%": 70, "@": 50, "$": 20
    }
    return mapping.get(char, 0)

with open(path_of_file_to_upload, "r") as f :
    ascii_rows = list(reversed(f.readlines()))

height = len(ascii_rows)
width = len(ascii_rows[0].strip())
padding = (4 - (width * 3 % 4)) % 4
pixel_data_size = (width * 3 + padding) * height

with open(output, "wb") as f:
    f.write(b'BM') 
    f.write(struct.pack("<L", 54 + pixel_data_size))
    f.write(b'\x00\x00\x00\x00')
    f.write(struct.pack("<i", width))
    f.write(struct.pack("<i", height))
    f.write(struct.pack("<H", 1))
    f.write(struct.pack("<H", 24))
    f.write(struct.pack("<L", 0))
    f.write(struct.pack("<L", pixel_data_size))
    f.write(struct.pack("<i", 2835))
    f.write(struct.pack("<i", 2835))
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')

    for row in ascii_rows:
        clean_row = row.strip()
        for char in clean_row:
            val = char_to_val(char)
            f.write(struct.pack("BBB", val, val, val))

        f.write(b'\x00' * padding)