# import qrcode

# data = input('Enter the text or URL: ').strip()
# filename = input('Enter the file name: ').strip()

# qr = qrcode.QRCode(box_size=10, border=4)

# qr.add_data(data) 

# image = qr.make_image(fill_color='black', back_color='white')

# image.save(filename)

# print(f'QR code saved as: {filename}')


import qrcode

def generate_qr_code(data, filename, fill_color='black', back_color='white'):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=fill_color, back_color=back_color)
    image.save(filename)
    print(f'QR code saved as: {filename}')

def main():
    print("Welcome to the QR Code Generator!")
    
    # Choose mode: Single or Multiple
    mode = input("Do you want to generate a single QR code or multiple? (single/multiple): ").strip().lower()
    
    if mode == "single":
        # Single QR Code
        data = input("Enter the text or URL: ").strip()
        filename = input("Enter the file name (e.g., 'example.png'): ").strip()
        fill_color = input("Enter the QR code color (default is black): ").strip() or 'black'
        back_color = input("Enter the background color (default is white): ").strip() or 'white'
        generate_qr_code(data, filename, fill_color, back_color)
    
    elif mode == "multiple":
        # Multiple QR Codes
        print("Enter multiple texts or URLs separated by commas.")
        data_list = input("Enter the texts/URLs: ").strip().split(',')
        fill_color = input("Enter the QR code color (default is black): ").strip() or 'black'
        back_color = input("Enter the background color (default is white): ").strip() or 'white'
        
        for i, data in enumerate(data_list, start=1):
            filename = f"qr_code_{i}.png"
            generate_qr_code(data.strip(), filename, fill_color, back_color)
        print("All QR codes have been generated!")
    
    else:
        print("Invalid mode selected. Please choose 'single' or 'multiple'.")

if __name__ == "__main__":
    main()
