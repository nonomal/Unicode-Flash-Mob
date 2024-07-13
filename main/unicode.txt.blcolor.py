# 定义文件名
filename = "processed_unicode.txt"

# 打开文件并读取数据
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 处理第一行，添加 ",0"
if ',' not in lines[0].strip():
    lines[0] = lines[0].rstrip() + ',0\n'
else:
    parts = lines[0].strip().split(',')
    if len(parts) < 3:
        print(f"第 1 行数据格式错误：{lines[0].strip()}")
    else:
        lines[0] = lines[0].rstrip() + ',"0"\n'

# 在文件末尾追加新数据行 ",0"
if lines[-1].strip() == "":
    lines[-2] = lines[-2].rstrip() + ',"0"\n'
else:
    lines[-1] = lines[-1].rstrip() + ',"0"\n'

# 在文件末尾追加新数据行 ",\"blcolor\""
new_line = ',\"blcolor\"\n'
lines.append(new_line)

# 处理每一行数据
for i in range(2, len(lines)):
    # 解析每行数据
    line = lines[i].strip()
    if ',' not in line:
        print(f"第 {i+1} 行数据格式错误：{line}")
        continue
    
    parts = line.split(',')
    if len(parts) < 3:
        print(f"第 {i+1} 行数据格式错误：{line}")
        continue
    
    unicode_code = parts[0].strip()
    font_dir = parts[1].strip()
    descriptions = ','.join(parts[2:]).strip()
    description_parts = descriptions.split('|')
    
    # 获取说明1部分
    if len(description_parts) > 0:
        description1 = description_parts[0]
    else:
        description1 = ""
    
    # 比较前两行的说明1部分
    prev_line = lines[i-1].strip()
    if ',' not in prev_line:
        print(f"第 {i} 行数据格式错误：{prev_line}")
        continue
    
    prev_parts = prev_line.split(',')
    if len(prev_parts) < 3:
        print(f"第 {i} 行数据格式错误：{prev_line}")
        continue
    
    prev_unicode_code = prev_parts[0].strip()
    prev_font_dir = prev_parts[1].strip()
    prev_descriptions = ','.join(prev_parts[2:]).strip()
    prev_description_parts = prev_descriptions.split('|')
    
    if len(prev_description_parts) > 0:
        prev_description1 = prev_description_parts[0]
    else:
        prev_description1 = ""
    
    # 更新前一行的blcolor值
    if description1 == prev_description1:
        lines[i-1] = lines[i-1].rstrip() + ',"0"\n'
    else:
        lines[i-1] = lines[i-1].rstrip() + ',"1"\n'

# 删除最后两行
del lines[-1:]

# 写回文件
with open(filename, 'w', encoding='utf-8') as file:
    file.writelines(lines)

print("数据处理完成并已写入文件。")