# requirements.txt 파일 읽기
with open('requirements.txt', 'r') as f:
    lines = f.readlines()

# @ file:/// 경로 제거
cleaned_lines = []
for line in lines:
    if '@ file:///' in line:
        # 패키지 이름과 버전 추출
        cleaned_line = line.split('@')[0].strip()
        cleaned_lines.append(cleaned_line)
    else:
        cleaned_lines.append(line.strip())

# 새 파일로 저장
with open('cleaned_requirements.txt', 'w') as f:
    f.write('\n'.join(cleaned_lines))

print("경로가 제거된 requirements.txt 파일 생성 완료!")
