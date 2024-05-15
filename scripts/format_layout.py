from pathlib import Path
import re

content = Path("config/glove80.keymap").read_text()


layout_regex = r"<GLV80_LAYOUT\((.*?)\)>"


def strip(row):
    return [key.strip() for key in row]


def strip_rows(rows):
    return [strip(row.split("&")[1:]) for row in rows]


def col_width(part, col):
    return max([len(row[col] or "") for row in part])


def render_part(layout):
    rows = []
    for row in layout:
        keys = []
        for col, key in enumerate(row):
            key = "&" + key if key else " "
            keys.append(key.ljust(col_width(layout, col) + 1, " "))
        rows.append(" ".join(keys))
    return rows


matches = re.findall(layout_regex, content, flags=re.MULTILINE | re.DOTALL)

result: str = content

for raw_match in matches:
    match = re.sub(r"\/\/ .*", "", raw_match)
    rows = [row.strip() for row in match.split(",") if row.strip()]
    lh = strip_rows(rows[0:6])
    lh[0].append(None)
    lh[5].append(None)

    lht = strip_rows(rows[6:8])

    rh = strip_rows(rows[8:14])
    rh[0] = [None] + rh[0]
    rh[5] = [None] + rh[5]

    rht = strip_rows(rows[14:16])

    s_lh = render_part(lh)
    s_lht = render_part(lht)
    s_rh = render_part(rh)
    s_rht = render_part(rht)

    width = max([len(p[0]) for p in [s_lh, s_lht, s_rh, s_rht]])

    formated = "\n"
    for part in [s_lh, s_lht, s_rh, s_rht]:
        formated += "// ".ljust(width + 3, "-") + " ,\n"
        for row in part:
            formated += f'   {row.ljust(width, " ")} ,\n'

    result = result.replace(raw_match, formated)

Path("config/glove80.keymap").write_text(result)
