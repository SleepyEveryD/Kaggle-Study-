# 00 · 进度活页（我正在做什么）

> 这是项目的**活页状态**，每次学习推进后更新。背景见 [README](../README.md)。

## 当前阶段
阶段 1→2 过渡。**CRNN+CTC 主线原理已全通**（任务/数据/CTC），**工作流已定**（本地写 src + Kaggle 跑，GitHub 同步，见 [workflow](workflow.md)）。下一步：搭好 Kaggle 环境 + fork 一个高分 notebook 跑通。

## 工作流 & 环境（已定）
- 本地写 `src/*.py`（git，**commit/push 由用户手动**）→ push → Colab `git clone` 后 import。
- **跑在 Colab**；数据用 Kaggle API 下载到 `/content/data/iam`。路径由 `src/config.py` 自动适配。
- 仓库：https://github.com/SleepyEveryD/Kaggle-Study-（branch main）。
- 待办：拿 kaggle.json、push 脚手架、Colab 跑通下载、回填真实目录到 config + resources。

## 最近进展（2026-06-08）
- 搭好笔记/记忆体系（项目 `notes/` 为知识库本体）。
- 学完 HTR 全局技术地图 → [01-htr-overview](01-htr-overview.md)。
- 学完 IAM 数据集结构 → [02-iam-dataset-structure](02-iam-dataset-structure.md)。
- 对齐问题(alignment)检查点：用户答对。
- 学完 CTC loss 原理 → [03-ctc-loss](03-ctc-loss.md)（blank/collapse/forward-backward/greedy vs beam/PyTorch坑）。

## 下一步候选
- **[推荐] 读真实高分 notebook**：去 Kaggle 页面挑 1 个 CRNN+CTC 方案通读，对照 7 步 pipeline，确定第一个复现目标。
- 或先下载数据 `ls` 确认本 Kaggle mirror 真实目录结构。
- 进阶原理：CRNN 网络结构细节（CNN backbone + BiLSTM 怎么接）。

## 知识点索引
- [01-htr-overview](01-htr-overview.md) — HTR 全局技术地图（对齐问题/CRNN+CTC/粒度/CER-WER/7步pipeline）
- [02-iam-dataset-structure](02-iam-dataset-structure.md) — IAM 数据结构（四粒度/命名钥匙/words.txt/ok-err过滤）
- [03-ctc-loss](03-ctc-loss.md) — CTC loss（blank/collapse/loss求和/解码/PyTorch要点）
