import argparse
import qrcode
import os
import platform

def main():
    parser = argparse.ArgumentParser(description='Generate a QR code from a string or URL')
    parser.add_argument('data', metavar='DATA', type=str, help='The data to encode in the QR code')
    parser.add_argument('-n', '--name', type=str, default='qr_code', help='The name of the output image file (without extension)')
    args = parser.parse_args()

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(args.data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    file_ext = 'png' # Change file extension here if needed
    image_name = args.name + '.' + file_ext

    img.save(image_name)
    print(f"QR code saved to {image_name}")

    if platform.system() == 'Darwin':
        os.system(f"open {image_name}")
    elif platform.system() == 'Linux':
        os.system(f"xdg-open {image_name}")
    elif platform.system() == 'Windows':
        os.system(f"start {image_name}")
    else:
        print(f"Please open the file manually: {image_name}")


if __name__ == '__main__':
    main()
