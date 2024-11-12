# main.py
from gui import create_interface
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def main():
    root = ctk.CTk()
    root.title("Color Converter")
    root.geometry("800x700")

    create_interface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
