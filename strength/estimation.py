import math


def calculate_password_entropy(passwd: str):
    return math.log2(len(set(passwd)) * len(passwd))
