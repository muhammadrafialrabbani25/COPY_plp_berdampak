from pathlib import Path

WORKFLOW = Path(__file__).resolve().parent.parent / "workflows" / "checkpoint.yml"


def test_checkpoint_workflow_can_checkout_private_repo():
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "contents: read" in text  # tanpa ini actions/checkout gagal di repo privat
    assert "issues: write" in text
