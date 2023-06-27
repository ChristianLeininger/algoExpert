# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 26.06.2023


from typing import List


def validIPAddresses(string: str) -> List[str]:
    """ create all valid ip addresses of given string
    Assume: string only contains numbers and length is 12

    Args:
        param1: string
    Return: list of valid ip addresses
    """

    valid_ip_addresses = []
    # first part can be 1 to 3 digits
    for i in range(1, min(len(string), 4)):
        current_ip_address_parts = ["", "", "", ""]
        current_ip_address_parts[0] = string[:i]
        # import pdb; pdb.set_trace()
        # check if first part is valid
        if not valid_number(int(current_ip_address_parts[0])) or not check_string(current_ip_address_parts[0]):
            # if not valid no need to check the rest
            continue
        # second part can be 1 to 3 digits
        for j in range(i + 1, i + min(len(string) - i, 4)):
            current_ip_address_parts[1] = string[i:j]
            if not valid_number(int(current_ip_address_parts[1])) or not check_string(current_ip_address_parts[1]):
                # if not valid no need to check the rest

                continue
            # if the first two parts are valid check the rest
            for k in range(j + 1, j + min(len(string) - j, 4)):
                # the rest needs to be split in two parts
                current_ip_address_parts[2] = string[j:k]
                current_ip_address_parts[3] = string[k:]
                # check if both parts are valid
                part1_valid = valid_number(int(current_ip_address_parts[2])) and check_string(current_ip_address_parts[2])
                part2_valid = valid_number(int(current_ip_address_parts[3])) and check_string(current_ip_address_parts[3])
                if part1_valid and part2_valid:
                    # now we have four valid parts and can add it to the list
                    valid_ip_addresses.append(".".join(current_ip_address_parts))
    return valid_ip_addresses


def valid_number(value: int) -> bool:
    """ check if value is between 0 and 255
    Args:
        param1(int): value
    Return: bool true if value is between 0 and 255
    """
    return value >= 0 and value <= 255


def check_string(s: str) -> bool:
    """ check for leading zeros
    Args:
        param1(str): string
    Return: bool true if no leading zeros
    """
    if len(s) > 1 and s[0] == '0':
        return False
    return True


if __name__ == "__main__":
    string = "1921680"
    string = "10110110"
    string = "17216211"
    string = "100100"
    string = "00010"
    # string = "88881234"
    print(validIPAddresses(string))
    print(len(validIPAddresses(string)))
