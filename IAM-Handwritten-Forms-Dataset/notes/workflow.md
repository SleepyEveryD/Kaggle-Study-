# 工作流：本地写代码 + 云端跑

## 决定
- **写代码**：本地（VS Code），放 `src/*.py`，用 git 管理。
- **跑**：云端 GPU。第一阶段用 **Kaggle**（数据原生、零下载、高分 notebook 就在那），之后自己建模可选 Colab。
- **同步桥**：GitHub。本地 push → 云端 notebook `git clone`/`pull` → import 运行。

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
- **Kaggle**：notebook 里点 "Add Data" 搜 iam-handwritten-forms → 自动挂载到 `/kaggle/input/<dataset-slug>/`。
- **Colab**：用 kaggle API + `kaggle.json` token 下载到 `/content/data/`（每次会话重来）。
- **本地**：一般不放全量数据；如需小样本调试再放 `data/`（已被 .gitignore 忽略）。
- 路径由 `src/config.py` 的 `DATA_DIR` 自动选择。⚠️ Kaggle 的确切挂载路径要在 Add Data 后看一眼再确认填回 config。

## 在 Kaggle notebook 里用本地代码（典型开头 cell）
```python
# 1. 打开 notebook 的 Internet 开关（Settings → Internet on）
!git clone https://github.com/SleepyEveryD/Kaggle-Study-.git
import sys; sys.path.append('/kaggle/working/Kaggle-Study-/IAM-Handwritten-Forms-Dataset')
from src import config, ...    # 调用本地写好的函数
# 改了本地代码后：!cd Kaggle-Study- && git pull
```

## 首次行动 checklist
1. [ ] 注册/登录 Kaggle 账号，手机验证（解锁 GPU + Internet）。
2. [ ] 确认本地仓库已连到 GitHub 远程（`git remote -v`），能 push。
3. [ ] 打开数据集页面，挑 1 个 CRNN+CTC 高分 notebook，"Copy & Edit" fork 来跑通一次（先整体感受）。
4. [ ] 记下挂载路径与 notebook 链接，回填 `notes/resources.md` 和 `src/config.py`。
