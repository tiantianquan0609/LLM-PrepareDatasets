import json

# 假设这是你的原始数据文件路径
original_data_file = './jsondataset/trainByZhong.json'

# 初始化自定义数据集格式
custom_dataset = []

# 打开文件并逐行读取
with open(original_data_file, 'r', encoding='utf-8') as file:
    for line in file:
        # 尝试解析每一行作为独立的JSON对象
        try:
            item = json.loads(line)
            # 提取并处理字段
            instruction = item.get("prompt", "用户指令（必填）")
            content = item.get("response", "模型回答（必填）")

            # 构建新的数据结构
            new_item = {
                "instruction": instruction,
                "input": "",
                "output": content,
                "history": []  # 初始化对话历史为空列表，可以在后续处理中填充
            }

            # 将新构建的对象添加到自定义数据集中
            custom_dataset.append(new_item)
        except json.JSONDecodeError:
            # 如果某一行不是有效的JSON，打印错误信息并跳过该行
            print(f"Error decoding JSON on line: {line}")
            continue

# 将自定义数据集写入新的 JSON 文件
output_file = './outputdataset/trainByZhong_converted_data.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(custom_dataset, file, ensure_ascii=False, indent=2)

print(f"数据转换完成，并已保存到 {output_file} 文件中。")