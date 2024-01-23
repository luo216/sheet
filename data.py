import yaml
from openpyxl import load_workbook


def read_yaml():
    # 读取YAML文件
    with open("./setup.yaml", "r", encoding="utf-8") as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data


def get_other_data(keywords, data, i):
    data["chart_type"] = keywords[i]["chart_type"]
    # 如果有other属性，则将其赋值给data
    if "other" in keywords[i]:
        data["other"] = keywords[i]["other"]


def keywords():
    yaml_data = read_yaml()
    # 遍历关键字列表
    keywords = yaml_data["keywords"]
    list = []
    for i in range(len(keywords)):
        list.append(keywords[i]["name"])

    return list


def data_transform_int(arr):
    # 尝试将arr中的元素转换为int类型
    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i])
        except ValueError:
            print("请注意：arr中存在非int类型的元素")
            arr[i] = None

    # 将arr中的none元素删除
    arr = [x for x in arr if x is not None]
    # 排序
    arr.sort()

    return arr


def summarize_classification_int(keyword, i, arr):
    interval = keyword[i]["int"]["interval"]
    zero_show = keyword[i]["int"]["zero_show"]
    start_num = arr[0] - arr[0] % interval
    end_num = arr[-1] - arr[-1] % interval + interval
    newarr = []

    for i in range(start_num, end_num, interval):
        name = str(i) + "-" + str(i + interval)
        newarr.append([name, 0])
        for j in arr:
            if j >= i and j <= i + interval:
                newarr[-1][1] += 1

    if zero_show:
        pass
    else:
        # 去除元素中为0的
        newarr = [x for x in newarr if x[1] != 0]

    return newarr


def summarize_classification(arr):
    # arr去重复
    xAxis_data = list(set(arr))
    # 声明长度为xAxis_data长度的数组，用于存放y
    series_data = [0] * len(xAxis_data)
    for i in arr:
        for j in xAxis_data:
            if i == j:
                series_data[xAxis_data.index(j)] += 1

    # 创建一个二维数组来存储
    arr = []
    for i in range(len(xAxis_data)):
        arr.append([xAxis_data[i], series_data[i]])

    return arr


def data_type_judge(keyword, i, arr):
    data_type = keyword[i]["data_type"]
    if data_type == "default":
        arr = summarize_classification(arr)

        return arr
    else:
        if data_type == "int":
            arr = data_transform_int(arr)
            arr = summarize_classification_int(keyword, i, arr)
            return arr


def get_date(data, i):
    yaml_data = read_yaml()
    # 获取Excel文件路径
    excel_path = yaml_data["excel_path"]
    workbook = load_workbook(excel_path)

    # 遍历关键字列表
    keyword = yaml_data["keywords"]

    # 这里可以配置一些无关紧要的参数
    get_other_data(keyword, data, i)

    sheet_name = keyword[i]["sheet_name"]
    sheet = workbook[sheet_name]
    start_row = keyword[i]["start_add"]["row"]
    # 将excel中列的字母转换为数字
    start_col = keyword[i]["start_add"]["col"].upper()

    arr = []
    for cell in sheet[start_col]:
        arr.append(cell.value)

    # 去除前start_row行
    arr = arr[start_row - 1 :]

    # 去除空值
    arr = [x for x in arr if x is not None]

    arr = data_type_judge(keyword, i, arr)

    data["data"] = arr


def main():
    data = {}
    get_date(data, 4)
    print(data)


if __name__ == "__main__":
    main()
