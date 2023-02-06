from PIL import Image

import sys
import numpy

save_file = 'image.txt'


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

                with open(save_file, 'w') as file:
                    print("Writing image to file...")
                    file.write(array)

                print(f"Successfully saved image to '{save_file}'.")
        except FileNotFoundError:
            print("Invalid image. Is it inside of this folder?")
    except IndexError:
        print("Please enter a valid file name.")


if __name__ == '__main__':
    main()
