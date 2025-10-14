import os
import secrets

# Hằng số cho các giới hạn của Unicode
UNICODE_MAX = 0x10FFFF
SURROGATE_START = 0xD800
SURROGATE_END = 0xDFFF

def generate_random_unicode_codepoint():
    """
    Tạo một số nguyên ngẫu nhiên, phân phối đều trong khoảng từ 0 đến 0x10FFFF.
    Hàm này sử dụng os.urandom() để đảm bảo tính ngẫu nhiên an toàn về mặt mật mã.
    """

    # 1. Xác định số byte cần thiết
    # Ta cần một số lớn hơn hoặc bằng 0x10FFFF (1,114,111)
    # 2 bytes = 2^16 = 65,536 (Không đủ)
    # 3 bytes = 2^24 = 16,777,216 (Đủ)
    num_bytes = 3 # 3 bytes là đủ để bao phủ toàn bộ phạm vi

    # Tính toán giá trị tối đa có thể được tạo ra từ num_bytes
    # Đây là giới hạn trên của trình tạo số ngẫu nhiên của chúng ta
    max_possible_val = (1 << (num_bytes * 8)) - 1 # Tương đương 2**(num_bytes*8) - 1

    # 2. Áp dụng kỹ thuật "Lấy mẫu loại bỏ" (Rejection Sampling)
    # Vòng lặp này đảm bảo chúng ta không tạo ra sự thiên vị (bias).
    # Chúng ta sẽ liên tục tạo một số ngẫu nhiên 3 byte cho đến khi
    # tìm được một số nằm trong phạm vi hợp lệ [0, UNICODE_MAX].
    while True:
        # Lấy 3 byte ngẫu nhiên an toàn
        random_bytes = os.urandom(num_bytes)

        # Ghép các byte lại để tạo thành một số nguyên lớn.
        # 'big' có nghĩa là byte đầu tiên là byte có trọng số lớn nhất (most significant).
        # ví dụ: b'\x01\x02\x03' -> 1*256^2 + 2*256^1 + 3*256^0
        random_int = int.from_bytes(random_bytes, 'big')

        # Nếu số được tạo ra nằm trong phạm vi mong muốn, hãy trả về nó.
        if random_int <= UNICODE_MAX:
            return random_int
        # Nếu không, vòng lặp sẽ tiếp tục và chúng ta thử lại.
        # Việc này loại bỏ các giá trị > UNICODE_MAX, đảm bảo mọi giá trị
        # từ 0 đến UNICODE_MAX đều có cùng một xác suất được chọn.

def generate_random_unicode_str(seq_len: int) -> str:
    print(f"Phạm vi Unicode hợp lệ: 0 đến {UNICODE_MAX} (hoặc 0x{UNICODE_MAX:X})")
    print("-" * 40)

    print("Tạo 10 mã code point Unicode ngẫu nhiên:")
    for i in range(seq_len):
        random_codepoint = generate_random_unicode_codepoint()
        # In ra dưới dạng số thập phân và thập lục phân
        print(f"Lần {i+1}: {random_codepoint:<7} (Hex: 0x{random_codepoint:X})")


def generate_random_unicode_character() -> str:
    """
    Tạo một ký tự Unicode đơn lẻ, ngẫu nhiên và an toàn về mặt mật mã.

    Hàm này sử dụng secrets.randbelow() để đảm bảo tính ngẫu nhiên an toàn.
    Nó cũng đảm bảo không bao giờ trả về một mã code point trong phạm vi
    surrogate (0xD800-0xDFFF), vốn không phải là các ký tự hợp lệ.

    Returns:
        str: Một chuỗi chứa một ký tự Unicode ngẫu nhiên.
    """
    while True:
        # 1. Tạo một số nguyên ngẫu nhiên trong toàn bộ phạm vi code point
        # secrets.randbelow(n) tạo số trong [0, n-1], vì vậy ta cần n = UNICODE_MAX + 1
        # để bao gồm cả 0x10FFFF.
        random_codepoint = secrets.randbelow(UNICODE_MAX + 1)

        # 2. Kiểm tra xem code point có nằm trong phạm vi surrogate không
        # Nếu nằm ngoài phạm vi không hợp lệ, nó là một ký tự hợp lệ.
        if not (SURROGATE_START <= random_codepoint <= SURROGATE_END):
            # 3. Chuyển đổi code point thành ký tự và trả về
            return chr(random_codepoint)

        # Nếu code point là một surrogate, vòng lặp sẽ tiếp tục và thử lại.
        # Việc này đảm bảo phân phối đều trên tất cả các ký tự hợp lệ.


def generate_random_unicode_string(length: int = 15) -> str:
    print(f"Tạo {length} ký tự Unicode ngẫu nhiên và an toàn:")
    print("-" * 50)

    for i in range(length):
        char = generate_random_unicode_character()
        # Lấy mã code point của ký tự để hiển thị
        codepoint = ord(char)

        # In ra ký tự cùng với mã code point (dạng thập phân và thập lục phân)
        # để dễ dàng kiểm tra và tham khảo.
        print(f"Ký tự {i+1}: '{char}' \t (Code: {codepoint:<7}, Hex: 0x{codepoint:X})")

if __name__ == "__main__":
    generate_random_unicode_string(15)
