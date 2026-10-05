"""Add a language to the hand-formatted data files without re-dumping them.

  python tools/lang_fill.py extract ja work/     every string that has no "ja" yet -> work/<file>.json
  python tools/lang_fill.py check ja work/       validate the filled-in work files, write nothing
  python tools/lang_fill.py inject ja work/      put the filled-in "ja" values back, right after the previous language

A work file is a list of units {"i", "en", "ja"}: "en" is a string or a list of strings, "ja" comes out as null and
goes back in the same shape. `i` is the position of the unit among the file's translated strings, so do not edit the
data file between extract and inject (inject checks that the English text still matches). The new key is inserted
textually after the value of the previous language in `site.json -> langs`, so the layout of the files stays as it is.
data/i18n.json works the same way with units {"k", "en", "ja"} and gets its block as one line, like uk and tr.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LANGS = json.loads((DATA / "site.json").read_text(encoding="utf-8"))["langs"]
FILES = sorted(p for p in [*DATA.glob("*.json"), *(DATA / "leveling").glob("*.json")] if p.name != "i18n.json")
# Things a translation must carry over unchanged: tags, {i:item} chips, [[skill]] references.
MARKUP = re.compile(r"<[^>]+>|\{[^{}]*\}|\[\[[^\]]*\]\]")


def units(data, prev):
    """The dicts that hold a `prev` translation, in the order their `prev` key appears in the file."""
    out = []

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == prev and "en" in x:
                    out.append(x)
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(data)
    return out


def spots(text, prev):
    """(end offset, value) of every `"prev": value` in the file text."""
    dec, out = json.JSONDecoder(), []
    for m in re.finditer(rf'"{prev}":\s*', text):
        value, end = dec.raw_decode(text, m.end())
        out.append((end, value))
    return out


def problems(en, new):
    if type(en) is not type(new) or (isinstance(en, list) and len(en) != len(new)) or (isinstance(en, dict) and list(en) != list(new)):
        return ["shape differs from the English value"]
    if isinstance(en, dict):                # i18n.json has a few keyed groups (search_kind, tip_cat)
        en, new = list(en.values()), list(new.values())
    out = []
    for a, b in zip(*([en, new] if isinstance(en, list) else [[en], [new]])):
        if not isinstance(b, str) or (a.strip() and not b.strip()):
            out.append("empty")
        elif sorted(MARKUP.findall(a)) != sorted(MARKUP.findall(b)):
            out.append(f"markup differs: {sorted(set(MARKUP.findall(a)) ^ set(MARKUP.findall(b)))}")
    return out


def extract(lang, work):
    prev = LANGS[LANGS.index(lang) - 1]
    work.mkdir(parents=True, exist_ok=True)
    for f in FILES:
        todo = [{"i": i, "en": u["en"], lang: None}
                for i, u in enumerate(units(json.loads(f.read_text(encoding="utf-8")), prev)) if lang not in u]
        if todo:
            name = f.relative_to(DATA).as_posix().replace("/", "-")
            (work / name).write_text(json.dumps(todo, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"{name}: {len(todo)} units")
    i18n = json.loads((DATA / "i18n.json").read_text(encoding="utf-8"))
    todo = [{"k": k, "en": v, lang: None} for k, v in i18n["en"].items() if k not in i18n.get(lang, {})]
    if todo:
        (work / "i18n.json").write_text(json.dumps(todo, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"i18n.json: {len(todo)} keys")


def inject(lang, work, write=True):
    prev, bad = LANGS[LANGS.index(lang) - 1], 0
    for f in FILES:
        src = work / f.relative_to(DATA).as_posix().replace("/", "-")
        if not src.exists():
            continue
        text = f.read_text(encoding="utf-8")
        us, sp = units(json.loads(text), prev), spots(text, prev)
        if [u[prev] for u in us] != [v for _, v in sp]:
            sys.exit(f"{f.name}: cannot line up the \"{prev}\" keys in the text with the parsed data")
        inserts = []
        for unit in json.loads(src.read_text(encoding="utf-8")):
            u, new = us[unit["i"]], unit[lang]
            errs = (["English text changed since extract"] if u["en"] != unit["en"] else
                    ["already translated"] if lang in u else ["not translated"] if new is None else problems(u["en"], new))
            if errs:
                bad += 1
                print(f"{src.name} #{unit['i']}: {'; '.join(errs)}")
                continue
            inserts.append((sp[unit["i"]][0], f', "{lang}": {json.dumps(new, ensure_ascii=False)}'))
        for pos, piece in sorted(inserts, reverse=True):
            text = text[:pos] + piece + text[pos:]
        json.loads(text)
        if write:
            f.write_text(text, encoding="utf-8")
        print(f"{f.name}: {len(inserts)} {'added' if write else 'ready'}")
    src = work / "i18n.json"
    if src.exists():
        f = DATA / "i18n.json"
        text = f.read_text(encoding="utf-8")
        i18n = json.loads(text)
        block = dict(i18n.get(lang, {}))
        for unit in json.loads(src.read_text(encoding="utf-8")):
            errs = ["not translated"] if unit[lang] is None else problems(i18n["en"][unit["k"]], unit[lang])
            if errs:
                bad += 1
                print(f"i18n.json {unit['k']}: {'; '.join(errs)}")
                continue
            block[unit["k"]] = unit[lang]
        block = {k: block[k] for k in i18n["en"] if k in block}          # key order of the English block
        line = f'  "{lang}": {json.dumps(block, ensure_ascii=False)}'
        if lang in i18n:
            text = re.sub(rf'^  "{lang}": \{{.*\}}(,?)$', lambda m: line + m.group(1), text, flags=re.M)
        else:
            text = re.sub(r"\n\}\s*$", lambda m: ",\n" + line + "\n}\n", text)
        if json.loads(text)[lang] != block:
            sys.exit("i18n.json: the new block did not land as expected")
        if write:
            f.write_text(text, encoding="utf-8")
        print(f"i18n.json: {len(block)} keys in the {lang} block")
    if bad:
        sys.exit(f"{bad} units were skipped — fix them in the work files and run inject again")


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("extract", "check", "inject") or sys.argv[2] not in LANGS[1:]:
        sys.exit(__doc__)
    if sys.argv[1] == "extract":
        extract(sys.argv[2], Path(sys.argv[3]))
    else:
        inject(sys.argv[2], Path(sys.argv[3]), write=sys.argv[1] == "inject")
