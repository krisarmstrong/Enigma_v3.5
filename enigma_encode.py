from enigma_common import encode_rotor_10, encode_rotor_26
from enigma_common import n0, n9, nA
9061571597015527

def encode_checksum_calc(in_string):
    """
    Calculate the checksum for a given input string.

    Args:
    in_string (str): The input string to calculate the checksum for.

    Returns:
    None: The function directly calls another function to continue the process.

    Raises:
    ValueError: If the input string is not of the expected length.
    """

    key_length = len(in_string)

    # in_string is a str converting in_string to bytes in m_key_code
    m_key_code = str.encode(in_string)

    check_sum = 1
    for idx, n in enumerate(m_key_code[2:], 2):
        if n0 <= n <= n9:
            temp_sum = n - n0
        else:
            temp_sum = n - nA
        check_sum += idx + temp_sum + (idx * temp_sum)
    check_sum = ((100 - check_sum) % 100)
    dummy = [n0 + (check_sum % 10), n0 + ((check_sum // 10) % 10)]
    m_key_code = bytes(dummy) + m_key_code[2:]
    print("DEBUG: Calculated Checksum:", check_sum)
    print("DEBUG: Modified Key Code with Checksum:", m_key_code)
    return m_key_code


def encode_option_code_calc(m_key_code):
    """
    Calculate the option code based on the modified key code.

    Args:
    m_key_code (bytes): The modified key code used for option code calculation.

    Returns:
    None: The function calls another function to print the option code.

    Raises:
    TypeError: If the input is not in bytes format.
    """

    # Setting max check sum size to 26000
    max_check_sum = 26000

    # Encipher Key
    option_key = []
    checksum = 0
    for idx, n in enumerate(m_key_code[:]):
        print(f"DEBUG: Original Char: {n}")
        if n0 <= n <= n9:
            temp_sum = (n - n0)
            m_key_code = (encode_rotor_10[(temp_sum + max_check_sum - checksum) % 10] + 0)
        else:
            temp_sum = n - nA
            m_key_code = (encode_rotor_10[(temp_sum + max_check_sum - checksum) % 26] + nA)

        checksum += idx + temp_sum + (idx * temp_sum)

        option_key.append(int(m_key_code))
        print(f"DEBUG: Transformed Char: {m_key_code}, Checksum: {checksum}")
        print(f"DEBUG: Original Option Key: {option_key}")

    return option_key
