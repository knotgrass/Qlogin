from colorama import Fore, Style



def print_passwd(str_passwd:str) -> str:
    colored = ""
    for char in str_passwd:
        if char.isdigit():
            colored += f"{Fore.BLUE}{char}"
        elif char.isalpha():
            colored += f"{Fore.WHITE}{char}"
        else:
            colored += f"{Fore.RED}{char}"

    print(colored + Style.RESET_ALL)
    return colored

if __name__ == '__main__':
    # Example usage
    str_passwd = r"""25d8w5R=}%ggzsa"""
    inputing = "A string with 123 and @#! characters"
    print_passwd(str_passwd)
    print_passwd(inputing)
