# 03 · CTC loss 原理

> 第 3 步学习沉淀。CRNN+CTC 主线最核心一块。解决 [01](01-htr-overview.md) 里的对齐问题。

## 难题回顾
CNN+RNN 每个 time step 输出一个字符概率分布，共 N 列；目标文字 L 个字符，**N > L** 且无对齐标注。CTC 要不靠标注、自动把 N 列预测变成目标串。靠两样东西：**blank 符** + **collapse 规则**。

## 发明 1：blank 符 `-`
字符表额外加一个特殊符 `-`（blank），不代表任何字符，意为"这列没吐出新字符"。每列输出在 `{字符} + {-}` 上的分布。一条 path/alignment 如：`c c - a a a - t t -`。

## 发明 2：collapse 折叠规则 ⭐
两步：① 合并相邻重复字符 → ② 删除所有 blank。
例：`c c - a a a - t t -` → `c - a - t -` → `cat`。

**重复字母靠 blank 隔开**：`hello` 的 `ll` 必须写成 `l - l`，否则 ①会把相邻 ll 合并成单个 l → "helo"。即：**只有被 blank 隔开的相同字符才保留成两个**。这是 CTC 必须有 blank 的根本原因。

## CTC loss 在算什么
同一目标有成千上万条路径都能 collapse 成它。CTC 不挑某条"正确对齐"，而是把**所有能折叠成目标的路径概率求和**作为预测出目标的总概率：
`P(target|图) = Σ_π P(π)`，每条路径概率 = 各列所选字符概率连乘。
**Loss = −log P(target|图)**，训练让总概率变大。
路径不枚举：用 **forward-backward 动态规划**（同 HMM）高效求和；`nn.CTCLoss` 已实现，原理不必死磕。

## 解码 (decoding)：输出概率 → 文字
- **Greedy / best-path**：每列取 argmax 再 collapse。快、简单、近似。初学先用。
- **Beam search**：保留 top-k 候选串（考虑多路径折叠同串），可外挂语言模型。更准、常见提分手段、但慢。

## PyTorch 实战要点
```python
criterion = nn.CTCLoss(blank=0)        # blank 约定为索引 0
log_probs = output.log_softmax(2)      # 形状 (T, N, C)
loss = criterion(log_probs, targets, input_lengths, target_lengths)
```
**易踩坑**：
1. blank 索引要在字符表留位（这里=0）。
2. 必须 `log_softmax` 不是 `softmax`。
3. `input_lengths ≥ target_lengths`（N≥L，否则报错/inf）。
4. 字符表大小 C = 真实字符数 **+1**（blank）。

至此 CRNN+CTC 原理全通：CNN 看图 → BiLSTM 读上下文 → 每列字符分布 → CTC(blank+collapse) 对齐算loss → 解码出文字。
