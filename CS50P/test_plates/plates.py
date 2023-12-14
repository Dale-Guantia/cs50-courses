def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for char in s:
            if char.isdigit():
                c = s.index(char)
                if s[c:].isdigit() and char != "0":
                    return True
                else:
                    return False
        return True

    else:
        return False


if __name__ == "__main__":
    main()