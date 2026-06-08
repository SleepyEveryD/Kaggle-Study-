"""环境与路径配置：本地写、Kaggle/Colab 跑，数据路径自动适配。

用法：
    from src import config
    print(config.ENV, config.DATA_DIR)
"""
import os
from pathlib import Path


def detect_env() -> str:
    """检测当前运行环境：'kaggle' / 'colab' / 'local'。"""
    if "KAGGLE_KERNEL_RUN_TYPE" in os.environ:
        return "kaggle"
    try:
        import google.colab  # noqa: F401
        return "colab"
    except ImportError:
        return "local"


ENV = detect_env()

# 项目根（本地仓库内 .../IAM-Handwritten-Forms-Dataset）
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 数据根目录：各环境不同。
# ⚠️ Kaggle 的确切 slug 要在 notebook "Add Data" 后核对再改这里。
DATA_DIR = {
    "kaggle": Path("/kaggle/input/iam-handwritten-forms-dataset"),
    "colab": Path("/content/data/iam"),
    "local": PROJECT_ROOT / "data",
}[ENV]
