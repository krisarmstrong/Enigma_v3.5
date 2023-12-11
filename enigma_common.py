
"""
This module contains global variables and lists used for encoding and decoding in the Enigma machine.
"""

n0, n9, nA, nZ = b'09A'

# Encode Enigma Rotors 10 & 26
encode_rotor_10 = [5, 4, 1, 8, 7, 3, 0, 2, 9, 6]
encode_rotor_26 = [16, 8, 25, 5, 23, 21, 18, 17, 2, 1, 7, 24, 15, 11, 9, 6, 3, 0, 19, 12, 22, 14, 10, 4, 20, 13]

# Decode Enigma Rotors 10 & 26 - Inverse of encode
decode_rotor_10 = [6, 2, 7, 5, 1, 0, 9, 4, 3, 8]
decode_rotor_26 = [17, 9, 8, 16, 23, 3, 15, 10, 1, 14, 22, 13, 19, 25, 21, 12, 0, 7, 6, 18, 24, 5, 20, 4, 11, 2]