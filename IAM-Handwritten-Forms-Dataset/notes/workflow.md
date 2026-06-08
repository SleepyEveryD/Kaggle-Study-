# 工作流：本地写代码 + 云端跑

## 决定
- **写代码**：本地（VS Code），放 `src/*.py`，用 git 管理。**commit/push 永远由用户手动做。**
- **跑**：**Colab**（免费 GPU）。数据用 Kaggle API 下载到 Colab。学习/参考的高分 notebook 仍来自 Kaggle 数据集页面（读思路）。
- **同步桥**：GitHub。本地 push → Colab `git clone`/`pull` → import 运行。

## 仓库结构
```
IAM-Handwritten-Forms-Dataset/
├── README.md
├── notes/              学习笔记（知识库本体）
├── src/                本地写的可复用代码 (.py 模块)
│   └── config.py       环境/路径自动适配（local / kaggle / colab）
├── notebooks/          在 colab/kaggle 跑的 .ipynb（薄壳：拉代码+设路径+调用 src）
├── requirements.txt
└── .gitignore          忽略 data/、checkpoints、大文件
```

## 数据放哪（不下载到本地！）
Colab 用 **Kaggle API** 把数据集拉进 `/content/data/`（每次新会话要重跑；想免重下可挂 Google Drive 缓存）。
- 拿 token：Kaggle → Account → "Create New API Token" 下载 `kaggle.json`。
- 路径由 `src/config.py` 的 `DATA_DIR` 自动选择（colab → `/content/data/iam`）。
- ⚠️ 解压后看一眼真实子目录结构，回填 config / resources。

## Colab notebook 典型开头 cells
```python
# Cell 1: 拉本地代码
!git clone https://github.com/SleepyEveryD/Kaggle-Study-.git
import sys; sys.path.append('/content/Kaggle-Study-/IAM-Handwritten-Forms-Dataset')
# 改了本地代码后：!cd /content/Kaggle-Study- && git pull

# Cell 2: 配 Kaggle API（把 kaggle.json 传上来，或用 Colab Secrets）
from google.colab import files; files.upload()          # 选 kaggle.json
!mkdir -p ~/.kaggle && cp kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json
!pip -q install kaggle

# Cell 3: 下载并解压数据
!kaggle datasets download -d naderabdelghany/iam-handwritten-forms-dataset -p /content/data/iam --unzip

# Cell 4: 用本地写好的代码
from src import config            # config.ENV == 'colab', config.DATA_DIR 已就绪
print(config.ENV, config.DATA_DIR)
```
> GPU：Colab 菜单 Runtime → Change runtime type → T4 GPU。

## 首次行动 checklist
1. [ ] Kaggle Account → Create New API Token，拿到 `kaggle.json`。
2. [ ] 本地把脚手架 commit + push 到 GitHub（用户手动）。
3. [ ] 新建 Colab notebook，跑上面 4 个 cell，确认数据下载成功、能 import src。
4. [ ] 解压后 `ls` 看真实目录，回填 `src/config.py` 与 `notes/resources.md`。
5. [ ] 去 Kaggle 数据集页面挑 1 个 CRNN+CTC 高分 notebook 读思路（参考，不一定在那跑）。
