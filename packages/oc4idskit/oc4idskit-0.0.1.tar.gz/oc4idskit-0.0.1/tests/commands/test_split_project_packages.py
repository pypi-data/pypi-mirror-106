from oc4idskit.cli.__main__ import main
from tests import assert_streaming


def test_command(monkeypatch):
    assert_streaming(
        monkeypatch,
        main,
        ["split-project-packages", "1"],
        ["project_package.json"],
        ["project_package_split.json"],
    )
