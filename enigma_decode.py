# enigma_decode.py

from enigma_common import decode_rotor_10, decode_rotor_26
from enigma_common import n0, n9, nA, nZ


def decode(encoded_option_code):
    # Convert the encoded option code to bytes
    encoded_bytes = bytes(encoded_option_code, 'utf-8')

    # Validate the checksum
    if not decode_checksum_calc(encoded_bytes):
        print("Invalid checksum.")
        return None, None  # Return a tuple of None values

    # Continue with the decoding process...
    decoded_data = decode_with_rotor_10(encoded_bytes)
    original_key = decode_with_rotor_26(decoded_data)

    # Return the decoded data and the original key
    return decoded_data, original_key


def decode_with_rotor_10(encoded_data):
    decoded_data = ''
    checksum = 0
    for idx, char in enumerate(encoded_data):
        str_char = chr(char)  # Convert byte to its character representation
        if str_char.isdigit():
            byte_val = ord(str_char)  # Convert character to its ASCII value
            adjusted_val = (byte_val - n0) % 10  # Reverse the transformation
            decoded_val = decode_rotor_10[adjusted_val]

            # Adjust for the checksum effect (if applicable)
            temp_sum = decoded_val
            checksum += idx + temp_sum + (idx * temp_sum)

            print(f"DEBUG: idx={idx}, char={char}, byte_va{byte_val}, adjusted_val={adjusted_val}, decoded_val={decoded_val}, temp_sum={temp_sum}, checksum={checksum}")

            # Add the decoded value to the decoded data
            decoded_data += str(decoded_val)
        else:
            decoded_data += str_char  # Non-digit characters are left as is
    return decoded_data


def decode_with_rotor_26(encoded_data):
    """
    Calculate the original key code based on the option key for rotor 26.

    Args:
    encoded_data (list): The encoded data used for original key code calculation.

    Returns:
    list: The original key code.

    Raises:
    TypeError: If the input is not in list format.
    """

    # Setting max check sum size to 26000
    max_check_sum = 26000

    # Decipher Key
    original_key = []
    checksum = 0
    for idx, n in enumerate(encoded_data[:]):
        if nA <= n <= nZ:
            temp_sum = n - nA
            original_key_code = (decode_rotor_26[(temp_sum + max_check_sum - checksum) % 26] + nA)
            checksum += idx + temp_sum + (idx * temp_sum)
            original_key.append(int(original_key_code))

    return original_key


def decode_checksum_calc(encoded_string):
    """
    Validate the checksum for a given encoded string.

    Args:
    encoded_string (bytes): The encoded string to validate the checksum for.

    Returns:
    bool: True if the checksum is valid, False otherwise.
    """

    # Extract the checksum from the encoded string
    extracted_checksum = (encoded_string[1] - n0) * 10 + (encoded_string[0] - n0)

    # Calculate the checksum for the remaining string
    check_sum = 1
    for idx, n in enumerate(encoded_string[2:], 2):
        if n0 <= n <= n9:
            temp_sum = n - n0  # Reverse the transformation
        else:
            temp_sum = n - nA
        check_sum += idx + temp_sum + (idx * temp_sum)
        print(f"DEBUG: idx={idx}, n={n}, temp_sum={temp_sum}, check_sum={check_sum}")  # Debug statement

    check_sum = ((100 - check_sum) % 100)

    print("DEBUG: Extracted Checksum:", extracted_checksum)
    print("DEBUG: Calculated Checksum:", check_sum)

    # Return True if the calculated checksum matches the extracted checksum
    return check_sum == extracted_checksum