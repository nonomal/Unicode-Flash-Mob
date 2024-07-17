import os
from rich import traceback

traceback.install(
    show_locals=True,
    extra_lines=2,
    max_frames=10
)

def main():
    current_directory = os.getcwd()
    unicode_file = os.path.join(current_directory, 'unicode.txt')
    blocks_file = os.path.join(current_directory, 'python', 'assets', 'UnicodeMY1LBlocks.txt')
    unicode_data_file = os.path.join(current_directory, 'python', 'assets', 'UnicodeData.txt')
    output_file = os.path.join(current_directory, 'processed_unicode.txt')

    # 读取UnicodeMY1LBlocks.txt文件内容，构建映射字典
    print(f'构建映射字典中，请等待...')
    block_map = {}
    with open(blocks_file, 'r', encoding='utf-8') as blocks:
        for line in blocks:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) >= 2:
                    unicode_char = parts[0].strip().strip('"')
                    description = parts[1].strip().strip('"')
                    block_map[unicode_char] = description

    # 读取UnicodeData.txt文件内容，构建映射字典
    unicode_data_map = {}
    with open(unicode_data_file, 'r', encoding='utf-8') as unicode_data:
        for line in unicode_data:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) >= 2:
                    unicode_char = parts[0].strip().strip('"')
                    other_description = parts[1].strip().strip('"')
                    unicode_data_map[unicode_char] = other_description

    # 处理unicode.txt文件，写入到processed_unicode.txt中
    print(f'处理中，请等待...')
    with open(unicode_file, 'r', encoding='utf-8') as unicode, \
         open(output_file, 'w', encoding='utf-8') as output:
        
        for line in unicode:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) >= 2:
                    unicode_char = parts[0].strip().strip('"')
                    font_directory = parts[1].strip().strip('"')
                    
                    # 查找对应的说明信息
                    if unicode_char in block_map:
                        description = block_map[unicode_char]
                    else:
                        description = ''

                    # 查找对应的UnicodeData信息
                    if unicode_char in unicode_data_map:
                        other_description = unicode_data_map[unicode_char]
                    else:
                        other_description = ''

                    # 构建新行并写入文件
                    new_line = f'"{unicode_char}","{font_directory}","{description}|{other_description}"\n'
                    output.write(new_line)
                else:
                    output.write(line + '\n')

    print(f'处理完成，结果保存在 {output_file}')

if __name__ == '__main__':
    main()