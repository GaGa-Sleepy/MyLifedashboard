# 人生仪表盘 - 数据更新脚本（健壮版）
# 作用：读取 index.html，按需替换技能、状态、计划，再写回原文件

import re

print("=== 更新人生仪表盘 ===\n")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()


# ============ 1. 技能树 ============
print("【技能树】")
choice = input("是否更新技能树？(y/n)：").strip().lower()

if choice == 'y':
    html_skill = input("  HTML/CSS 熟练度（0-100）：")
    python_skill = input("  Python 熟练度（0-100）：")
    math_skill = input("  高数熟练度（0-100）：")
    english_skill = input("  英语熟练度（0-100）：")

    # 用正则匹配整段标签，不管里面数值是多少都能替换
    content = re.sub(
        r'<span id="html-skill">.*?</span>',
        f'<span id="html-skill">{html_skill}%</span>',
        content
    )
    content = re.sub(
        r'<div class="skill-fill" id="html-skill-bar" style="width: .*?%;"></div>',
        f'<div class="skill-fill" id="html-skill-bar" style="width: {html_skill}%;"></div>',
        content
    )

    content = re.sub(
        r'<span id="python-skill">.*?</span>',
        f'<span id="python-skill">{python_skill}%</span>',
        content
    )
    content = re.sub(
        r'<div class="skill-fill" id="python-skill-bar" style="width: .*?%;"></div>',
        f'<div class="skill-fill" id="python-skill-bar" style="width: {python_skill}%;"></div>',
        content
    )

    content = re.sub(
        r'<span id="math-skill">.*?</span>',
        f'<span id="math-skill">{math_skill}%</span>',
        content
    )
    content = re.sub(
        r'<div class="skill-fill" id="math-skill-bar" style="width: .*?%;"></div>',
        f'<div class="skill-fill" id="math-skill-bar" style="width: {math_skill}%;"></div>',
        content
    )

    content = re.sub(
        r'<span id="english-skill">.*?</span>',
        f'<span id="english-skill">{english_skill}%</span>',
        content
    )
    content = re.sub(
        r'<div class="skill-fill" id="english-skill-bar" style="width: .*?%;"></div>',
        f'<div class="skill-fill" id="english-skill-bar" style="width: {english_skill}%;"></div>',
        content
    )

    print("  ✅ 技能树已更新\n")
else:
    print("  ⏭️  跳过技能树\n")


# ============ 2. 每日状态 ============
print("【今日状态】")
mood = input("今日心情（1-10）：")
energy = input("今日精力（1-10）：")
focus = input("专注时长（小时）：")

content = re.sub(
    r'<span class="status-value" id="mood-value">.*?</span>',
    f'<span class="status-value" id="mood-value">😊 {mood} / 10</span>',
    content
)
content = re.sub(
    r'<span class="status-value" id="energy-value">.*?</span>',
    f'<span class="status-value" id="energy-value">⚡ {energy} / 10</span>',
    content
)
content = re.sub(
    r'<span class="status-value" id="focus-value">.*?</span>',
    f'<span class="status-value" id="focus-value">{focus} 小时</span>',
    content
)

print("  ✅ 状态已更新\n")


# ============ 3. 今日计划 ============
print("【今日计划】")
choice = input("是否更新今日计划？(y/n)：").strip().lower()

if choice == 'y':
    print("  （一行一条，输入空行结束）")
    plans = []
    while True:
        plan = input("  计划：")
        if plan == "":
            break
        plans.append(plan)

    if plans:
        new_li = "\n".join(
            [f'                <li><input type="checkbox" id="plan-{hash(p)}"> {p}</li>'
             for p in plans]
        )
        content = re.sub(
            r'<ul class="plan-list".*?</ul>',
            f'<ul class="plan-list" id="plan-list">\n{new_li}\n            </ul>',
            content,
            flags=re.DOTALL
        )
        print("  ✅ 计划已更新\n")
    else:
        print("  ⏭️  没输入内容，计划保持不变\n")
else:
    print("  ⏭️  跳过计划\n")


# ============ 写回文件 ============
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 全部完成！去浏览器刷新 index.html 看看吧！")