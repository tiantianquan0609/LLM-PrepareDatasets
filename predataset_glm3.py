import json

# 假设这是你的原始数据文件路径
original_data_file = './jsondataset/glm-baiwen.json'

# 读取原始 JSON 数据
with open(original_data_file, 'r', encoding='utf-8') as file:
    original_data = json.load(file)

# 创建自定义数据集格式
custom_dataset = []

# 遍历原始数据中的每个对象
for item in original_data:
    # 提取并处理 title 和 content 字段
    instruction = item.get("title", "用户指令（必填）")  # 如果缺少 title，则使用默认值
    #content = item.get("content", "").strip()[:300] + "..."  # 如果缺少 content，则使用空字符串，并截取前300个字符
    content = item.get("content", "模型回答（必填）") # 如果缺少 content，则使用空字符串，并截取前300个字符

    # 构建新的数据结构
    new_item = {
        "instruction": instruction,
        "input": "",
        "output": content,
        "history": [] # 初始化对话历史为空列表，可以在后续处理中填充
    }

    # 将新构建的对象添加到自定义数据集中
    custom_dataset.append(new_item)

# 将自定义数据集写入新的 JSON 文件
output_file = './outputdataset/glm-baiwen_converted_data.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(custom_dataset, file, ensure_ascii=False, indent=2)

print(f"数据转换完成，并已保存到 {output_file} 文件中。")