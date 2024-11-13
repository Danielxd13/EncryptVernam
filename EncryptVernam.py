def palabra_a_ascii(palabra):
    # Delete spaces y signos
    palabra_sin_signos = ''.join(filter(str.isalpha, palabra))
    return [ord(letra) for letra in palabra_sin_signos]

def num_to_bin(num):
    # convert each number to binary and remove the prefix '0b'
    codeBin = [bin(num)[2:].zfill(8) for num in num]
    return ' '.join(codeBin)

def xor_binaries(text, clave):
    # Separate the strings into individual binary lists
    text_bin = text.replace(' ', '')
    clave_bin = clave.replace(' ', '')

    # Calculate XOR punt to punt
    result_bin = ''

    for t, k in zip(text_bin, clave_bin):
        result_bin += str(int(t) ^ int(k))

    return ' '.join([result_bin[i:i+8] for i in range(0, len(result_bin), 8)])

def bin_to_decimal(bin_str):
    # Delete spaces string binaries
    bin_str = bin_str.replace(' ', '')
    return [int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8)]

def decimal_to_ascii(decimal_list):
    return ''.join(chr(i) for i in decimal_list)

# date
text = input("Enter text: ")
key =  input("Enter key: ")

# convert text and clave in ascii
textAscii = palabra_a_ascii(text)
calveAscii = palabra_a_ascii(key)
# see result ascii
print('Text: ',textAscii)
print('Clave: ',calveAscii,'\n')

# convert ascii in binary
textBin = num_to_bin(textAscii)
calveBin = num_to_bin(calveAscii)
# see result binaries
print('Text Binaries: ',textBin)
print('Clave Binaries: ',calveBin,'\n')

# Go to XOR
xor_bin = xor_binaries(textBin, calveBin)
print(f"XOR: {xor_bin}")
print('''
      XOR: 
        {}
      + {}
      ---------------
        {}
      '''.format(textBin, calveBin, xor_bin))

# Go to XOR to decimal
xor_dec = bin_to_decimal(xor_bin)
print(f"text decimal: {xor_dec}")

# Go to XOR to ASCII
encryption = decimal_to_ascii(xor_dec)
print(f"text encryption: {encryption}")