# 00 · 进度活页（我正在做什么）

> 这是项目的**活页状态**，每次学习推进后更新。背景见 [README](../README.md)。

## 当前阶段
阶段 2（**方向修正**）。**原 forms 数据集弃用**——探查确认：1539 张整页 form 图、**无文字标签**、659 文件夹按 writer 分，实为 **Writer Identification** 用途，不是 HTR。
**新主线**：复现 **Keras 官方 HTR 示例（CRNN+CTC，IAM Words 带标签）**，数据换成 word 级带 `words.txt` 的 Kaggle 镜像。详见 [resources](resources.md)。
**待办**：换数据集 → 复现 Keras CRNN+CTC（正好对应 concept-01/02/03）。
**已知坑**：Colab clone 残留旧文件夹会拉错分支 → Cell 1 已加 `rm -rf`+分支打印；notebook 双向 commit 易冲突，改 notebook 后须在 Colab 重新从 GitHub 打开。
**数据持久化**：已改成 Google Drive 版——zip 缓存到 `MyDrive/iam-handwritten-forms/`，每次会话从 Drive 解压到本地 `/content/data/iam`（只下载一次；IAM 海量小图不直接存 Drive）。

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
- [04-train-val-test](04-train-val-test.md) — train/val/test 三集合（为什么 val 和 test 都要）
- [solution-keras-crnn-ctc](solution-keras-crnn-ctc.md) — 复现 Keras CRNN+CTC（块1数据加载已拆 ✅，块2-5待续）
