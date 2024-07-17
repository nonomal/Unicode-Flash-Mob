import re
import os
from rich import traceback

traceback.install(
    show_locals=True,
    extra_lines=2,
    max_frames=10
)

current_directory = os.getcwd()
UData = os.path.join(current_directory, 'assets', 'UData.txt')

with open(UData, 'r', encoding='utf-8') as f, open('assets/UnicodeData.txt', 'w', encoding='utf-8') as out:

    start = end = None

    for line in f:
        code_point = int(line.split(';')[0], 16)

        if "First" in line:
            start = code_point
            desc = re.sub(r'[<>,]| First', '', line.split(';')[1])

        elif "Last" in line:
            end = code_point
            desc = re.sub(r'[<>,]| Last', '', line.split(';')[1])

            if start and end:
                for cp in range(start, end+1):
                    out.write(f'"U+{cp:04X}","{desc}-{cp:04X}"\n')
                start = end = None

        else:
            desc = line.split(';')[1]
            if desc:
                out.write(f'"U+{code_point:04X}","{desc}"\n')
            else:
                out.write(f'"U+{code_point:04X}"\n')
