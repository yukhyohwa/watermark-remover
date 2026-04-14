# Frequency Domain Watermark Analyzer & Remover

一个用于检测、分析并物理抹除隐写“盲水印”的桌面安全分析工具。它通过组合物理维度的图形变换策略，从底层破坏基于空域点阵和频域（FFT/DCT）的数字溯源信息。

## 核心功能

* **提取与检测 (`extract` 模式)**：计算图像的傅里叶变换频谱 (FFT Spectrum) 结合拉普拉斯滤波空间域扫描，将隐藏在人眼不可见的高频信号或 LSB 微小噪声可视化。
* **物理抹除 (`remove` 模式)**：对载体执行 **高斯频段截断** -> **微重采样点阵破坏** -> **DCT 特征定型**，实现不可逆的物理级脱敏。

## 环境依赖

* Python 3.7+
* OpenCV
* NumPy

## 快速安装

```bash
git clone <repository_url>
cd watermark-remover
pip install -r requirements.txt
```

## 使用方法

脚本现在支持 `remove` 和 `extract` 两种模式。

### 1. 扫描与探测水印 (`--mode extract`)
当你怀疑一张截图带有企业微信/钉钉/飞书之类的盲水印时，你可以运行提取命令来确诊：
```bash
python watermark_remover.py --mode extract -i input.png -o analysis.jpg
```
*这会输出一张 1:3 拼宽的长图，依次包含：**原始灰度图** | **频域 FFT 频谱热力图** | **空域拉普拉斯锐化图**。如果 FFT 频谱中出现了非自然的星状或交叉对称亮点，说明图片 100% 存在频域水印。*

### 2. 清洗与破坏水印 (`--mode remove`)
使用默认强度清理暗水印（最大限度保留阅读质量）：
```bash
python watermark_remover.py --mode remove -i input.png -o clean.jpg
```

**高级清洗参数：**
如果你追求彻底的安全，牺牲部分画质以绕过更加抗鲁棒的最新型水印算法：
```bash
python watermark_remover.py --mode remove -i input.png -o ultra_clean.jpg -b 5 -q 70 -r 0.98
```

### CLI 完整参数

* `-i`, `--input`: 输入图片路径。
* `-o`, `--output`: 输出图片路径。
* `--mode`: 运行模式。`remove` (抹除) 或 `extract` (探测分析)。默认: `remove`。
* `-b`, `--blur`: [仅remove模式] 高斯模糊内核尺寸。必须为奇数，默认 3。
* `-q`, `--quality`: [仅remove模式] 最终 JPEG 有损压缩率 (1-100)，默认 85。
* `-r`, `--resize`: [仅remove模式] 抗晶格对齐位移比。默认 0.99。

## 架构说明

本项目采用了面向对象的重构模型 (`WatermarkProcessor`)，彻底解耦了文件 I/O 读写和业务逻辑。它同时提供了一个安全的方法来防止 Windows 下中文路径的 OpenCV C++ 引擎报错。

## 注意事项
本项目的研究旨在加强开发者对于信息隐藏技术的学术理解。由于新型水印技术发展迅速（如对抗生成网络隐藏），本工具并不能对安全级别极高的司法级追踪溯源提供绝对匿名保证，机密信息的最高安全操作仍是光学屏摄重建。 
