# 치킨 한마리 -> 쿠폰 1개(+) 
# 쿠폰 10개 -> 서비스 치킨 1마리
# 서비스 치킨 1마리 -> 쿠폰 1개(+)
# coupon = chicken

def solution(chicken):
    s_chicken = 0
    coupon = chicken

    while coupon >= 10:                     # 쿠폰 10개 => 치킨 하나 
        new_chicken = coupon // 10          # 몇 마리 받을 수 있는지
        s_chicken += new_chicken            # 서비스 치킨 
        coupon = coupon % 10 + new_chicken  # 남은 구폰 + 새치킨 쿠폰 
    return s_chicken