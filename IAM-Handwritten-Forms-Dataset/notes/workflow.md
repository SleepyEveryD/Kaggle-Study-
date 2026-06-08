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
- 认证：Kaggle settings 页只能**复制 API key**（一长串字符）→ 不用 kaggle.json，直接在 Colab 设环境变量 `KAGGLE_USERNAME` / `KAGGLE_KEY`。
- ⚠️ key 是机密：别提交 git、别公开分享含 key 的 notebook。推荐用 **Colab Secrets**（左侧 🔑）存，避免明文写在 cell 里。
- 路径由 `src/config.py` 的 `DATA_DIR` 自动选择（colab → `/content/data/iam`）。
- ⚠️ 解压后看一眼真实子目录结构，回填 config / resources。

## Colab notebook 典型开头 cells
```python
# Cell 1: 拉本地代码（-b 跟你的开发分支，当前 process-data；合并到 main 后改 main）
!rm -rf Kaggle-Study-                              # 删旧 clone，保证拿最新（Colab 会残留上次的）
!git clone -b process-data https://github.com/SleepyEveryD/Kaggle-Study-.git
import sys; sys.path.append('/content/Kaggle-Study-/IAM-Handwritten-Forms-Dataset')
!cd Kaggle-Study- && git branch --show-current && git log --oneline -1   # 核对分支+commit
# 改了 src 后重跑：最稳妥 Runtime → Restart session（避免 Python 模块缓存旧版）

# Cell 2: 配 Kaggle 认证（推荐 Colab Secrets 版）
import os
from google.colab import userdata          # 左侧 🔑 Secrets 里先建 KAGGLE_USERNAME / KAGGLE_KEY
os.environ['KAGGLE_USERNAME'] = userdata.get('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY']      = userdata.get('KAGGLE_KEY')
!pip -q install kaggle
# —— 或最简版（明文，仅自己用、别分享）：
# os.environ['KAGGLE_USERNAME'] = '你的用户名'
# os.environ['KAGGLE_KEY']      = '你复制的key'

# Cell 3: 下载并解压数据（已存在则跳过，避免重下 4.3GB）
import os, subprocess
DATA_DIR = '/content/data/iam'
if os.path.isdir(f'{DATA_DIR}/data') and os.listdir(f'{DATA_DIR}/data'):
    print('✅ 已存在，跳过下载')
else:
    subprocess.run(f'kaggle datasets download -d naderabdelghany/iam-handwritten-forms-dataset -p {DATA_DIR} --unzip', shell=True, check=True)
!ls {DATA_DIR}
# 注：删除/新建 runtime 会清空 /content，下次仍需重下；跨会话持久化需挂 Google Drive。

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
