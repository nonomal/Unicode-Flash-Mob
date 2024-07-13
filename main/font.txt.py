import os
import re
import sys
from fontTools.ttLib import TTFont

def extract_unicode(font_path):
    font = TTFont(font_path)
    cmap = font.getBestCmap()

    unicode_list = []
    name = font['name']
    for record in name.names:
        if record.nameID == 4:
            font_name = record.toUnicode()
            break

    for codepoint, glyph_name in sorted(cmap.items()):
        unicode_hex = f"U+{codepoint:04X}"
        unicode_list.append((unicode_hex, font_name))

    return unicode_list

def write_to_file(unicode_list):
    existing_unicode = set()
    try:
        with open('unicode.txt', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    unicode_code = parts[0].strip()[1:-1]  # remove quotes
                    existing_unicode.add(unicode_code)
    except FileNotFoundError:
        pass

    with open('unicode.txt', 'a', encoding='utf-8') as f:
        for unicode_hex, font_name in unicode_list:
            if unicode_hex not in existing_unicode:
                f.write(f'"{unicode_hex}","{font_name}",\n')
                existing_unicode.add(unicode_hex)

def main():
    if '-i' not in sys.argv:
        print("请使用命令行参数 '-i' 指定字体文件。")
        return
    
    index = sys.argv.index('-i')
    font_files = sys.argv[index+1:]

    for font_file in font_files:
        unicode_list = extract_unicode(font_file)
        write_to_file(unicode_list)

    # 读取并排序unicode.txt文件中的内容
    with open('unicode.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 自定义排序函数，根据Unicode码位排序
    def unicode_sort_key(line):
        unicode_hex = line.split(',')[0].strip().strip('"')
        if unicode_hex.startswith('U+'):
            codepoint = int(unicode_hex[2:], 16)
            # 加入码位长度信息，确保5码字符在4码字符之后
            return (len(unicode_hex), codepoint)
        else:
            return (0, 0)  # 异常情况，放在最前面

    lines.sort(key=unicode_sort_key)

    with open('unicode.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)

if __name__ == '__main__':
    main()
