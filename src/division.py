import base64

def generate_svg_badge_with_embedded_logo(
    output_path="badge/division_badge.svg",
    label="Division",
    badge_color="#000000",
    text_color="#ffffff",
    logo_file_path="logo/division.svg"  # 반드시 로컬 SVG 파일
):
    # SVG 배지 사이즈 설정
    badge_width = 92
    badge_height = 28
    logo_height = 22
    logo_x = 4
    logo_y = (badge_height - logo_height) / 2
    text_x = 32
    text_y = 18.5

    # SVG 파일을 Base64로 읽기
    with open(logo_file_path, "rb") as logo_file:
        logo_data = logo_file.read()
        encoded_logo = base64.b64encode(logo_data).decode("utf-8")
        logo_data_uri = f"data:image/svg+xml;base64,{encoded_logo}"

    svg_template = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{badge_width}" height="{badge_height}" role="img" aria-label="{label} badge">
  <rect width="{badge_width}" height="{badge_height}" rx="4" fill="{badge_color}"/>
  <image href="{logo_data_uri}" x="{logo_x}" y="{logo_y}" height="{logo_height}"/>
  <text x="{text_x}" y="{text_y}"
        fill="{text_color}"
        font-family="Arial, sans-serif"
        font-size="14"
        font-weight="600">{label}</text>
</svg>
'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_template)
        print(f"✅ SVG badge saved to: {output_path}")


# 예시 실행
if __name__ == "__main__":
    generate_svg_badge_with_embedded_logo(
        output_path="../badge/division_badge.svg",
        label="Division",
        badge_color="#000000",
        text_color="#ffffff",
        logo_file_path="../logo/division.svg"
    )