def find_max_min(lst):
    if not lst:
        return None, None  # 빈 리스트일 경우 None 반환
    
    max_value = lst[0]
    min_value = lst[0]
    
    for num in lst:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    
    return max_value, min_value

# 예시 리스트
my_list = [3, 1, 7, 4, 2, 8, 5]

# 최대 및 최소 요소 찾기
max_elem, min_elem = find_max_min(my_list)

print(f"리스트 {my_list}에서 최대 값은 {max_elem}, 최소 값은 {min_elem}입니다.")
