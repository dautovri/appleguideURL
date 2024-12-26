import urllib.parse
import base64
from google.protobuf.internal.decoder import _DecodeVarint
from google.protobuf.internal.wire_format import (
    WIRETYPE_VARINT,
    WIRETYPE_FIXED64,
    WIRETYPE_LENGTH_DELIMITED,
    WIRETYPE_FIXED32
)

def decode_protobuf_fields(data, indent=0):
    """
    Decode protobuf fields from the given data.
    
    Args:
        data (bytes): The protobuf data to decode.
        indent (int): The indentation level for nested fields.
    
    Returns:
        list: A list of Apple IDs extracted from the protobuf fields.
    """
    pos = 0
    apple_ids = []
    while pos < len(data):
        try:
            tag_wire, new_pos = _DecodeVarint(data, pos)
            field_number = tag_wire >> 3
            wire_type = tag_wire & 0x7
            pos = new_pos

            if wire_type == WIRETYPE_VARINT:
                value, pos = _DecodeVarint(data, pos)
                if field_number == 2:
                    apple_id = 'I' + hex(value)[2:].upper()
                    apple_ids.append(apple_id)

            elif wire_type == WIRETYPE_FIXED64:
                pos += 8

            elif wire_type == WIRETYPE_LENGTH_DELIMITED:
                length, new_pos = _DecodeVarint(data, pos)
                value = data[new_pos:new_pos + length]
                pos = new_pos + length
                if len(value) > 0:
                    apple_ids.extend(decode_protobuf_fields(value, indent + 1))

            elif wire_type == WIRETYPE_FIXED32:
                pos += 4
        except Exception as e:
            print(f"Error decoding field: {e}")
    return apple_ids

def extract_location_description(data):
    """
    Extract the location description from the given protobuf data.
    
    Args:
        data (bytes): The protobuf data to decode.
    
    Returns:
        str: The location description if found, otherwise None.
    """
    pos = 0
    while pos < len(data):
        try:
            tag_wire, new_pos = _DecodeVarint(data, pos)
            field_number = tag_wire >> 3
            wire_type = tag_wire & 0x7
            pos = new_pos

            if wire_type == WIRETYPE_LENGTH_DELIMITED:
                length, new_pos = _DecodeVarint(data, pos)
                value = data[new_pos:new_pos + length]
                pos = new_pos + length
                try:
                    description = value.decode('utf-8')
                    if field_number == 1:  # Assuming field number 1 is the location description
                        return description
                except UnicodeDecodeError:
                    pass
        except Exception as e:
            print(f"Error extracting location description: {e}")
    return None

def process_urls(file_path):
    """
    Process URLs from the given file and decode the protobuf data.
    
    Args:
        file_path (str): The path to the file containing URLs.
    """
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines()]
        print(f"Read {len(urls)} URLs from file.")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return

    for url in urls:
        print(f"Processing URL: {url}")
        parsed_url = urllib.parse.urlparse(url)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        encoded_ug = query_params.get('ug', [None])[0]
        if encoded_ug:
            decoded_ug = urllib.parse.unquote(encoded_ug)
            print(f"Decoded URL parameter: {decoded_ug}")

            try:
                decoded_bytes = base64.urlsafe_b64decode(decoded_ug + '==')  # Add padding if needed
                print(f"Decoded bytes: {decoded_bytes}\n")

                # Extract location description
                location_description = extract_location_description(decoded_bytes)
                if location_description:
                    print(f"Guide Name: {location_description}")

                # Decode protobuf fields and collect Apple IDs
                apple_ids = decode_protobuf_fields(decoded_bytes)
                for i, apple_id in enumerate(apple_ids, start=1):
                    print(f" Apple Maps ID {i} : {apple_id}")
                print("\n")
            except Exception as e:
                print(f"Error decoding Base64 or parsing protobuf: {e}\n")
        else:
            print("No 'ug' parameter found.\n")

if __name__ == "__main__":
    process_urls('urls.txt')