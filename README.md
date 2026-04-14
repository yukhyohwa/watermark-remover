# Frequency Domain Watermark Analyzer & Remover

一个用于检测、分析并物理抹除隐写“盲水印”的桌面端开源安全分析工具。它通过组合物理维度的图形变换策略，从底层破坏基于空域点阵和频域（FFT/DCT）的数字溯源信息。

## 目录结构说明

```text
watermark-remover/
├── core/
│   ├── __init__.py
│   └── processor.py      # 核心水印处理类 (WatermarkProcessor)
├── input/                # 推荐放置待处理原图的地方 (.gitignore 已排除)
├── output/               # 推荐放置输出图片的地方 (.gitignore 已排除)
├── main.py               # CLI 命令行入口执行点
├── requirements.txt
└── README.md
```

## 核心功能

* **提取与检测 (`extract` 模式)**：计算图像的傅里叶变换频谱 (FFT Spectrum) 结合拉普拉斯滤波空间域扫描，将隐藏在人眼不可见的高频信号或 LSB 微小噪声可视化。
* **物理抹除 (`remove` 模式)**：对载体执行 **高斯频段截断** -> **微重采样点阵破坏** -> **DCT 特征定型**，实现不可逆的物理级脱敏。

## 环境依赖

* Python 3.7+
* OpenCV
* NumPy

## 快速安装

```bash
git clone https://github.com/yukhyohwa/watermark-remover.git
cd watermark-remover
pip install -r requirements.txt
```

## 使用方法

脚本的入口已变更为项目根目录下的 `main.py`。

### 1. 扫描与探测水印 (`--mode extract`)
当你怀疑一张截图带有平台暗水印时，运行提取命令：
```bash
python main.py --mode extract -i "input/screenshot.png" -o "output/analysis.jpg"
```
*输出的 `analysis.jpg` 是一张 1:3 的对比长图（原始灰度图 | 频域 FFT 频谱热力图 | 空域拉普拉斯锐化图）。如果 FFT 频谱中出现了非自然的对称高亮亮斑，说明图片 100% 存在频域水印。*

### 2. 清洗与脱敏 (`--mode remove`)
使用默认强度清理暗水印（最大限度兼顾原始阅读画质）：
```bash
python main.py --mode remove -i "input/screenshot.png" -o "output/clean.jpg"
```

**高级清洗参数：**
如果你追求彻底的安全性，可以通过调大参数以过滤极具鲁棒性的新型水印：
```bash
python main.py --mode remove -i "input/screenshot.png" -o "output/ultra_clean.jpg" -b 5 -q 70 -r 0.98
```

### CLI 参数全查阅

* `-i`, `--input`: 输入图片路径。
* `-o`, `--output`: 输出图片路径。
* `--mode`: 运行模式。`remove` (抹除) 或 `extract` (探测分析)。默认: `remove`。
* `-b`, `--blur`: [仅remove模式] 高斯模糊内核尺寸。必须为奇数，默认 3。
* `-q`, `--quality`: [仅remove模式] 最终 JPEG 有损压缩率 (1-100)，默认 85。
* `-r`, `--resize`: [仅remove模式] 抗晶格对齐位移比。默认 0.99。

## 注意事项
本项目的研究旨在加强开发者对于信息隐藏技术的学术理解。由于新型水印技术发展迅速（如对抗生成网络级隐藏），本工具并不能对安全级别极高的司法级追踪溯源提供绝对匿名保证，机密信息的最高安全操作仍是光学屏摄重建。
