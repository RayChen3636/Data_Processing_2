import json

# r 讀取為預設
file = open("空氣品質小時值_桃園市_中壢站.json",encoding="utf-8")
json_text = file.read()
print(json_text)
# print(type(json_text))

# json 文字 轉換成 物件資料
data = json.loads(json_text)
print(data)
print(type(data))
print(data[0]["ItemEngName"])


# Q 找出 PM2.5 的資料並輸出成 json文字檔案
PM25_list = []

for d in data:
    # print(d)
    if d["ItemEngName"] == "PM2.5":
        PM25_list.append(d)
        #print(PM25_list)

json_text = json.dumps(PM25_list,ensure_ascii=False)
print(json_text)
file = open("output.json","w",encoding="utf-8")
file.write(json_text)
# file.write(json.dumps(PM25_list,ensure_ascii=False))
# \"28"\ == "28" 輸出格式略有不同
file.close()


#Q 找出 PM2.5 在哪個時間濃度最高?

# max_dict = None
#
# for d in PM25_list:
#     if max_dict == None:
#         max_dict = d
#     try:
#         if int(d["Concentration"]) > int(max_dict["Concentration"]):
#             max_dict = d
#             # print(max_dict)
#     except ValueError:
#         # 以整數int()檢測
#         print("資料破損:",d)
#
# print("資料完整:",max_dict)
# print(max_dict["MonitorDate"])

