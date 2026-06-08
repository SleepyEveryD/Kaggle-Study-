# 04 · train / validation / test 三集合（可迁移 ML 基础）

数据切三份，互不重叠、各司其职：

| 集合 | 用途 | 模型学它吗 |
|------|------|-----------|
| **train** | 训练，调权重（梯度下降） | ✅ 反复学 |
| **validation** | 训练**过程中**检验/调参/早停判断 | ❌ 只"看"不学 |
| **test** | 训练**全部结束后只用一次**，报告诚实的最终成绩 | ❌ 全程不碰 |

## 为什么 val 和 test 都要
考试类比：train=练习题、validation=模拟考（据其调整复习策略）、test=高考（只考一次）。
关键：**一旦你根据 validation 成绩做决策（调超参/选 epoch），validation 就"不干净"了**，拿它当最终分会**高估**模型。所以必须再留一个全程不参与任何决策的 test，给出无偏的真实水平。
一句话：**validation 边训边决策，test 最后诚实打分。**

## Keras HTR 里的 90/5/5
```python
split_idx = int(0.9*len(words_list)); train = words_list[:split_idx]   # 90%
rest = words_list[split_idx:]                                          # 10%
val = rest[:int(0.5*len(rest))]   # 5%
test = rest[int(0.5*len(rest)):]  # 5%
```
坑：原代码变量 `test_samples` 被复用两次（先=10%，对半切后又=最后5%），别看晕。

承接 [solution-keras-crnn-ctc](solution-keras-crnn-ctc.md) 块1。
