def remove_duplicates_and_sort(countries):
    unique_countries = sorted(set(countries))  # 중복 제거 후 정렬
    return unique_countries

# 예제 입력 리스트
countries_list = ["France", "Italy", "Japan", "Germany", "Italy", "France", "Brazil", "Japan", "Canada", "Germany"]

# 중복 제거 및 정렬된 결과 출력
result = remove_duplicates_and_sort(countries_list)
print("중복 제거 및 정렬된 결과:")
print(result)
