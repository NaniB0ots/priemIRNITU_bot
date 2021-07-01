from django.db.models import Q


def str_q_and(field: str, data: str):
    """
    Поиск в нужном поле, вхождения всех элементов списка
    """
    temp = data.split()
    data = []
    for item in temp:
        if len(item) > 3:
            item = item[:-2]
        data.append(item)

    list_len = len(data)
    if list_len == 1:
        return Q(**{field: data[0]})

    result = Q(**{field: data[0]}) & Q(**{field: data[1]})
    if list_len > 2:
        for i in range(2, list_len):
            result = result & Q(**{field: data[i]})
    return result