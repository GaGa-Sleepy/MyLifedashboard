# 人生仪表盘 - 个人成长曲线
# 运行环境：Python 3.x
# 需要安装：pip install matplotlib

import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体，防止中文显示为方框
# 如果你的电脑没有 SimHei，可以改成 'Microsoft YaHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# ========== 数据区：你可以修改这里的数据 ==========

# 一周的日期
days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

# 心情评分（1-10分）
mood = [6, 7, 8, 7, 9, 8, 9]

# Python 技能熟练度（百分比）
python_skill = [20, 25, 30, 35, 40, 42, 45]

# 学习时长（小时）
study_hours = [1.5, 2.0, 2.5, 1.0, 3.0, 2.5, 3.5]

# ========== 绘图区 ==========

# 创建画布，设置大小和深色背景
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#161b22')

# 画三条折线
ax.plot(days, mood, marker='o', label='心情指数', color='#58a6ff', linewidth=2)
ax.plot(days, python_skill, marker='s', label='Python 熟练度', color='#3fb950', linewidth=2)

# 设置标题和标签
ax.set_title('个人成长曲线 · 一周记录', fontsize=16, color='#e6edf3', pad=16)
ax.set_xlabel('日期', fontsize=12, color='#c9d1d9')
ax.set_ylabel('数值', fontsize=12, color='#c9d1d9')

# 设置坐标轴颜色
ax.tick_params(colors='#8b949e')
for spine in ax.spines.values():
    spine.set_color('#30363d')

# 添加图例
legend = ax.legend(facecolor='#21262d', edgecolor='#30363d', fontsize=10)
for text in legend.get_texts():
    text.set_color('#e6edf3')

# 添加网格线
ax.grid(True, linestyle='--', alpha=0.2, color='#30363d')

# 保存图片（高清）
plt.tight_layout()
plt.savefig('growth_curve.png', dpi=150, facecolor=fig.get_facecolor())
print('✅ 图表已保存为 growth_curve.png')

# 显示图表
plt.show()