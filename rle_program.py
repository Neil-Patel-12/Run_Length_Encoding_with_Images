# project 2A
from console_gfx import ConsoleGfx

# 1. This works
# Ex: to_hex_string([3, 15, 6, 4]) yields string "3f64"
def to_hex_string(data):   # [3, 15, 6, 4]
    hex_charts99 = "0123456789abcdef"
    hex_str = ""
    for num in data:
        hex_str = hex_str + hex_charts99[num]
    return hex_str

# 2.
def count_runs(flat_data):     # [2, 3, 4, 5, 6]
    num_runs = 1
    numbers_same = 1

    for i in range(1, len(flat_data)):
        # this if-stat will check if the previous index is the same or not
        if flat_data[i] != flat_data[i - 1]:
            num_runs += 1
        else:
            numbers_same += 1
            if numbers_same == 15:
                num_runs += 2
    return num_runs

# 3.
# Ex: encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields list [3, 15, 6, 4].
def encode_rle(flat_data):
    encoded_data = []
    count = 1
    current_value = flat_data[0]

    for i in range(1, len(flat_data)):   # 16
        if flat_data[i] == current_value:
            count += 1
            # to make sure that 15 in a row will change to another count
            if count == 15:
                encoded_data.append(15)
                encoded_data.append(current_value)
                count = 0
        else:
            encoded_data.append(count)
            encoded_data.append(current_value)
            count = 1
        current_value = flat_data[i]
    # this if else statement block helps with the addition of range excluding last element
    if count == 15:
        encoded_data.append(15)
        encoded_data.append(current_value)
    else:
        encoded_data.append(count)
        encoded_data.append(current_value)
    return encoded_data

# 4.
# Ex: get_decoded_length([3, 15, 6, 4]) yields integer 9.
def get_decoded_length(rle_data):
    answer_output = 0
    for i in range(0, len(rle_data), 2):
        answer_output += rle_data[i]
    return answer_output
# 5.
# Ex: decode_rle([3, 15, 6, 4]) yields list [15, 15, 15, 4, 4, 4, 4, 4, 4].
def decode_rle(rle_data):   # enumerate
    long_list = []
    if rle_data != []:
        for i in range(0, len(rle_data), 2):
            num1 = rle_data[i]  # 3
            range_mil = i + 1
            list_ok = [rle_data[range_mil]]  # [15]

            multiply_lis_num = (list_ok * num1)
            long_list.extend(multiply_lis_num)

    return long_list

# 6.
# Ex: string_to_data ("3f64") yields list [3, 15, 6, 4]
def string_to_data(data_string): # 3f64
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    hex_str = []
    for num in data_string:
        hex_str = hex_str + [hex_list.index(num)]
    return hex_str

# 7.
# to_rle_string([15, 15, 6, 4]) yields string "15f:64"    # [1, 9, 1, 4, 15, 1, 15, 1, 6, 1]          # 19:14:151:151:61
def to_rle_string(rle_data):
    i = 0

    y = (f"{rle_data[i]}{rle_data[i + 1]}")
    x = []
    x.append(y)

    for i in range(2, len(rle_data) - 1, 2):
        z = (f"{rle_data[i]}{rle_data[i + 1]}")
        x.append(z)
    q = ":".join(x)
    return q


# 8. rle_string: "15f:64:1a:2e" => [15, 15, 6, 4, 1, 10, 2, 14] as output
def string_to_rle(rle_string):
    abc = "abcdef"
    main_list = []
    check_place = []
    value01 = 0 # test values
    value02 = 0
    run = True
    while run: # while loop because  we don't know how many values
        for i in range(value01, len(rle_string)):
            if rle_string[i] == ":": # didn't use split fun
                value02 = i
                break
            check_place.append(rle_string[i]) # to add to the practice list
            if i == len(rle_string) - 1:
                run = False

        # if 2 then do this
        if len(check_place) == 2:
            main_list.append(int(check_place[0]))
            if check_place[-1] in abc:
                main_list.append(10 + abc.index(check_place[-1]))
            else:
                main_list.append(int(check_place[-1]))
        # if 3 then do this
        if len(check_place) == 3:
            main_list.append((int(check_place[0]) * 10) + int(check_place[1]))
            if check_place[-1] in abc:
                main_list.append(10 + abc.index(check_place[-1]))
            else:
                main_list.append(int(check_place[-1]))
        check_place.clear()    # keep the practice list clean
        value01 = value02 + 1  # update the value of count value01
    return main_list



if __name__ == "__main__":
    # display the welcome message
    print("Welcome to the RLE image encoder!\n")
    # display spectrum message
    print("Displaying Spectrum Image: ")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    # image data veriable we have to set up (We initualy dont know what the image data look like )
    image_data = None

    while True:
        # 1. print all the menu options
        print("\nRLE Menu")
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
        print("9. Display Hex Flat Data\n")
        # 2. prompt the user for option
        option = int(input("Select a Menu Option: "))
        # 3. set up option 0,1,2,6 properly 2A
        if option == 0:
            break
        elif option == 1:
            # prompt the file name entered by user
            file_name = input("Enter name of file to load: ")
            # store ---> this image info ---> ConsoleGfx.load_file(filename=)     (this loaded file image information___in image_data variable)
            image_data = ConsoleGfx.load_file(file_name)
            # ConsoleGfx.displayimage(...)        takes in a decoded array of bytes
        elif option == 2:
            # test image
            print("Test image data loaded.")
            # store the ConsoleGfx.text_image into image_data variable
            image_data = ConsoleGfx.test_image
            # 2nd iteration when option 6, you will display this test image
            pass
        elif option == 3:
            dragon = input("Enter an RLE string to be decoded: ")
            dragon2 = string_to_rle(dragon)
            image_data = decode_rle(dragon2)
        elif option == 4:
            value99 = input("Enter the hex string holding RLE data: ")
            value98 = string_to_data(value99)
            image_data = decode_rle(value98)
        elif option == 5:
            fly = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(fly)
        elif option == 6:
            print("Displaying image...")
            # display the image_data using ConsoleGfx.display_image(image_data)
            ConsoleGfx.display_image(image_data)
        elif option == 7:
            cat02 = encode_rle(image_data)
            function_7 = to_rle_string(cat02)
            print(f"RLE representation: {function_7}")
        elif option == 8:
            walk1 = encode_rle(image_data)
            walk2 = to_hex_string(walk1)
            print(f"RLE hex values: {walk2}")
        elif option == 9:
            slide1 = to_hex_string(image_data)
            print(f"Flat hex values: {slide1}")
