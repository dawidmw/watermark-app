import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw

def browse_files():
    filename = tk.filedialog.askopenfile(
        initialdir="C:/",
        title="Select a picture",
        filetypes=[('Image Files', '*.jpg')]
    )
    print(filename.name)
    file_path = filename.name
    fp.config(text=f'Chosen path: {file_path}')
    return file_path


def add_watermark():
    with Image.open(file_path).convert("RGBA") as im:

        txt = Image.new("RGBA", im.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype("arial", 40)
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((10, 10), "Dawid-san", font=fnt, fill=(255, 255, 255, 150))

        out = Image.alpha_composite(im, txt)
        out.save('new.png')


def exit_app():
    exit()


window = tk.Tk()
window.title('WatermarkYourPicture')
window.geometry('500x400')


welcome = tk.Label(text='Welcome to the Watermark application.')

greeting = tk.Label(text="To add a watermark to your picture, please choose its\n location on your drive by clicking the"
                         " 'Choose File' button.",
                    height=5,
                    width=350)

ok_button = tk.Button(text="Choose File",
                      width=25,
                      command=browse_files)

exit_button = tk.Button(text="Close",
                        width=25,
                        command=exit_app)

fp = tk.Label(text="")

welcome.pack()
greeting.pack()
fp.pack()

ok_button.pack()
exit_button.pack()




window.mainloop()
