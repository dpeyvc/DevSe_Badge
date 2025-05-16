# 기존 SVG 로고 파일 경로
original_logo_path = "logo/gaonnuri_color.svg"
# 흰색으로 바꾼 SVG 저장 경로
modified_logo_path = "logo/gaonnuri_white.svg"

# SVG 내용 불러와서 색상 교체
with open(original_logo_path, "r", encoding="utf-8") as f:
    svg_content = f.read()

# 검정색 → 흰색으로 변경 (대소문자 포함)
svg_content = (
    svg_content.replace("#000000", "#ffffff")
               .replace("black", "white")
               .replace("#000", "#fff")
)

# 변경된 SVG 저장
with open(modified_logo_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

modified_logo_path
