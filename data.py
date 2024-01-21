import yaml
from openpyxl import load_workbook


def keywords():
    # 读取YAML文件
    with open("./setup.yaml", "r") as file:
        yaml_data = yaml.safe_load(file)

    # 遍历关键字列表
    keywords = yaml_data["keywords"]
    list = []
    for i in range(len(keywords)):
        list.append(keywords[i]["name"])

    return list


def get_date(i):
    # 读取YAML文件
    with open("./setup.yaml", "r") as file:
        yaml_data = yaml.safe_load(file)

    # 获取Excel文件路径
    excel_path = yaml_data["excel_path"]
    workbook = load_workbook(excel_path)

    # 遍历关键字列表
    keyword = yaml_data["keywords"]

    sheet_name = keyword[i]["sheet_name"]
    sheet = workbook[sheet_name]
    start_row = keyword[i]["start_add"]["row"]
    # 将excel中列的字母转换为数字
    start_col = keyword[i]["start_add"]["col"].upper()

    arr = []
    for i in sheet[start_col]:
        arr.append(i.value)

    # 去除前start_row行
    arr = arr[start_row - 1 :]

    # 去除空值
    arr = [x for x in arr if x is not None]
    # TODO:在这里我要添加一个对数字型的数据重排
    return arr


def bar_chart(arr, index):
    # arr去重复
    xAxis_data = list(set(arr))
    # 声明长度为xAxis_data长度的数组，用于存放y
    series_data = [0] * len(xAxis_data)
    for i in arr:
        for j in xAxis_data:
            if i == j:
                series_data[xAxis_data.index(j)] += 1
    # 读取YAML文件
    with open("./setup.yaml", "r") as file:
        yaml_data = yaml.safe_load(file)

    title_text = yaml_data["keywords"][index]["title"]
    series_name = yaml_data["keywords"][index]["name"]
    data = {
        "title": {"text": title_text},
        "tooltip": {},
        "legend": {"data": ["test"]},
        "xAxis": {"data": xAxis_data},
        "yAxis": {},
        "series": [{"name": series_name, "type": "bar", "data": series_data}],
    }
    return data


def pie_chart(arr, index):
    # arr去重复
    xAxis_data = list(set(arr))
    # 声明长度为xAxis_data长度的数组，用于存放y
    series_data = []
    for i in range(len(xAxis_data)):
        series_data.append({"name": xAxis_data[i], "value": 0})
    for i in arr:
        for j in xAxis_data:
            if i == j:
                series_data[xAxis_data.index(j)]["value"] += 1

    # 读取YAML文件
    with open("./setup.yaml", "r") as file:
        yaml_data = yaml.safe_load(file)

    title_text = yaml_data["keywords"][index]["title"]
    data = {
        "title": {"text": title_text},
        "series": [{"type": "pie", "data": series_data}],
    }
    return data


def rose_chart(arr, index):
    # arr去重复
    xAxis_data = list(set(arr))
    # 声明长度为xAxis_data长度的数组，用于存放y
    series_data = []
    for i in range(len(xAxis_data)):
        series_data.append({"name": xAxis_data[i], "value": 0})
    for i in arr:
        for j in xAxis_data:
            if i == j:
                series_data[xAxis_data.index(j)]["value"] += 1

    # 读取YAML文件
    with open("./setup.yaml", "r") as file:
        yaml_data = yaml.safe_load(file)

    title_text = yaml_data["keywords"][index]["title"]
    data = {
        "title": {"text": title_text},
        "series": [{"type": "pie", "data": series_data}],
        "roseType": "area",
    }
    return data


def type_chart(arr, index):
    # 读取YAML文件
    with open("./setup.yaml", "r") as file:
        yaml_data = yaml.safe_load(file)

    if yaml_data["keywords"][index]["chart_type"] == "bar":
        data = bar_chart(arr, index)
        return data

    if yaml_data["keywords"][index]["chart_type"] == "pie":
        data = pie_chart(arr, index)
        return data

    if yaml_data["keywords"][index]["chart_type"] == "rose":
        data = rose_chart(arr, index)
        return data


def main():
    arr = get_date(2)
    print(arr)
    # data = type_chart(arr, 2)
    # print(data)


if __name__ == "__main__":
    main()
