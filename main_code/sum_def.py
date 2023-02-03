import requests


def getting_json_from_web():
    file = requests.get("https://www.jsonkeeper.com/b/FGAS")
    file = file.json()
    return file


def finding_ides():
    list_of_id = []
    dates = []
    dict_of_dates = {}
    file = getting_json_from_web()
    for index in file:
        if len(index) != 0 and index['state'] == "EXECUTED":
            date_month_num = index['date'].split('T')
            year_month_day = date_month_num[0].split('-')
            index_id = index['id']
            full_date = year_month_day[0] + year_month_day[1] + year_month_day[2]
            dates.append(full_date)
            dict_of_dates[full_date] = index_id

    dates.sort(reverse=True)
    dates = dates[0:5]
    while len(list_of_id) < 5:
        for ides in dates:
            list_of_id.append(dict_of_dates[ides])
    return list_of_id

print(finding_ides())