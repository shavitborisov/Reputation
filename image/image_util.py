from PIL import Image
import collections

imagePath = 'example.jpg'
newImagePath = 'result.jpg'

def return_8_bit(number):
    binary_number = bin(number)
    if len(binary_number) < 10:
        return binary_number[0:2] + ('0' * (10 - len(binary_number))) + binary_number[2:]
    return binary_number

string_to_insert = "matankoo"
major = 10
bit_location = 2

def get_string_current_bit(string_to_code):
    while True:
        for character in string_to_code:
            for bit in return_8_bit(ord(character))[2:]:
                for i in range(major):
                    yield bit


def index_generator(image_length):
    return set([200*i for i in range(64*1*major)])


def write_on_msb(number, bit):
    binary_number = return_8_bit(number)
    new_binary_number = list(binary_number)
    new_binary_number[bit_location] = bit

    return int(''.join(new_binary_number), 2)

def creator (source, string_to_encode):
    im = Image.open(source)
    newimdata = []
    current_char_index = 0

    message_generator = get_string_current_bit(string_to_encode)
    index_gen = index_generator(len(im.getdata()))
    for index, color in enumerate(im.getdata()):
        if index not in index_gen:
            newimdata.append( color )
            continue    
        
        #new_color = (ord(string_to_insert[current_char_index]), color[1], color[2])
        current_bit = next(message_generator)
        new_color = (write_on_msb(color[0], current_bit),
                    write_on_msb(color[1], current_bit), color[2])
                    #write_on_msb(color[2], current_bit))
        #new_color = (write_on_msb(color[0], current_bit), color[1], color[2])

        current_char_index += 1
        current_char_index %= len(string_to_insert)
        newimdata.append( new_color )

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
    
    message = get_string_current_bit(string_to_insert)
    errors = 0
    number = 0

    index_gen = index_generator(len(im.getdata()))
    for index, color in enumerate(im.getdata()):
        if index not in index_gen:
            continue

        number += 1
        
        current_bit_str = return_8_bit(color[0])[bit_location]# + \
                        #return_8_bit(color[1])[bit_location] + \
                        #return_8_bit(color[2])[bit_location]
        current_bit = collections.Counter(current_bit_str).most_common(1)[0][0]
        bit_collector += current_bit
        
        if current_bit != next(message):
            errors += 1

        if len(bit_collector) == major:
            real_bit = collections.Counter(bit_collector).most_common(1)[0][0]
            current_character += real_bit

            if len(current_character) == 8:
                current_character_chr = chr(int(current_character, 2))
                current_string += current_character_chr

                if len(current_string) == 8:
                    all_messages.append(current_string)
                    current_string = ""

                current_character = ""
            bit_collector = ""
    
    print (str(errors) + "/" + str(number))
    print (str(float(errors) * (100.0 / number)))

    return all_messages[0]

creator(imagePath, string_to_insert).save(newImagePath)
print (investigator(newImagePath))