"""
将 developer-site-waas2 的文件和目录复制到 developer-site 的脚本，并在完成后
清理 developer-site/v2/cobo_waas2_openapi_spec 中除 dev_openapi.yaml 外的所有文件。
支持文件和目录的复制，并处理已存在的目标目录。
"""

import shutil
import os
from pathlib import Path
from typing import List, Tuple

# 使用 Path 对象定义项目根路径
PROJECT_ROOT = Path.cwd().parent.parent

# 定义源和目标基础路径
SOURCE_BASE = PROJECT_ROOT / 'developer-site-waas2'
TARGET_BASE = PROJECT_ROOT / 'developer-site'

# 定义需要复制的文件和目录对
COPY_PAIRS: List[Tuple[Path, Path]] = [
    (SOURCE_BASE / '_snippets', TARGET_BASE / '_snippets'),
    (SOURCE_BASE / 'snippets', TARGET_BASE / 'snippets'),
    (SOURCE_BASE / 'docs.json', TARGET_BASE / 'docs.json'),
    (SOURCE_BASE / 'logo', TARGET_BASE / 'logo'),
    (SOURCE_BASE / 'v1', TARGET_BASE / 'v1'),
    (SOURCE_BASE / 'v2', TARGET_BASE / 'v2'),
    (SOURCE_BASE / 'v2_cn', TARGET_BASE / 'v2_cn'),
    (SOURCE_BASE / 'mint.json', TARGET_BASE / 'mint.json'),
    (SOURCE_BASE / 'README.md', TARGET_BASE / 'README.md'),
    (SOURCE_BASE / 'script.js', TARGET_BASE / 'script.js'),
    (SOURCE_BASE / 'api_playground.js', TARGET_BASE / 'api_playground.js'),
    (SOURCE_BASE / 'styles.css', TARGET_BASE / 'styles.css'),
]

# 定义需要清理的目录和保留的文件
SPEC_DIR = TARGET_BASE / 'v2' / 'cobo_waas2_openapi_spec'
KEEP_FILE = SPEC_DIR / 'dev_openapi.yaml'


def copy_file_or_directory(src: Path, dst: Path) -> None:
    """
    复制单个文件或目录到目标路径。

    Args:
        src: 源路径
        dst: 目标路径
    """
    try:
        if src.is_file():
            # 确保目标目录存在
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(src, dst)
            print(f"已复制文件: {src} -> {dst}")
        elif src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
            print(f"已复制目录: {src} -> {dst}")
        else:
            print(f"警告: 源路径不存在或无效: {src}")
    except FileNotFoundError as e:
        print(f"错误: 文件或目录未找到: {e}")
    except PermissionError as e:
        print(f"错误: 权限不足: {e}")
    except Exception as e:
        print(f"错误: 复制 {src} 到 {dst} 时发生未知错误: {e}")


def clean_spec_directory() -> None:
    """清理 SPEC_DIR 中除 KEEP_FILE 外的所有文件和目录"""
    if not SPEC_DIR.exists():
        print(f"目录不存在，无需清理: {SPEC_DIR}")
        return

    try:
        for item in SPEC_DIR.iterdir():
            if item == KEEP_FILE:
                continue
            if item.is_file():
                item.unlink()
                print(f"已删除文件: {item}")
            elif item.is_dir():
                shutil.rmtree(item)
                print(f"已删除目录: {item}")
    except PermissionError as e:
        print(f"错误: 清理 {SPEC_DIR} 时权限不足: {e}")
    except Exception as e:
        print(f"错误: 清理 {SPEC_DIR} 时发生未知错误: {e}")


def main() -> None:
    """主函数，执行文件和目录复制操作并清理特定目录"""
    # 执行复制操作
    for src, dst in COPY_PAIRS:
        copy_file_or_directory(src, dst)

    # 清理特定目录
    print("\n开始清理 v2/cobo_waas2_openapi_spec 目录...")
    clean_spec_directory()
    print("搬运完成")


if __name__ == "__main__":
    main()
