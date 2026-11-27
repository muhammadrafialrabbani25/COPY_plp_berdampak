from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_required_folders_exist():
    for name in ("src", "docs", "ai-logs"):
        assert (ROOT / name).is_dir(), f"folder {name}/ harus ada"


def test_tree_sitter_importable():
    import tree_sitter  # noqa: F401
