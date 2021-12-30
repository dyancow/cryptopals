import base64

def convertHexToBinary(val):
    try:
        bytesHex = bytes.fromhex(val)
        return bytesHex
    except ValueError:
        return


def convertBinaryToBase64(bin):
    try:
        b64bin = base64.b64encode(bin).decode()
        return b64bin
    except ValueError:
        return


def hex_to_base64(hexInt):
    hexBin = convertHexToBinary(hexInt)  # only work in binary
    if hexBin is None:
        print("Invalid hex")
        return
    converted = convertBinaryToBase64(hexBin)
    if converted is None:
        print("Invalid conversion")
        return
    return str(converted)


if __name__ == '__main__':
    exampleHexVal = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    exampleB64Val = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    actual = hex_to_base64(exampleHexVal)
    if actual == exampleB64Val:
        print("Passed example")
    else:
        print("Failed")
