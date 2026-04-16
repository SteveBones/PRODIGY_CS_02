import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageEncryptor:
    def __init__(self, root):
        self.root = root
        self.root.title("PixelGuard: Encrypt & Decrypt")
        self.root.geometry("500x550")
        self.root.configure(bg="#1e1e2e")

        # UI Elements
        self.create_widgets()
        self.file_path = ""

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="PixelGuard Tool", font=("Arial", 20, "bold"), bg="#1e1e2e", fg="#cba6f7").pack(pady=20)

        # File Selection Frame
        frame = tk.Frame(self.root, bg="#313244", padx=10, pady=10)
        frame.pack(pady=10, padx=20, fill="x")

        self.label_path = tk.Label(frame, text="No file selected", bg="#313244", fg="white", wraplength=350)
        self.label_path.pack(pady=5)

        btn_browse = tk.Button(frame, text="Select Image", command=self.select_image, bg="#45475a", fg="white", relief="flat")
        btn_browse.pack()

        # Key Input
        tk.Label(self.root, text="Enter Secret Key (0-255):", bg="#1e1e2e", fg="#a6adc8").pack(pady=(20, 0))
        self.entry_key = tk.Entry(self.root, justify="center", font=("Arial", 14), bg="#181825", fg="#f9e2af", insertbackground="white")
        self.entry_key.insert(0, "123")
        self.entry_key.pack(pady=5)

        # Action Buttons
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(pady=20)

        # Encrypt and Decrypt buttons both call the same process function
        btn_encrypt = tk.Button(btn_frame, text="ENCRYPT", command=self.process, bg="#f38ba8", fg="white", font=("Arial", 10, "bold"), width=12)
        btn_encrypt.pack(side="left", padx=10)

        btn_decrypt = tk.Button(btn_frame, text="DECRYPT", command=self.process, bg="#a6e3a1", fg="#11111b", font=("Arial", 10, "bold"), width=12)
        btn_decrypt.pack(side="left", padx=10)

        # Status
        self.status = tk.Label(self.root, text="Ready", bg="#1e1e2e", fg="#6c7086")
        self.status.pack(side="bottom", pady=10)

    def select_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if self.file_path:
            self.label_path.config(text=self.file_path)
            self.status.config(text="Image loaded.", fg="#89b4fa")

    def process(self):
        if not self.file_path:
            messagebox.showwarning("Error", "Please select an image first!")
            return

        try:
            key = int(self.entry_key.get())
            if not (0 <= key <= 255):
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Key", "Please enter a number between 0 and 255.")
            return

        try:
            # 1. Open image and ensure RGB mode
            img = Image.open(self.file_path).convert("RGB")
            
            # 2. XOR Logic (The LUT method is the most stable)
            # This math converts original -> encrypted AND encrypted -> original
            lut = [i ^ key for i in range(256)]
            processed_img = img.point(lut * 3) # Apply to R, G, and B channels

            # 3. Save as PNG (Lossless)
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            
            if save_path:
                processed_img.save(save_path, "PNG")
                self.status.config(text="File saved successfully!", fg="#a6e3a1")
                messagebox.showinfo("Success", f"Operation successful!\nSaved to: {save_path}")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptor(root)
    root.mainloop()