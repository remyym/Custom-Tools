from PIL import Image

import sys
import numpy
import pyperclip

def main():
    try:
        file = sys.argv[1]

        try:
            with Image.open(file).convert('RGBA') as image:
                # noinspection PyTypeChecker
                array = str(numpy.asarray(image).tolist())

                array = array.replace('[', '{')
                array = array.replace(']', '}')

                print(f"Pixels: {str(len(array))}")

                pyperclip.copy(array)

                print("Successfully copied image to clipboard.")
        except FileNotFoundError:
            print("Invalid image. Is it inside of this folder?")
    except IndexError:
        print("Please enter a valid file name.")


if __name__ == '__main__':
    main()
