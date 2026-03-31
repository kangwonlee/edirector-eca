# begin tests/test_syntax.py
#
# For director (prompt-only) assignments, test_syntax checks:
#   1. prompt.txt exists and is not empty
#   2. prompt.txt does not contain Python code constructs
#   3. exercise.py was generated and is syntactically valid Python

import ast
import functools
import pathlib
import re
from typing import Tuple

import pytest


# Python code detection patterns
_CODE_PATTERNS = re.compile(
    r'^\s*(def |class |import |from .+ import|if .+:|for .+:|while .+:|print\(|[a-zA-Z_]\w*\s*=\s*)',
    re.MULTILINE,
)


def test__prompt_exists(prompt_path:pathlib.Path):
    assert prompt_path.exists(), (
        f"prompt.txt not found at {prompt_path}\n"
        f"{prompt_path} 에서 prompt.txt 를 찾을 수 없습니다."
    )


def test__prompt_not_empty(prompt_path:pathlib.Path):
    content = prompt_path.read_text(encoding='utf-8').strip()
    # Strip comment lines (lines starting with #)
    lines = [l for l in content.splitlines() if not l.strip().startswith('#')]
    text = '\n'.join(lines).strip()
    assert text, (
        "prompt.txt is empty (only comments). Write a natural language description.\n"
        "prompt.txt 가 비어 있습니다 (주석만 있음). 자연어 설명을 작성하세요."
    )


def test__prompt_no_python_code(prompt_path:pathlib.Path):
    content = prompt_path.read_text(encoding='utf-8')
    matches = _CODE_PATTERNS.findall(content)
    assert not matches, (
        "prompt.txt appears to contain Python code. "
        "Write a natural language description, not code.\n"
        "prompt.txt 에 Python 코드가 포함된 것으로 보입니다. "
        "코드가 아닌 자연어 설명을 작성하세요.\n"
        f"Detected patterns 감지된 패턴: {[m.strip() for m in matches[:5]]}"
    )


def test__exercise_generated(script_path:pathlib.Path):
    assert script_path.exists(), (
        "exercise.py was not generated. Check the prompt pipeline output.\n"
        "exercise.py 가 생성되지 않았습니다. 프롬프트 파이프라인 출력을 확인하세요."
    )


@functools.lru_cache()
def read_code(script_path:pathlib.Path) -> str:
    return script_path.read_text(encoding="utf-8")


@functools.lru_cache()
def parse_code(script_path:pathlib.Path, proj_folder:pathlib.Path) -> ast.AST:
    try:
        tree = ast.parse(read_code(script_path))
    except SyntaxError as e:
        pytest.fail(
            f"Syntax error in generated code: {script_path.relative_to(proj_folder)}\n"
            f"생성된 코드에 문법 오류: {e}"
        )
    return tree


def test__exercise_syntax_valid(script_path:pathlib.Path, proj_folder:pathlib.Path):
    parse_code(script_path, proj_folder)


if __name__ == "__main__":
    pytest.main(['--verbose', __file__])

# end tests/test_syntax.py
