<h1>Вывод BMP изображения про помощи библиотеки Tkinter</h1>

Задание: <br>
Вывести на экран 16, 256-цветный и true Color BMP файл используя
putpixel, без использования библиотек обработки графических файлов.

-----

```python 
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
```

Данная функция получает информацию о BMP изображении про помощи фукнции ```read_bmp``` и распределеяет её по необходимым полям
Далее создаётся поле ```canvas```, которое автоматически форматируется под размер исходного изобржадения. <br>
```root.mainloop()``` необходим для того, чтобы окно с изображением было открыто до тех пор пока пользователь его не закроет
