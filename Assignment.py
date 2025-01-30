import binascii
import json


def hex_to_ascii(hex_string):
    bytes_data = binascii.unhexlify(hex_string)
    return bytes_data.decode('utf-8')


def ascii_to_hex(ascii_string):
    return binascii.hexlify(ascii_string.encode('utf-8')).decode()


def encode_unknown(hex_string):
    return binascii.hexlify(binascii.unhexlify(hex_string)).decode()


def decode_unknown(unknown_string):
    return binascii.hexlify(binascii.unhexlify(unknown_string)).decode()


def process_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    for key, value in data.items():
        hex_value = value["hex"]
        ascii_value = hex_to_ascii(hex_value)
        encoded_unknown = encode_unknown(hex_value)
        decoded_hex = decode_unknown(value["unknown"])

        print(f"Dataset {key}:")
        print(f"Hex: {hex_value}")
        print(f"ASCII: {ascii_value}")
        print(f"Encoded Unknown: {encoded_unknown}")
        print(f"Decoded Hex: {decoded_hex}")
        print("-" * 50)


process_json('C:\\Users\\Asus\\PycharmProjects\\pythonProject\\assingment_cryptography.json')
