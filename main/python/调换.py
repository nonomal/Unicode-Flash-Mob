from rich import traceback

traceback.install(
    show_locals=True,
    extra_lines=2,
    max_frames=10
)

with open('MY1LBlocks1.yaml', 'r', encoding='utf-8') as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    if "F; " in line:
        index = line.index("F; ")
        left = line[:index + 3]
        right = line[index + 3:]
        if "|" in right:
            left_part, right_part = right.split("|")
            new_line = left + right_part.strip() + "|" + left_part.strip() + "\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open('MY1LBlocks1_updated.yaml', 'w', encoding='utf-8') as file:
    file.writelines(new_lines)