import re
import os
from rich import traceback

traceback.install(
    show_locals=True,
    extra_lines=2,
    max_frames=10
)

current_directory = os.getcwd()
MY1LBlocks = os.path.join(current_directory, 'assets', 'MY1LBlocks.yaml')

with open(MY1LBlocks, 'r', encoding='utf-8') as file:
    lines = file.readlines()

output_lines = []
for line in lines:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    match = re.search(r'([A-F0-9]+)\.\.([A-F0-9]+);\s(.+)', line)

    if match:
        start_range = int(match.group(1), 16)
        end_range = int(match.group(2), 16)
        description = match.group(3)

        for codepoint in range(start_range, end_range + 1):
            output_lines.append(f'"U+{codepoint:04X}","{description}"')

with open('assets/UnicodeMY1LBlocks.txt', 'w', encoding='utf-8') as output_file:
    for line in output_lines:
        output_file.write(line + '\n')
