from flask import Flask, render_template
from pathlib import Path
import threading
import socket
import customtkinter as ctk
from PIL import Image
from reusable_tasks.tasks import  Tasks

class Connect:

    def __init__(self, parent):
        ip = self.get_ip()

        tasks = Tasks()
        lin = "http://" + ip + ":5000"
        tasks.qr_generator(lin)


        self.parent = parent

        # ALWAYS POINT TO PROJECT ROOT
        base_dir = Path(__file__).resolve().parent.parent
        template_dir = base_dir / "templates"

        print("DEBUG template path:", template_dir)

        self.app = Flask(
            __name__,
            template_folder=str(template_dir)
        )

        @self.app.route("/")
        def home():
            return render_template("index.html")

        threading.Thread(target=self.run_server, daemon=True).start()

        ctk.CTkLabel(
            parent,
            text=f"Open on phone: http://{ip}:5000",
            font=("Arial", 20),
            fg_color="blue"
        ).grid(row=0, column=0)

        qr_image = Image.open("qr_img.png")

        ctk_qr_image = ctk.CTkImage(
            light_image=qr_image,
            dark_image=qr_image,
            size=(600, 600)

        )
        qr_image_label = ctk.CTkLabel(
            parent,
            image=ctk_qr_image,
            height=500,
            width=600
        )
        qr_image_label.grid(row=1, column=0)

    def run_server(self):
        self.app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
    @staticmethod
    def get_ip():

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
        except:
            return "127.0.0.1"
        finally:
            s.close()
