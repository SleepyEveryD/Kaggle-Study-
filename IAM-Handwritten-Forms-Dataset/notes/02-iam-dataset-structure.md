# 02 · IAM 数据集结构

> 第 2 步学习沉淀。理解它才能看懂 notebook 的"数据加载"部分。

## 四个粒度 = 四个图片文件夹
```
forms/      整张表单扫描图        a01-000u.png
lines/      一行文字的图          a01-000u-00.png
words/      单个词的图            a01-000u-00-00.png
sentences/  一句话的图
```
训练几乎都用 `lines/` 或 `words/`；初学从 word 起步。
> 本 Kaggle mirror 名为 "forms dataset"，主打整页图；**实际目录待下载后 `ls` 确认**（mirror 可能重组目录）。

## 命名约定 = 图片↔标注的"钥匙" ⭐
文件名本身编码层级：
```
a01 - 000u - 00 - 00 . png
 │     │      │    └── 这行里的第几个 word
 │     │      └─────── 这张表单里的第几 line
 └─────┴────────────── form id (a01-000u)
```
靠这个 id 把词图 ↔ 文字标注对应起来，是数据加载的关键。

## 标注文件格式（最重要）
最常用 `words.txt` / `lines.txt`。`words.txt` 每行：
```
a01-000u-00-00 ok 154 408 768 27 51 AT A
```
| 字段 | 例 | 含义 |
|------|----|------|
| word id | `a01-000u-00-00` | 对应图片文件名（钥匙） |
| **segmentation 结果** | `ok` | ⚠️ `ok`=切得好，`err`=可能切歪 |
| graylevel | `154` | 二值化阈值 |
| bbox | `408 768 27 51` | x, y, w, h |
| 词性 tag | `AT` | POS tag（一般用不上） |
| **transcription** | `A` | ⭐ 真正的文字标注 (label) |

`lines.txt` 类似，整行文字用 `|` 分隔词。

## 实战必踩坑：ok vs err ⚠️
`err` 样本切割可能有误。**几乎所有高分方案先过滤掉 err 只留 ok**，否则脏标签拖垮模型。这是"读懂数据才知道"的关键 trick。

## 数据加载逻辑（6 步）
1. 逐行读 words.txt
2. 跳过 `#` 开头注释行
3. 按空格 split；过滤 `segmentation == 'err'`
4. 用 word id 拼图片路径
5. 取最后字段作 label（文字）
6. 得到 (图片路径, 文字) 配对 → 喂给 Dataset
