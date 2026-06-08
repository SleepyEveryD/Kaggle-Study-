# Solution 拆解 · Keras 官方 HTR (CRNN + CTC)

来源：https://keras.io/examples/vision/handwriting_recognition/
数据：IAM Words（带标签），CRNN + CTC，greedy 解码。逐块拆解，对照 [01](01-htr-overview.md)/[02](02-iam-dataset-structure.md)/[03](03-ctc-loss.md)。

## 块 1 · 数据加载与标签解析 ✅
- **下载**：IAM_Words.zip（Sayak Paul mirror）→ `words/` 图片 + `words.txt` 标签。
- **解析 words.txt**：`if line[0]=='#': continue`（跳注释）；`if line.split(' ')[1] != 'err'`（过滤切割失败样本）。→ 正是 concept-02 的 `#` 注释 + ok/err 过滤。
- **切分**：shuffle 后 90% train / 5% val / 5% test。
- **拼路径** `get_image_paths_and_labels`：从 id `a01-000u-00-00` 拆 `a01`/`000u` → `words/a01/a01-000u/a01-000u-00-00.png`（concept-02 命名钥匙）；`os.path.getsize` 过滤 0 字节坏图。
- 此刻样本存整行，文字 label（最后字段）在块 2 编码时才提取。

## 块 2 · 预处理 + label 向量化  （待拆）
## 块 3 · 模型 CRNN + CTCLayer  （待拆）
## 块 4 · 训练 + edit distance 回调  （待拆）
## 块 5 · 推理 greedy 解码  （待拆）
