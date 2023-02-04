from main_code.sum_def import getting_json_from_web

test_link = "https://jsonkeeper.com/b/MBOG"


def test_getting_json_from_web():
    assert getting_json_from_web(test_link) == [{"key":"test","number":1234,"sort_str":"string","long_str":"long_string"},{"key1":"test1","number1":1}]
