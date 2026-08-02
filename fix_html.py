# DSA 잔재 코드(516~534번째 줄, 0-indexed: 515~533) 제거
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines before: {len(lines)}")

# 515번(0-indexed)부터 533번(0-indexed)까지 제거 (1-indexed: 516~534)
new_lines = lines[:515] + lines[534:]

print(f"Total lines after: {len(new_lines)}")
print(f"Line 514 (0-indexed): {new_lines[514].strip()[:80]}")
print(f"Line 515 (0-indexed): {new_lines[515].strip()[:80]}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done!")
