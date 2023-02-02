import requests


def getting_json_from_web():
    file = requests.get("https://www.jsonkeeper.com/b/FGAS")
    file = file.json()
    return file


def finding_ides():
    list_of_id = []
    dates = []
    dict_of_dates = {}
    max_date = ['2019', '11', '00']
    file = getting_json_from_web()
    for index in file:
        if len(index) != 0 and index['state'] == "EXECUTED":
            date_month_num = index['date'].split('T')
            year_month_day = date_month_num[0].split('-')
            index_id = index['id']
            if year_month_day[0] == max_date[0] and year_month_day[1] >= max_date[1]:
                full_date = year_month_day[0] + year_month_day[1] + year_month_day[2]
                dates.append(full_date)
                dict_of_dates[full_date] = index_id

    dates.sort(reverse=True)
    dates = dates[0:6]
    while len(list_of_id) < 5:
        for ides in dates:
            list_of_id.append(dict_of_dates[ides])
    return list_of_id


def creating_classes_from_id(id_, name_of_typo, class_):
    file = getting_json_from_web()
    for item in file:
        if item['id'] == id_:
            time_data = item['date'].split('T')
            date_ = time_data[0].split('-')
            normal_date = f"{date_[2]}.{date_[1]}.{date_[0]}"
            disc = item['description']
            from_ = item['from']
            to = item['to']
            summ = item["operationAmount"]["amount"]
            cur = item["operationAmount"]["currency"]["name"]
            name_of_typo = class_(normal_date, disc, from_, to, summ, cur)
    return name_of_typo


def everything_for_class(id_):
    file = getting_json_from_web()
    for item in file:
        if item['id'] == id_:
            print(item)
            time_data = item['date'].split('T')
            date_ = time_data[0].split('-')
            normal_date = f"{date_[2]}.{date_[1]}.{date_[0]}"
            disc = item['description']
            if 'from' in item:
                from_ = item['from']
            to = item['to']
            summ = item["operationAmount"]["amount"]
            cur = item["operationAmount"]["currency"]["name"]
    return normal_date, disc, from_, to, summ, cur
