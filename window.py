from tkinter import *


def btn_clicked():
    print("Button Clicked")


#ekranın tam ortasında başlatmak için
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

window = Tk()
window.title("")
window.geometry("1000x600")
window.configure(bg = "#ffffff")
window_width = 1000
window_height = 600
center_window(window, window_width, window_height)

#window.overrideredirect(True)   #pencere bölmesini gizler kücült kapat buttonlarının olduğu windows formunu

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    554.5, 421.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    740.0, 193.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 553.0, y = 165,
    width = 374.0,
    height = 54)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    740.0, 296.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 553.0, y = 268,
    width = 374.0,
    height = 54)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 658, y = 344,
    width = 183,
    height = 49)

window.resizable(False, False)
window.mainloop()
