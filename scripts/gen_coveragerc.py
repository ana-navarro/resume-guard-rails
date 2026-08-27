"""Regenerates .coveragerc, adding any @wip-annotated source file to the omit list.

Constitution Principle III: files marked with the @wip annotation/comment MUST be
fully excluded from the coverage metric. Coverage.py's [run] omit only accepts path
patterns, so this script scans the tree for the @wip marker and writes the resulting
omit list before each pipeline run.
"""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATIC_OMIT = ["*/tests/*", "*/.venv/*", "conftest.py", "scripts/*"]


def find_wip_files() -> list[str]:
    wip = []
    for path in ROOT.rglob("*.py"):
        if ".venv" in path.parts or "tests" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "@wip" in text:
            wip.append(str(path.relative_to(ROOT)).replace("\\", "/"))
    return wip


def main() -> None:
    omit = STATIC_OMIT + find_wip_files()
    lines = ["[run]", "source = .", "omit ="]
    lines += [f"    {pattern}" for pattern in omit]
    lines += ["", "[report]", "fail_under = 80", "show_missing = True"]
    (ROOT / ".coveragerc").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
