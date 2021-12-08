from PIL import Image
import collections

imagePath = 'example.jpg'
newImagePath = 'result.jpg'

def return_8_bit(number):
    binary_number = bin(number)
    if len(binary_number) < 10:
        return binary_number[0:2] + ('0' * (10 - len(binary_number))) + binary_number[2:]
    return binary_number

string_to_insert = "matan kotick was here\n"

def get_string_current_bit():
    while True:
        for character in string_to_insert:
            for bit in return_8_bit(ord(character))[2:]:
                yield bit

MY_OFFSET = 1000

def write_on_msb(number, bit):
    binary_number = return_8_bit(number)
    new_binary_number = list(binary_number)
    new_binary_number[2] = bit

    return int(''.join(new_binary_number), 2)

def creator (source):
    im = Image.open(source)
    newimdata = []
    current_char_index = 0
    message_generator = get_string_current_bit()
    for index, color in enumerate(im.getdata()):
        if index % MY_OFFSET != 0:
            newimdata.append( color )
            continue    
        
        #new_color = (ord(string_to_insert[current_char_index]), color[1], color[2])
        current_bit = next(message_generator)
        new_color = (write_on_msb(color[0], current_bit),
                    write_on_msb(color[1], current_bit),
                    write_on_msb(color[2], current_bit))

        current_char_index += 1
        current_char_index %= len(string_to_insert)
        newimdata.append( new_color )

    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

def investigator(source):
    im = Image.open(source)
    current_character = ""
    current_string = ""
    
    message = get_string_current_bit()
    errors = 0
    number = 0
    for index, color in enumerate(im.getdata()):
        if index % MY_OFFSET != 0:
            continue
        number += 1
        
        current_bit_str = return_8_bit(color[0])[2] + return_8_bit(color[1])[2] + return_8_bit(color[2])[2]
        current_bit = collections.Counter(current_bit_str).most_common(1)[0][0]

        if current_bit != next(message):
            errors += 1
        current_character += current_bit

        if len(current_character) == 8:
            current_character_chr = chr(int(current_character, 2))
            current_string += current_character_chr

            if current_character_chr == '\n':
                print (current_string)
                current_string = ""

            current_character = ""
    print (str(errors) + "/" + str(number))
    print (str(float(errors) * (100.0 / number)))

creator(imagePath).save(newImagePath)
investigator(newImagePath)