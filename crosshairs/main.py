import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
crosshair = tk.Toplevel()
#change the size to your crosshair width and height 
windows_size = 21
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
x_position = (x // 2) - (windows_size // 2)
y_position = (y // 2) - (windows_size // 2)
crosshair.overrideredirect(True)
crosshair.geometry(f"{windows_size}x{windows_size}+{x_position}+{y_position}")
crosshair.attributes('-topmost', True)
crosshair.configure(bg="black")
crosshair.wm_attributes("-transparentcolor", 'black')
crosshair_image = tk.Label(crosshair, bg="black")
crosshair_image.pack()
root.geometry(f"200x200+{x_position}+{y_position}")
crosshair.image = None


def select_crosshair():
    crosshair_path = filedialog.askopenfilename()
    if crosshair_path:
        crosshair.image = tk.PhotoImage(file=crosshair_path)
        crosshair_image.config(image=crosshair.image)



select_crosshair_button = tk.Button(root, text="Choose your corsshair", command=select_crosshair)
select_crosshair_button.pack(expand=True)

root.mainloop()