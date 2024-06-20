import yaml

data = {
    'name': 'Example',
    'details': {
        'age': 30,
        'city': 'New York'
    },
    'skills': [
        'Python',
        'YAML',
        'Docker'
    ]
}


# 将数据写入 YAML 文件
with open('output.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False, sort_keys=False)

print("YAML 文件已生成")