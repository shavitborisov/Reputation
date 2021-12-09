from PIL import Image
import collections
import random

imagePath = 'example.jpg'
newImagePath = 'result.jpg'

def return_8_bit(number):
    bin_num = bin(number)
    return bin_num[:2] + ('0' * (10 - len(bin_num))) + bin_num[2:]

EXAMPLE_STRING = "Gal Sade Sade"
MAJOR = 15
BIT_LOCATION = 2
DECODE_TIMES = 1
SEED = 0xdeadbeaf

def get_string_current_bit(string_to_code):
    string_to_code = chr(len(string_to_code)) + string_to_code
    for i in range(DECODE_TIMES):
        for character in string_to_code:
            for bit in return_8_bit(ord(character))[2:]:
                for j in range(MAJOR):
                    yield bit

def index_generator_one(offset, image_length):
    index_array = 0
    while index_array < image_length:
        index_array += offset
        yield index_array

def index_generator_two(image_length):
    random.seed(SEED)
    values = set()
    while True:
        current_value = random.randrange(image_length)
        while current_value in values:
            current_value += 1
            current_value %= image_length
        values.add(current_value)
        yield current_value

def index_generator_three(offset, width, height):
    index_array = 0
    for i in range(height):
        for j in range(width):
            yield 16

def index_generator(width, height):
    return index_generator_two(width * height)

def write_on_msb(number, bit):
    binary_number = return_8_bit(number)
    new_binary_number = list(binary_number)
    new_binary_number[BIT_LOCATION] = bit

    return int(''.join(new_binary_number), 2)

def creator (source, string_to_encode):
    im = Image.open(source)
    newimdata = [color for color in im.getdata()]

    message_generator = get_string_current_bit(string_to_encode)
    index_gen = index_generator(*im.size)
    for current_bit in message_generator:
        index = next(index_gen)
        color = newimdata[index]
        
        #new_color = (ord(string_to_insert[current_char_index]), color[1], color[2])
        new_color = (write_on_msb(color[0], current_bit),
                    write_on_msb(color[1], current_bit),
                    write_on_msb(color[2], current_bit))
        #new_color = (write_on_msb(color[0], current_bit), color[1], color[2])
        newimdata[index] = new_color

    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

def most_common(lst):
    return max(set(lst), key=lst.count)

def investigator(source):

    all_messages = []

    im = Image.open(source)
    bit_collector = ""
    current_string = ""
    current_character = ""
    
    first_byte = True
    message_length = 0
    decoded_messages = 0
    index_gen = index_generator(*im.size)
    for index in index_gen:
        color = im.getdata()[index]
        
        current_bit_str = return_8_bit(color[0])[BIT_LOCATION] + \
                        return_8_bit(color[1])[BIT_LOCATION] + \
                        return_8_bit(color[2])[BIT_LOCATION]
        current_bit = collections.Counter(current_bit_str).most_common(1)[0][0]
        bit_collector += current_bit

        if len(bit_collector) == MAJOR:
            real_bit = collections.Counter(bit_collector).most_common(1)[0][0]
            current_character += real_bit

            if len(current_character) == 8:

                current_character_chr = chr(int(current_character, 2))
                if first_byte:
                    message_length = ord(current_character_chr)
                    first_byte = False
                else:
                    current_string += current_character_chr
                    if len(current_string) == message_length:
                        all_messages.append(current_string)
                        current_string = ""
                        first_byte = True
                        decoded_messages += 1
                        if decoded_messages == DECODE_TIMES:
                            break
                current_character = ""
            bit_collector = ""

    return most_common(all_messages)

if __name__ == '__main__':
    creator(imagePath, EXAMPLE_STRING).save(newImagePath)
    print (investigator(newImagePath))