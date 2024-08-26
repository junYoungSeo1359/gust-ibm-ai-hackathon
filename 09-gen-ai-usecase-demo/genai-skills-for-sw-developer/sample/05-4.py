def remove_duplicates_and_sort(countries):
    return sorted(set(countries)) if countries else []

# 예제 입력 리스트
countries_list = ["France", "Italy", "Japan", "Germany", "Italy", "France", "Brazil", "Japan", "Canada", "Germany"]

# 중복 제거 및 정렬된 결과 출력
result = remove_duplicates_and_sort(countries_list)
print("중복 제거 및 정렬된 결과:")
print(result)
