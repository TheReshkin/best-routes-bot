import requests

req= {
    "fromStationCode": "2000000",
    "fromStationNodeId": "5a323c29340c7441a0a556bb",
    "toStationCode": "2004000",
    "toStationNodeId": "5a3244bc340c7441a0a556ca",
    "departureDatetime": "2022-04-13",
    "count": 2
}



def railway_search(f_station, s_station, date, num=5):
    print("Railway")
    return railway_search()


def railway_search(inline_query, num=5):
    print("railway")
    code = 200
    if code == 200:
        return edit_answer_query(num)
    else:
        railway_search(inline_query)


def edit_answer_query(num):
    f_station = "Москва"
    s_station = "Санкт-Петербург"
    t_num = "1"
    # departure
    dep_date = "01.01.2022"
    dep_time = "09:00"
    # arrival
    arr_date = "01.01.2022"
    arr_time = "14:00"
    travel_time = "7:00"
    # купе
    coupe_seats = ""
    coupe_price = ""
    # плацкарт
    res_seats = ""
    res_price = ""
    # сидячий
    sit_seats = ""
    sit_price = ""
    link = "rzd.ru"
    if num > 0:
        answer = f"""🚆 {num}
        {f_station}➡️{s_station}
        Фирменный ✖️
        🕐 Отправление: {dep_time}  {dep_date}
        🕗 Прибытие: {arr_time}  {arr_date}
        ⏰ Время в пути: {travel_time}
        Купе: {coupe_seats} мест от {coupe_price} ₽
        Плацкартный: {res_seats} мест от {res_price} ₽
        Сидячий: {sit_seats} мест от {sit_price} ₽ 
        Ссылка: {link}""" + \
                 "\n" + \
                 edit_answer_query(num - 1) if num > 0 else """ """
    else:
        return ""
    return answer


def edit_answer():
    f_station = "Москва"
    s_station = "Санкт-Петербург"
    t_num = "1"
    # departure
    dep_date = "01.01.2022"
    dep_time = "09:00"
    # arrival
    arr_date = "01.01.2022"
    arr_time = "14:00"
    travel_time = "7:00"
    # купе
    coupe_seats = ""
    coupe_price = ""
    # плацкарт
    res_seats = ""
    res_price = ""
    # сидячий
    sit_seats = ""
    sit_price = ""
    link = "rzd.ru"

    answer = f"""🚆 {1}
    {f_station}➡️{s_station}
    Фирменный ✖️
    🕐 Отправление: {dep_time}  {dep_date}
    🕗 Прибытие: {arr_time}  {arr_date}
    ⏰ Время в пути: {travel_time}
    Купе: {coupe_seats} мест от {coupe_price} ₽
    Плацкартный: {res_seats} мест от {res_price} ₽
    Сидячий: {sit_seats} мест от {sit_price} ₽ 
    Ссылка: {link}"""
    return answer
