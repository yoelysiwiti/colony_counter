import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog
from class_counter import ColonyCounter
from pages.phone_connector import Connect
import os
import sys


# ---------------- RESOURCE PATH ----------------
def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


ctk.set_appearance_mode("light")


class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.configure(fg_color="white")

        # ---------------- WINDOW ----------------
        self.geometry("900x650")
        self.title("Siwiti Colony Counter")

        # ---------------- ICON ----------------
        icon_path = resource_path("assets/icon.ico")
        self.iconbitmap(icon_path)

        # ---------------- MAIN IMAGE ----------------
        self.image_colonies = self.load_image(
            "assets/images_colonies.jfif",
            size=(500, 350)
        )

        # ---------------- LEFT FRAME ----------------
        self.left_frame = ctk.CTkFrame(
            self,
            fg_color="#F7F7F1",
            height=600,
            width=150,
            corner_radius=15,
            border_width=1,
            border_color="#F0EBE0"
        )

        self.left_frame.grid(row=0, column=0, rowspan=2, padx=(10, 5), pady=10)
        self.left_frame.grid_propagate(False)
        self.left_frame.grid_columnconfigure(0, weight=1)

        # ---------------- HEADER FRAME ----------------
        self.header_frame = ctk.CTkFrame(
            self,
            fg_color="#F7F7F1",
            height=50,
            width=720,
            corner_radius=10
        )

        self.header_frame.grid(row=0, column=1, padx=5, pady=(10, 5))
        self.header_frame.grid_propagate(False)

        self.header_frame_head = ctk.CTkLabel(
            self.header_frame,
            text="Welcome to Siwiti Colony counter",
            text_color="black",
            font=("Arial", 16, "bold")
        )

        self.header_frame_head.grid(
            row=0,
            column=0,
            padx=10,
            pady=(5, 0),
            sticky="w"
        )

        self.header_frame_para = ctk.CTkLabel(
            self.header_frame,
            text="Click to start your service",
            text_color="black"
        )

        self.header_frame_para.grid(
            row=1,
            column=0,
            padx=10,
            sticky="w"
        )

        # ---------------- MAIN FRAME ----------------
        self.main_frame = ctk.CTkFrame(
            self,
            fg_color="white",
            height=550,
            width=720,
            corner_radius=15,
            border_width=1,
            border_color="white"
        )

        self.main_frame.grid(row=1, column=1, padx=5, pady=(0, 10))
        self.main_frame.grid_propagate(False)

        # ---------------- LEFT MAIN SECTION ----------------
        self.main_frame_first = ctk.CTkFrame(
            self.main_frame,
            fg_color="#F7F7F1",
            height=530,
            width=470,
            corner_radius=15,
            border_width=1,
            border_color="#F0EBE0"
        )

        self.main_frame_first.grid(row=0, column=0, padx=5, pady=5)
        self.main_frame_first.grid_propagate(False)

        # ---------------- RIGHT MAIN SECTION ----------------
        self.main_frame_second = ctk.CTkFrame(
            self.main_frame,
            fg_color="#F7F7F1",
            height=530,
            width=230,
            corner_radius=15,
            border_width=1,
            border_color="#F0EBE0"
        )

        self.main_frame_second.grid(row=0, column=1, padx=5, pady=5)
        self.main_frame_second.grid_propagate(False)

        # ---------------- TOP FRAME ----------------
        self.main_frame_top = ctk.CTkFrame(
            self.main_frame_first,
            width=470,
            height=50,
            fg_color="#F7F7F1",
            border_width=1,
            border_color="#F0EBE0"
        )

        self.main_frame_top.grid(row=0, column=0, pady=(0, 5))
        self.main_frame_top.grid_propagate(False)

        # ---------------- MIDDLE FRAME ----------------
        self.main_frame_middle = ctk.CTkFrame(
            self.main_frame_first,
            fg_color="#F7F7F1",
            width=470,
            height=360
        )

        self.main_frame_middle.grid(row=2, column=0, pady=(5, 5))
        self.main_frame_middle.grid_propagate(False)

        # ---------------- IMAGE LABEL ----------------
        self.image_label = ctk.CTkLabel(
            self.main_frame_middle,
            width=500,
            height=350,
            corner_radius=15,
            image=self.image_colonies,
            text=""
        )

        self.image_label.grid(row=0, column=0)

        # ---------------- BOTTOM FRAME ----------------
        self.main_frame_bottom = ctk.CTkFrame(
            self.main_frame_first,
            width=470,
            height=50,
            fg_color="#F7F7F1"
        )

        self.main_frame_bottom.grid(row=1, column=0)
        self.main_frame_bottom.grid_propagate(False)

        # ---------------- SIDE FRAME ----------------
        self.main_frame_side = ctk.CTkFrame(
            self.main_frame_second,
            width=220,
            height=50,
            fg_color="#F7F7F1"
        )

        self.main_frame_side.grid(row=0, column=0, padx=5, pady=5)
        self.main_frame_side.grid_propagate(False)

        self.result_output = ctk.CTkLabel(
            self.main_frame_side,
            text="Result will appear here",
            font=("Arial", 16, "bold"),
            text_color="black"
        )

        self.result_output.grid(row=0, column=0)

        # ---------------- LOAD IMAGES ----------------
        self.image_profile = self.load_image("assets/profile.jfif")
        self.image_help = self.load_image("assets/images_help.png")
        self.image_colony_counter = self.load_image("assets/images_colonies.jfif")
        self.image_home = self.load_image("assets/images_home.jfif")
        self.settings_home = self.load_image("assets/settings.jfif")
        self.image_phone = self.load_image("assets/connect_phone.jfif")

        # ---------------- BUTTONS ----------------
        self.home_button = ctk.CTkButton(
            self.left_frame,
            image=self.image_home,
            text="Home",
            width=130,
            height=20,
            fg_color="transparent",
            hover_color="#EEEFEA",
            text_color="black",
            anchor="w"
        )

        self.home_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.profile_button = ctk.CTkButton(
            self.left_frame,
            image=self.image_profile,
            text="Profile",
            width=130,
            height=20,
            fg_color="transparent",
            hover_color="#EEEFEA",
            text_color="black",
            anchor="w"
        )

        self.profile_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.gc_ratio_button = ctk.CTkButton(
            self.left_frame,
            image=self.image_help,
            text="Help",
            text_color="black",
            width=130,
            height=20,
            fg_color="#F7F7F1",
            hover_color="#EEEFEA",
            anchor="w",
        )

        self.gc_ratio_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.colony_counter_button = ctk.CTkButton(
            self.left_frame,
            image=self.image_colony_counter,
            text="Upload Image",
            width=130,
            height=20,
            fg_color="#F7F7F1",
            hover_color="#EEEFEA",
            anchor="w",
            command=self.browse_file,
            text_color="black"
        )

        self.colony_counter_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        self.setting_button = ctk.CTkButton(
            self.left_frame,
            image=self.settings_home,
            text="Settings",
            width=130,
            height=20,
            fg_color="#F7F7F1",
            hover_color="#EEEFEA",
            anchor="w",
            text_color="black"
        )

        self.setting_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.phone_button = ctk.CTkButton(
            self.left_frame,
            image=self.image_phone,
            text="Link phone",
            width=130,
            height=20,
            fg_color="transparent",
            hover_color="#EEEFEA",
            text_color="black",
            anchor="w",
            command=self.phone_connector,
        )

        self.phone_button.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

        # ---------------- ENTRY ----------------
        self.file_input_entry = ctk.CTkEntry(
            self.main_frame_bottom,
            width=320,
            placeholder_text="Selected file path..."
        )

        self.file_input_entry.grid(row=0, column=0, padx=10, pady=10)

        # ---------------- SUBMIT BUTTON ----------------
        self.submit_button = ctk.CTkButton(
            self.main_frame_bottom,
            text="Submit",
            command=self.display_image,
            text_color="black",
            fg_color="#BDC0A0"
        )

        self.submit_button.grid(row=0, column=1, padx=10)

    # ---------------- LOAD IMAGE FUNCTION ----------------
    def load_image(self, path, size=(30, 30)):

        try:

            full_path = resource_path(path)

            image = Image.open(full_path)

            return ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=size
            )

        except FileNotFoundError:
            return None

    # ---------------- BROWSE FILE ----------------
    def browse_file(self):

        file_path = filedialog.askopenfilename(
            title="Select Biological Sequence File",
            filetypes=[
                ("Supported Files", "*.png *.jpg *.jpeg *.webp"),
                ("All Files", "*.*")
            ]
        )

        if file_path:
            self.file_input_entry.delete(0, ctk.END)
            self.file_input_entry.insert(0, file_path)

    # ---------------- DISPLAY IMAGE ----------------
    def display_image(self):

        file_path = self.file_input_entry.get()

        if file_path:

            image = Image.open(file_path)
            image = image.resize((400, 350))

            tk_image = ImageTk.PhotoImage(image)

            self.image_label.configure(image=tk_image)
            self.image_label.image = tk_image

            counter = ColonyCounter(file_path)

            result = counter.counter_colonies()

            result_text = f"Number of colonies : {result['normal']}"

            self.result_output.configure(text=result_text)

    # ---------------- PHONE CONNECTOR ----------------
    def phone_connector(self):

        for conn in self.main_frame.winfo_children():
            conn.destroy()

        Connect(self.main_frame)