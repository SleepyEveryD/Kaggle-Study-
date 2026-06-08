# IAM Handwritten Forms — 学习项目

学习 Kaggle [IAM Handwritten Forms Dataset](https://www.kaggle.com/datasets/naderabdelghany/iam-handwritten-forms-dataset/code) benchmark，从优秀解题者的方案中学习 **HTR (Handwritten Text Recognition)** 的思路与相关知识。

## 学习目标（四位一体）
1. **理解概念与原理** — 搞懂 HTR 方法论及"为什么这么做"
2. **复现优秀方案** — 跟高分 notebook 一步步复现、跑通、理解每一步
3. **自己动手建模** — 最终能从零搭一个可用的 HTR 模型并评估
4. **积累可迁移技能** — 把数据处理、训练技巧、调参沉淀成可复用方法论

## 我是谁
ML/CV/HTR 初学者，有 Python 与深度学习入门基础。讲解用中英混合，先原理后代码。

## 笔记结构（`notes/`）
| 文件 | 内容 |
|------|------|
| [`notes/00-progress.md`](notes/00-progress.md) | ⭐ **「我正在做什么」活页** — 当前阶段 / 进展 / 下一步 / 知识点索引 |
| [`notes/01-htr-overview.md`](notes/01-htr-overview.md) | HTR 全局技术地图 |
| [`notes/02-iam-dataset-structure.md`](notes/02-iam-dataset-structure.md) | IAM 数据集结构 |
| [`notes/resources.md`](notes/resources.md) | Kaggle 链接、关键 notebook、论文 |

> 命名约定：`0x-*` 是按学习顺序的知识点（concept），`solution-*` 放复现的高分方案拆解。每学完一段更新 `00-progress.md`。

## 工作流（本地写 + 云端跑）
本地写 `src/*.py`（git 管理）→ push 到 GitHub → 在 Kaggle/Colab notebook 里 `git clone` 后 import 运行。详见 [`notes/workflow.md`](notes/workflow.md)。

```
src/         本地可复用代码（config.py 自动适配 local/kaggle/colab 路径）
notebooks/   云端跑的 .ipynb（薄壳：拉代码 + 设路径 + 调用 src）
```
