import operator
from typing import Any, Dict, List, Type


def find_one_node(
    search_list: List, property_name: str, search_keyword: Any
) -> Type or Dict or None:
    """list of class 에서 property_name 값이 search_keyword인 첫 번째 노드를 리턴

    Args:
        property_name (str): 검색할 class의 property 이름
        search_keyword (object): 검색할 값

    Returns:
        List: 검색된 노드 리스트
    """

    for x in search_list:
        if type(x) is dict:
            if x[property_name] == search_keyword:
                return x
        else:
            if getattr(x, property_name) == search_keyword:
                return x

    return None


def find_all_node(search_list: List, property_name: str, search_keyword: Any) -> List:
    """list of class 에서 property_name 값이 search_keyword인 첫 번째 노드를 리턴

    Args:
        property_name (str): 검색할 class의 property 이름
        search_keyword (object): 검색할 값

    Returns:
        List: 검색된 노드 리스트
    """
    list_result = []
    for x in search_list:
        if type(x) is dict:
            if x[property_name] == search_keyword:
                list_result.append(x)
        else:
            if getattr(x, property_name) == search_keyword:
                list_result.append(x)

    return list_result


def contains_node(search_list: List, property_name: str, search_keyword: Any) -> bool:
    """list of class 에서 property_name 값이 search_keyword인 노드가 존재하면 True, 아니면 False 리던

    Args:
        property_name (str): 검색할 class의 property 이름
        search_keyword (object): 검색할 값

    Returns:
        bool: 검색 결과
    """

    def contains(list, filter, filter_dict):
        for x in list:
            if type(x) is dict:
                if filter_dict(x):
                    return True
            else:
                if filter(x):
                    return True
        return False

    return contains(
        search_list,
        lambda x: getattr(x, property_name) == search_keyword,
        lambda x: x[property_name] == search_keyword,
    )


def list_sort(sort_list: List, property_name: str, reverse: bool = False) -> None:
    """리스트 정렬

    Args:
        property_name (str): 정렬할 class의 property 이름
        reverse (bool, optional): False - 오름차순, True - 내림차순. Defaults to True.
    """
    return sorted(sort_list, key=operator.attrgetter(property_name), reverse=reverse)
