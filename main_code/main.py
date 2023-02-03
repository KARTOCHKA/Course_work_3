from sum_def import finding_ides, getting_json_from_web

file = getting_json_from_web()
list_of_id = finding_ides()
for idefic in list_of_id:
    for item in file:
        if len(item) != 0 and item['id'] == idefic:
            time_data = item['date'].split('T')
            date_ = time_data[0].split('-')
            normal_date = f"{date_[2]}.{date_[1]}.{date_[0]}"
            disc = item['description']
            if 'from' in item:
                from_ = item['from'].split(' ')
                if len(from_) == 3:
                    from_num = from_[2]
                    abs_from = f"{from_[0]} {from_[1]} {from_num[:4]} {from_num[4:6]}** **** {from_num[-4:]} -> "
                else:
                    from_num = from_[1]
                    abs_from = f"{from_[0]} {from_num[:4]} {from_num[4:6]}** **** {from_num[-4:]} -> "
            else:
                abs_from = ''
            to = item['to'].split(' ')
            num_of_trans = to[1]
            summ = item["operationAmount"]["amount"]
            cur = item["operationAmount"]["currency"]["name"]
            print(f"{normal_date} {disc}\n{abs_from}"
                  f"{to[0]} **{num_of_trans[-4:]}\n{summ} {cur}\n")
