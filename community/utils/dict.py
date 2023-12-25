"""
주어진 딕셔너리 리스트에서 특정 키에 해당하는 값들만을 추출하여 새로운 딕셔너리 리스트를 생성합니다.

Parameters:
data (list of dict): 처리할 딕셔너리들이 담긴 리스트.
keys (list of str): 추출할 키들의 리스트.

Returns:
list of dict: 각 딕셔너리에서 주어진 키에 해당하는 값들만을 포함하는 새로운 딕셔너리 리스트.

예시:
>>> data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
>>> keys = ['a']
>>> extract_keys_from_dict_list(data, keys)
[{'a': 1}, {'a': 3}]
"""


def extract_keys_from_dict_list(data, keys):
    return [{key: item.get(key) for key in keys} for item in data]
