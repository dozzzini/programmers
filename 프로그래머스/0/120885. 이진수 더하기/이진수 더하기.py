def solution(bin1, bin2):

    # 1. 이진수 -> 십진수 
    # ex) 1101 -> (1 * 2^3) +(1 * 2^2) + (0 * 2^1) + (1 * 2^0)
    def binary_to_decimal(binary_str):
        decimal = 0 # 10진수를 0으로 초기세팅
        power = 1   # 2의0승(2) * 1 = 1
        for ch in binary_str[::-1]:
            if ch == '1':
                decimal += power
            power *= 2
        return decimal

    # 2. 십진수 -> 이진수
    def decimal_to_binary(n):
        if n == 0:
            return "0"
        result = ""
        while n > 0:
            result = str(n % 2) + result
            n //= 2
        return result

    # 이진수 두 개 → 십진수로 변환 후 더함
    dec1 = binary_to_decimal(bin1)
    dec2 = binary_to_decimal(bin2)
    total = dec1 + dec2

    # 다시 이진수로 변환
    return decimal_to_binary(total)
