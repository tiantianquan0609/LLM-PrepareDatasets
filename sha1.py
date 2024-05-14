import hashlib

def calculate_sha1(file_path):
    sha1 = hashlib.sha1()
    try:
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(8192)  # Read in chunks to handle large files
                if not data:
                    break
                sha1.update(data)
        return sha1.hexdigest()
    except FileNotFoundError:
        return "File not found."

# 使用示例
file_path = './outputdataset/glm-baiwen_converted_data.json'  # 替换为您的文件路径
sha1_hash = calculate_sha1(file_path)
print("SHA-1 Hash:", sha1_hash)

#file_path = './outputdataset/glm-baiwen_converted_data.json' SHA-1 Hash: 279b6f29034e07e556f5d09c7853dfbe5ce30df6