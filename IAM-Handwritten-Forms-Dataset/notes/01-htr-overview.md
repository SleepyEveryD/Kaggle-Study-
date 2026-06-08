# 01 · HTR 全局技术地图

> 第 1 步学习沉淀。看后续数据、notebook、复现方案的"认知地基"。

## 任务定义
**HTR (Handwritten Text Recognition)**：输入手写文字图像 → 输出**变长**字符序列。

属于 **sequence recognition** 家族（输出是一串、长度不固定），区别于：
- **图像分类**：图 → 1 个固定类别
- **OCR（印刷体）**：字形规整、间距统一，相对简单
- **HTR（手写）**：字形千人千面、连笔、间距不均 → 难得多

## 核心难题：对齐问题 (alignment problem) ⭐
图像被切成 `N` 个 time steps，目标文字有 `L` 个字符，通常 **N > L**（一字符占多个竖条），且标注只给整行文字、不给每字符位置 → 模型不知道哪些列对应哪个字符。
精确刻画：**N > L、对应关系未标注、且 many-to-one（多对一）**。这三点正是 CTC 要自动搞定的事。

## 三条主流路线
- **A. CRNN + CTC**（经典基线，学习主线）：CNN 提特征 → BiLSTM 读上下文 → CTC loss 自动解决对齐。Kaggle 资料最多、最适合入门。
- **B. Seq2Seq + Attention**：encoder-decoder 逐字符生成 + attention，更灵活但训练更难。
- **C. Transformer（如 TrOCR）**：当前 SOTA，但重、需大算力。

主线：A →（看懂后）了解 B/C。

## 识别粒度（IAM 都提供）
`form`（整页）> `line`（行）> `word`（词）> `character`。常用 line/word；初学从 word 起步。

## 评估指标
- **CER (Character Error Rate)**：字符级错误率，基于 edit distance，**核心指标**
- **WER (Word Error Rate)**：词级错误率
- 都是越低越好。

## 典型 pipeline（7 步）
1. 数据加载 & 解析标注（图片路径 ↔ 文字）
2. 预处理（灰度 grayscale → resize → 归一化 normalize）
3. 数据增强（augmentation：轻微旋转/拉伸/加噪）
4. 模型（CRNN：CNN backbone + BiLSTM）
5. 损失（CTC loss）
6. 解码（decoding：greedy 或 beam search → 文字）
7. 评估（CER / WER）

下一步深入：CTC loss 原理。
