from ui.colony_counter import App
import os

app = App()

def on_close():
    if os.path.exists("qr_img.png"):
        os.remove("qr_img.png")

    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_close)
app.mainloop()