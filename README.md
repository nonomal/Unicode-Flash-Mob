# Unicode Flash PPT Generator

## 项目描述

Unicode Flash PPT Generator （Unicode快闪PPT生成器）是一个Python脚本，用于自动生成包含Unicode字符的PowerPoint演示文稿。这个工具可以创建大量包含各种Unicode字符、描述和自定义背景的幻灯片，适用于教育、展示或Unicode字符集探索等用途。

## 使用教程

1. 确保您已经从项目左边的 `releases` 页面下载最新版本，和下载 `ffmpeg` 并添加到环境变量；

2. 新建一个文件夹并运行 `UFMPPTG.exe` 把此程序安装在此目录，或者下载 `UFMPPTG.zip` 压缩包并全部解压到一个文件夹下；

3. 运行 `main.exe` 并安装 `RHR SC` 字体(中途会弹出来) 和 所有您生成PPTx文件需要使用的字体；

4. 等待脚本运行结束，生成的PPT文件将保存在 `res` 目录下以字体名称命名的文件夹中；

5. 生成的 pptx 文件推荐用 Microsoft PowerPoint 2016 以上的版本打开，您可以随意更改文本内容和颜色；

6. 如果要生成视频文件(.mp4)需按照以下步骤：

<details>
<summary>生成视频教程</summary>

1. 打开 pptx 文件，点击 "文件" > "导出" > "创建动态GIF"；
2. 质量选择 "特大" (1080p 24fps)；
3. 点击"创建GIF"按钮，选择保存位置 > 为GIF文件命名 > 点击"保存"；
4. 等待gif文件生成完毕，把 `res` 目录下的 `MP4.bat` 文件放在生成的git目录下；
5. 把 `res` 目录下的 `DUTM.ogg` 文件放在生成的git目录下，并运行。
</details>

<details>
<summary>生成速度公式</summary>

测试标准为我的电脑<br>
小于1500时：<br>
![equation](https://latex.codecogs.com/gif.latex?\dpi{200}&space;y=-7.24\ln(x)+200)<br>
大于1500时：<br>
![equation](https://latex.codecogs.com/gif.latex?\dpi{200}&space;y=7079.45x^{\left(-0.8751\right)}12.5)<br>
</details>

## 功能特点

- 自动从文本文件读取Unicode字符信息
- 为每个Unicode字符创建独立的幻灯片
- 支持自定义字体和背景颜色
- 自动分割大型演示文稿为多个文件
- 显示处理进度条

## 扩展配置

- 在 `ppt.py` 脚本中，您可以调整以下参数：
  - `font_color`：中间字符的颜色
  - `BottomFont`：左下角描述文本的字体
  - `threshold`：每个PPT文件包含的最大幻灯片数量（实验性功能）
  - `font_size`：中间Unicode字符的字体大小
  - `x_offset`：中间字符的x轴偏移量
  - `y_offset`：中间字符的y轴偏移量

## 软件授权

本项目采用 Apache License 2.0 授权协议。

完整的许可证文本可在 [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) 查看。

### 您可以:

 - 自由使用、复制、修改、分发本项目,包括商用,无需付费、告知或标明原作者。
 - 自由将项目文件安装在任何软件或设备中。
 - 在此基础上进行二次创作,修改后的作品也可以以 Apache License 2.0 发表。
 
### 但有以下要求:
 
 1. 您必须在任何副本或重大修改的文件中包含原始版权声明和本许可声明。
 2. 如果您修改了代码,必须在修改的文件中加注明显的"由此文件衍生"声明。
 3. 在任何发布的二次创作作品中,不得使用「Unicode-Flash-Mob」名称和「Unicode-Flash-PPT-Generator」名称或版权持有人的名称来认可或推广衍生作品,除非获得事先书面许可。

总之,只要遵守 Apache License 2.0 的要求,任何个人或组织都可以自由使用、修改和分发本项目。严禁任何倒卖或非法商业行为。如有违反,请立即举报,我们将保留追究法律责任的权利。

## 注意事项

- 生成大量幻灯片可能需要较长时间，请耐心等待。
- 确保您有足够的磁盘空间来存储生成的PPT文件，至少2GiB。
- 如果遇到内存不足的问题，请尝试降低 `threshold` 值。

## 贡献

欢迎提交问题报告、功能请求或代码贡献。请遵循以下步骤：

1. Fork 本仓库
2. 创建您的特性分支 ( `git checkout -b feature/AmazingFeature`)
3. 提交您的更改 ( `git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 ( `git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 联系方式

如有任何问题或建议，请通过以下方式联系我们：

- 项目Issues页面
- QQ 邮箱: 762270064@qq.com
- Gmail: chenlelei644@gmail.com(长期不在线)

最后感谢您使用 Unicode Flash PPT Generator！
