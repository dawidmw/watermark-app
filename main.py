import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageFont, ImageDraw


def browse_files():
    while True:
        try:
            filename = tk.filedialog.askopenfile(
                initialdir="C:/",
                title="Select a picture",
                filetypes=[('Image Files', '*.jpg'), ('All Files', '*.jpeg')]
            )
            input_directory_entry_textvar.set(filename.name)
            break
        except AttributeError:
            print("File not chosen.")
            break

def set_output_path():
    output_path = tk.filedialog.askdirectory(
        initialdir="C:/",
        title="Select an output folder"
    )
    output_path = f"{output_path}"
    output_directory_entry_textvar.set(output_path)


def add_watermark():
    colors_palette = {"white": (255, 255, 255, 70),
                      "red": (255, 0, 0, 70),
                      "blue": (0, 0, 255, 70),
                      "green": (0, 128, 0, 70)}


    if input_directory_entry_textvar.get() == "" or output_directory_entry_textvar.get() == "":
        messagebox.showerror(title="Error",
                             message="Directory path cannot be empty.")
    else:
        with Image.open(input_directory_entry.get()).convert("RGBA") as im:
            font_size = int(font_size_getter.get())
            font_type = font_type_getter.get().lower()
            signature = signature_entry.get()

            txt = Image.new("RGBA", im.size, (255, 255, 255, 0))
            fnt = ImageFont.truetype(font=f"font/{font_type}.ttf", size=font_size)
            d = ImageDraw.Draw(txt)

            # draw text, half opacity
            d.text((10, 10), text=signature, font=fnt, fill=colors_palette[font_color_getter.get()])

            out = Image.alpha_composite(im, txt)

            file_name = simpledialog.askstring(title="Saving",
                                              prompt="Save file as: \t\t\t")

            output_entry = str(output_directory_entry_textvar.get())
            if output_entry.endswith("/"):
                full_output_path = output_entry + file_name + ".png"
            else:
                full_output_path = str(output_directory_entry_textvar.get()) + "/" + file_name + ".png"
            print(full_output_path)
            out.save(fp=full_output_path)


def exit_app():
    exit()


window = tk.Tk()
window.title('WatermarkYourPicture')
window.geometry('600x500')
window.maxsize(600, 500)

welcome = tk.Label(text='Welcome to the Watermark application.')

greeting = tk.Label(
    text="To add a watermark to your picture, please choose its location on your drive by clicking the 'Choose File' "
         "button.",
    height=3,
    wraplength=400)



input_directory_entry_textvar = tk.StringVar()
input_directory_entry_textvar.set("C:/")
input_directory_entry = tk.Entry(width=85, textvariable=input_directory_entry_textvar)

path_button = tk.Button(text="Choose File",
                        width=25,
                        command=browse_files,
                        pady=2, padx=2)

output_directory_entry_textvar = tk.StringVar()
output_directory_entry_textvar.set("C:/")
output_directory_entry = tk.Entry(width=85, textvariable=output_directory_entry_textvar)

output_path_button = tk.Button(text="Choose Output Folder",
                        width=25,
                        command=set_output_path,
                        pady=2, padx=2)

watermark_button = tk.Button(text="Add Watermark",
                             width=25,
                             command=add_watermark,
                             pady=2, padx=2)

exit_button = tk.Button(text="Close",
                        width=25,
                        command=exit_app,
                        pady=2, padx=2)

# -------------------------- signature setter ------------------------------ #
signature_label = tk.Label(text="Signature to add:")
entry_default = tk.StringVar()
entry_default.set("Your name")
signature_entry = tk.Entry(width=30, bd=2, textvariable=entry_default)


# --------------------------- font setters --------------------------------- #
text_var = tk.StringVar()
font_size_label = tk.Label(window, text="Font Size:")
font_size_getter = ttk.Combobox(window, width=3, textvariable=text_var)
font_size_getter['values'] = (12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 62, 70)

text_var2 = tk.StringVar
font_type_label = tk.Label(window, text="Font Style:")
font_type_getter = ttk.Combobox(window, width=14, textvariable=text_var2)
font_type_getter['values'] = ("OpenSans",
                              "Pacifico",
                              "DroidSans")

text_var3 = tk.StringVar
font_color_label = tk.Label(window, text="Font Color:")
font_color_getter = ttk.Combobox(window, width=14, textvariable=text_var2)
font_color_getter['values'] = ("white",
                               "red",
                               "blue",
                               "green")

# --------------------------- widgets layout ------------------------------- #
welcome.place(x=200, y=20)
greeting.place(x=100, y=40)

input_directory_entry.place(x=40, y=100)
path_button.place(x=50, y=125)
output_directory_entry.place(x=40, y=160)
output_path_button.place(x=50, y=185)
watermark_button.place(x=50, y=215)
exit_button.place(x=50, y=260)

signature_label.place(x=298, y=185)
signature_entry.place(x=300, y=205)

font_size_label.place(x=298, y=225)
font_size_getter.place(x=300, y=245)

font_type_label.place(x=298, y=266)
font_type_getter.place(x=300, y=286)

font_color_label.place(x=298, y=307)
font_color_getter.place(x=300, y=327)

font_size_getter.current(3)
font_type_getter.current(0)
font_color_getter.current(0)

window.mainloop()
