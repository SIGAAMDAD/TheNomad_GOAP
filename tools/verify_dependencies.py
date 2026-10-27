#!/usr/bin/env python3
import json
import pathlib
import re
root=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((root/"deps/dependencies.lock.json").read_text())
cmake=(root/"cmake/Dependencies.cmake").read_text()
assert data["schema"]==1
for dep in data["dependencies"]:
    assert re.fullmatch("[0-9a-f]{40}",dep["commit"])
    pattern=r"FetchContent_Declare\s*\(\s*"+dep["name"]+r"\b(?P<body>[^)]*)\)"
    match=re.search(pattern,cmake,re.S)
    assert match and "GIT_TAG "+dep["commit"] in match["body"],dep["name"]+" drift"
    assert "GIT_REPOSITORY "+dep["url"] in match["body"]
print("Dependency lock verified: EASTL 3.27.01 and EABase")
