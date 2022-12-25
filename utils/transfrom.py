
# 前置条件： 数据库文件导出为json格式，
# [
#     {
#         "task_id": 123,
#         "task_name": "abv",
#         "task_type": "SQL"
#     }
# ]

# json数组导入elasticsearch, 转换为bulk_api需要的格式
def transform_to_es_json(json_file, save_file, my_index, my_type, start_id=1):
    import json

    # Read the JSON array from a file
    with open(json_file, "r") as f:
        data = json.load(f)

    # Generate the bulk request format
    bulk_request = ""
    for doc in data:
        bulk_request += json.dumps({"index": {"_index": my_index, "_type": my_type, "_id": start_id}}) + "\n"
        bulk_request += json.dumps(doc) + "\n"
        start_id += 1

    bulk_request += "\n"

    with open(save_file, "w") as f:
        f.write(bulk_request)
    print(f"save {save_file} success")


if __name__=='__main__':
    json_file = "/Users/lance2.1/Desktop/simple.json"
    save_file = "/Users/lance2.1/Desktop/s.json"
    my_index = "s_task"
    my_type = "t"
    transform_to_es_json(json_file, save_file, my_index, my_type)
