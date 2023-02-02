import requests
from datetime import date




def make_class_from_file():
    list_of_id = []
    dates = []
    used_id = []
    id_for_class = 0
    dict_of_dates ={}
    file = requests.get("https://www.jsonkeeper.com/b/FGAS")
    file = file.json()
    max_date = ['2019', '11', '00']
    for index in file:
        if len(index) != 0:
            date_month_num = index['date'].split('T')
            year_month_day = date_month_num[0].split('-')
            index_id = index['id']
            # print(year_month_day)
            # print(index_id)
            if year_month_day[0] == max_date[0] and year_month_day[1] >= max_date[1]:
                full_date = year_month_day[0] + year_month_day[1] + year_month_day[2]
                dates.append(full_date)
                dates.sort(reverse=True)
                dict_of_dates[full_date] = index_id
                print(dict_of_dates)
                print(dates)
    dates = dates.pop(5)
    while len(list_of_id) < 5:
        for ides in dates:
            list_of_id.append(dict_of_dates[ides])
    print(list_of_id)
    return list_of_id



make_class_from_file()
