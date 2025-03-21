import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")
        self.root.geometry("600x400")

        # UI Elements
        self.label = tk.Label(root, text="Upload an Image", font=("Arial", 14))
        self.label.pack(pady=10)

        self.upload_btn = tk.Button(root, text="Choose Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        self.canvas = tk.Canvas(root, width=400, height=250, bg="gray")
        self.canvas.pack()

        self.text_entry = tk.Entry(root, width=30)
        self.text_entry.insert(0, "Your Watermark")
        self.text_entry.pack(pady=5)

        self.add_text_btn = tk.Button(root, text="Add Text Watermark", command=self.add_text_watermark)
        self.add_text_btn.pack(pady=5)

        self.add_logo_btn = tk.Button(root, text="Add Logo Watermark", command=self.add_logo_watermark)
        self.add_logo_btn.pack(pady=5)

        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_btn.pack(pady=5)

        self.image_path = None
        self.image = None
        self.tk_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        self.image.thumbnail((400, 250))
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(200, 125, image=self.tk_image)

    def add_text_watermark(self):
        if not self.image:
            messagebox.showerror("Error", "Please upload an image first!")
            return

        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("arial.ttf", 30)
        text = self.text_entry.get()
        text_position = (20, 20)
        draw.text(text_position, text, fill=(255, 255, 255, 128), font=font)
        self.display_image()

    def add_logo_watermark(self):
        logo_path = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
        if not logo_path:
            return

        logo = Image.open(logo_path).convert("RGBA")
        logo.thumbnail((100, 100))
        if not self.image:
            messagebox.showerror("Error", "Please upload an image first!")
            return

        self.image.paste(logo, (self.image.width - 120, self.image.height - 120), logo)
        self.display_image()

    def save_image(self):
        if not self.image:
            messagebox.showerror("Error", "No image to save!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG Files", "*.png"),
                                                            ("JPEG Files", "*.jpg"),
                                                            ("All Files", "*.*")])
        if save_path:
            self.image.save(save_path)
            messagebox.showinfo("Success", "Image saved successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
