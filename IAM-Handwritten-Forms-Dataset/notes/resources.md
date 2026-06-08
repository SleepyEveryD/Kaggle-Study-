# 资源 (resources)

## ⚠️ 原数据集方向不符（已弃用）
https://www.kaggle.com/datasets/naderabdelghany/iam-handwritten-forms-dataset
经探查：1539 张整页 form 图、**无文字标签**、659 个文件夹按 writer 分。
它其实是给 **Writer Identification**（书写者识别，分类任务）用的，不是 HTR。→ 弃用。

## ✅ HTR 学习主线（已选定）
**复现目标：Keras 官方 Handwriting Recognition 示例（CRNN + CTC）**
https://keras.io/examples/vision/handwriting_recognition/
- 数据：IAM Words（96,456 带标签单词），90/5/5 切分
- 预处理：灰度、128×32、保长宽比 padding、归一化、过滤 err、StringLookup 编码 label
- 模型：Conv2D×2 → Reshape → Dense → BiLSTM×2 → Dense(softmax) → CTCLayer
- 解码：greedy CTC decoding；指标：edit distance / CER
- 完美对应我们学的 concept-01/02/03，是初学复现黄金起点。

**带标签数据集（替换 forms）**：
https://www.kaggle.com/datasets/nibinv23/iam-handwriting-word-database  （word 级 + words.txt）

**其他可参考 notebook（备选）**：
- Kaggle: hamiddamadi/handwritten-text-recognition-iam（TF）
- Kaggle: mathewtkevin/handwritten-text-recognition-pytorch（PyTorch）
- GitHub: Sagar-modelling/Handwriting_Recognition_CRNN_LSTM

## SOTA（学术"第一名"，进阶再看）
TrOCR（微软，Transformer+预训练，IAM CER ≈ 2.9%）。太重，非首个复现目标。

## 论文（建立体系后读）
CRNN、CTC、TrOCR 原始论文。
