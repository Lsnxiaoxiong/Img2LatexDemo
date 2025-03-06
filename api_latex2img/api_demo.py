import requests
import re
import cairosvg

base_url = "https://math.vercel.app?bgcolor=auto&from="
headers = {
    "Host": "math.vercel.app",
}

latex_str = r"X_{a}^{b}\lim_{x\to\infty}\sqrt[a]{b}\int_{a}^{b}{\textstyle\prod_{c}^{d}} "

print(base_url + latex_str)

response = requests.get(base_url + latex_str)
# 提取svg标签内容
svg_pattern = r'<svg[^>]*>.*?</svg>'
svg_matches = re.findall(svg_pattern, response.text, re.DOTALL)

with open("latex.svg", "w") as f:
    f.write(svg_matches[0])

# 将SVG转换为PNG
cairosvg.svg2png(url="latex.svg", write_to="latex.png")