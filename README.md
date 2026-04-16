# 🖼️ PixelGuard: Image Encryption & Decryption Tool

PixelGuard is a simple, lightweight Python application that allows you to secure your images using pixel-level manipulation. By applying a mathematical XOR operation to every pixel, it transforms your images into unreadable noise that can only be restored with your secret key.

## 🚀 Features
- **Modern GUI**: A clean, dark-themed interface built with Python's Tkinter.
- **Symmetric Logic**: The same secret key is used to both scramble (encrypt) and restore (decrypt) the image.
- **Fast Processing**: Uses optimized Lookup Tables (LUT) to process high-resolution images instantly.
- **Lossless Output**: Automatically saves as `.png` to ensure that every pixel is preserved perfectly for decryption.

---

## 🛠️ Setup & Installation

### 1. Install Python
Ensure you have Python 3.x installed on your computer. You can download it from [python.org](https://www.python.org/).

### 2. Install Required Library
The tool uses the **Pillow** library for image processing. Install it via your terminal:
```bash
pip install Pillow
```
### 📖 How to Use

### 🔒 Encrypting an Image
Click Select Image and choose any photo (.jpg, .png, or .bmp).
Enter a Secret Key (any whole number between 0 and 255).
Click ENCRYPT.
Choose where to save your "scrambled" file. It will look like colorful static.

### 🔓 Decrypting an Image
Click Select Image and choose the scrambled .png file you created.
Enter the EXACT SAME Secret Key you used to encrypt it.
Click DECRYPT.
Choose a save location, and your original image will be perfectly restored.

## 🧠 The "Math" Behind It

This tool uses the Bitwise XOR (^) operation:
When you XOR a pixel value with a key, it changes into a new, seemingly random value.
Because of the unique properties of XOR logic, if you XOR that new value with the same key again, it returns to the original value.
Formula: (Original Pixel ^ Key) ^ Key = Original Pixel

## ⚠️ Important Notes
Key Sensitivity: If you forget your key or enter it wrong by even 1 digit, the decryption will fail, and the image will remain scrambled.
File Formats: Always save your encrypted files as .png. If you save an encrypted image as a .jpg, the JPEG compression will "smudge" the pixel colors, making it impossible to decrypt the image back to its original state.

## 📜 License
This project is open-source and intended for educational use.

