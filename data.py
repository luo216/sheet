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
    start_col = keyword[i]["start_add"]["col"]
    length = keyword[i]["length"]

    arr = []
    for i in range(length):
        arr.append(sheet.cell(row=start_row + i, column=start_col).value)

    # 去除空值
    arr = [x for x in arr if x is not None]
    return arr


def main():
    print(keywords())
    print(get_date(0))


if __name__ == "__main__":
    main()
