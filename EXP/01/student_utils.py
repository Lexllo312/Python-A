# -*- coding: utf-8 -*-
"""实验01 用到的学生记录解析工具。由 Notebook 4-7 生成。"""


def parse_student(line):
    """把 'name,score' 一行解析为 {'name': str, 'score': int}。

    字段数不为 2、姓名为空、成绩非整数或超出 0~100 时抛 ValueError。
    """
    parts = [p.strip() for p in line.strip().split(",")]

    if len(parts) != 2:
        raise ValueError(f"字段数量应为 2，实际为 {len(parts)}：{line.strip()!r}")

    name, raw_score = parts
    if not name:
        raise ValueError(f"姓名为空：{line.strip()!r}")

    try:
        score = int(raw_score)
    except ValueError:
        raise ValueError(f"成绩不是合法整数：{raw_score!r}") from None

    if score < 0 or score > 100:
        raise ValueError(f"成绩超出 0~100 范围：{score}")

    return {"name": name, "score": score}
