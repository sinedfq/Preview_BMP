import struct
import tkinter as tk
from PIL import Image, ImageTk


def read_bmp(filename):
    with open(filename, 'rb') as f:
        bmp_header = f.read(14)
        dib_header = f.read(40)

        width = struct.unpack('<I', dib_header[4:8])[0]
        height = struct.unpack('<i', dib_header[8:12])[0]  # Signed integer for height
        bits_per_pixel = struct.unpack('<H', dib_header[14:16])[0]

        row_size = ((width * bits_per_pixel + 31) // 32) * 4
        palette = None

        if bits_per_pixel == 8:
            palette = f.read(1024)  # 256 colors * 4 bytes per entry (RGBA)

        pixel_data = [f.read(row_size) for _ in range(abs(height))]

    return width, height, bits_per_pixel, palette, pixel_data


def display_bmp(filename):
    width, height, bits_per_pixel, palette, pixel_data = read_bmp(filename)

    root = tk.Tk()
    root.title("BMP Viewer")

    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)

    canvas.create_image(0, 0, anchor=tk.NW, image=img)

    root.mainloop()


if __name__ == "__main__":
    input_bmp_file = "Images/_сarib_TC.bmp"
    display_bmp(input_bmp_file)