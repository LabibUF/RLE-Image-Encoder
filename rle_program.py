# from the code that was provided the ConsoleGfx function is imported
from console_gfx import ConsoleGfx


# Sets up another function where the menu is set up and menu options can be chosen to do different things.
def menu_display():
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")
    print("")

# Method 2
def count_runs(flat_data):
    count = 0
    current_run = 1

    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            current_run += 1
        else:
            count += current_run // 15 + 1
            current_run = 1

    count += current_run // 15 + 1

    return count

# Method 1
def to_hex_string(data):
    image_data = ""
    for i in data:
        if i == 10:
            image_data += 'a'
        elif i == 11:
            image_data += 'b'
        elif i == 12:
            image_data += 'c'
        elif i == 13:
            image_data += 'd'
        elif i == 14:
            image_data += 'e'
        elif i == 15:
            image_data += 'f'
        else:
            image_data += str(i)
    return image_data

# Method 3
def encode_rle(flat_data):
    image_data = []

    count = 1
    for i in range(1, len(flat_data)):
        if flat_data[i - 1] == flat_data[i]:
            count += 1
            if count == 15:
                image_data.extend([15, flat_data[i - 1]])
                count = 0
        else:
            if count == 15:
                image_data.extend([15, flat_data[i - 1]])
                count = 1
            else:
                image_data.extend([count, flat_data[i - 1]])
                count = 1

    image_data.extend([count, flat_data[-1]])

    return image_data

# Method 5
def decode_rle(rle_data):
    image_data = []
    for i in range(0, len(rle_data), 2):
        count = rle_data[i]
        multiply = rle_data[i + 1]
        image_data.extend([multiply] * count)
    return image_data

# Method 4
def get_decoded_length(rle_data):
    total = len(decode_rle(rle_data))
    return total

# Method 6
def string_to_data(data_string):
    image_data = []
    for i in data_string:
        if i == 'a':
            image_data.append(10)
        elif i == 'b':
            image_data.append(11)
        elif i == 'c':
            image_data.append(12)
        elif i == 'd':
            image_data.append(13)
        elif i == 'e':
            image_data.append(14)
        elif i == 'f':
            image_data.append(15)
        else:
            image_data.append(int(i))
    return image_data

# Method 8
def string_to_rle(rle_string):
    image_data = []
    string_split = rle_string.split(":")

    for i in string_split:
        split1 = int(i[ : -1])
        split2 = "0123456789abcdef".index(i[-1])
        image_data.extend([split1, split2])
    return image_data

# Method 7
def to_rle_string(rle_data):
    image_data = ""
    for i in range(0, len(rle_data), 2):
        split1 = rle_data[i]
        split2 = rle_data[i + 1]

        if split1 < 10:
            split1 = str(split1)
        else:
            str(split1)
        hex_conversion = "0123456789abcdef"
        split2 = hex_conversion[split2 % 16]
        image_data += f"{split1}{split2}:"

    image_data = image_data[ : -1]

    return image_data



# While loop is set up so that the code continues to run and you can choose different things
def main():
    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    menu_display()
    rle_string = ""

    print_image = None

    while True:
        user_input = int(input("Select a Menu Option: "))

    # If user inputs 1 they will be prompted to enter a file name and then the program will load it.
        if user_input == 1:
            print_image = input("Enter name of file to load: ")
            print_image = ConsoleGfx.load_file(print_image)

    # If user inputs 2 the test image will be loaded into the program
        if user_input == 2:
            print_image = ConsoleGfx.test_image
            print("Test image data loaded.")

    # If user inputs 6 the image that is loaded will be displayed
        if user_input == 6:
            print("Displaying image...")
            if print_image is not None:
                ConsoleGfx.display_image(print_image)
            else:
                print("(no data)")

    # If user inputs 3 an RLE string has to be inputed and methods 8 and 5 run
        if user_input == 3:
            input_data = input("Enter an RLE string to be decoded: ")
            print_image = decode_rle(string_to_rle(input_data))

    # If user enters 7 it will print no data if there was no data loaded in but if 4 was pressed first then it will output the stored data
        if user_input == 7:
            if print_image is not None:
                print("RLE representation:", rle_string)
            else:
                print("RLE representation: (no data)")

    # If user inputs something greater than 9 or less than 0 it makes us choose a valid input
        if user_input > 9 or user_input < 0:
            print("Error! Invalid input.")

    # If user inputs 8 it will print no data if there was no data loaded in but it 5 was inputed first then it will output the stored data
        if user_input == 8:
            if print_image is not None:
                hex_rle_data = ""
                for i in encode_rle(print_image):
                    hex_rle_data += format(i, 'x')
                print("RLE hex values:", hex_rle_data)
            else:
                print("RLE hex values: (no data)")

    # If user inputs 9 it will print eithe no data or whatever was stored
        if user_input == 9:
            if print_image is not None:
                flat_hex_data = ""
                for i in print_image:
                    flat_hex_data += format(i, 'x')
                print("Flat hex values:", flat_hex_data)
            else:
                print("Flat hex values: (no data)")

    # If user inputs 0 the program will end
        if user_input == 0:
            break

    # If user inputs 4 user will be prompted to input a hex string it will then be converted and stored.
        if user_input == 4:
            print_image = True
            input_data = input("Enter the hex string holding RLE data: ")
            rle_string = to_rle_string(string_to_data(input_data))

        # If user inputs 5 user will be prompted to input a hex string it will then be converted and stored.
        if user_input == 5:
            print_image = True
            input_data = input("Enter the hex string holding flat data: ")
            rle_string = string_to_data(input_data)

        menu_display()

if __name__ == '__main__':
    main()