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
    colored += Style.RESET_ALL
    print(colored)
    return colored

if __name__ == '__main__':
    # Example usage
    str_passwd = r"""25d8w5R=}%ggzsa1"""
    inputing = "A string with 123 and @#! characters &`"
    colored = print_passwd(str_passwd); print(colored, 'helloworld')
    colored = print_passwd(inputing); print(colored, 'helloworld')
