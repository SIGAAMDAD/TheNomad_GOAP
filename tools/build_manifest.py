#!/usr/bin/env python3
"""Record reproducibility evidence from a real configured build."""
import argparse
import hashlib
import json
import os
import pathlib
import platform
import subprocess

p=argparse.ArgumentParser()
p.add_argument("--preset",required=True)
args=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]
build=root/"build"/args.preset
exes=[]
for f in sorted((build/"bin").glob("*")):
    if f.is_file():
        h=hashlib.sha256()
        with f.open("rb") as fd:
            for chunk in iter(lambda:fd.read(1024*1024),b""):
                h.update(chunk)
        exes.append({"filename":f.name,"sha256":h.hexdigest(),"bytes":f.stat().st_size})
sha=os.getenv("GITHUB_SHA")
if not sha:
    sha=subprocess.run(["git","-C",str(root),"rev-parse","HEAD"],capture_output=True,text=True).stdout.strip() or None
output={"schema":1,"source_sha":sha,"preset":args.preset,"host":platform.platform(),
        "dependencies":json.loads((root/"deps/dependencies.lock.json").read_text())["dependencies"],
        "artifacts":exes}
build.mkdir(parents=True,exist_ok=True)
(build/"build-manifest.json").write_text(json.dumps(output,indent=2)+"\n")
print("Recorded",len(exes),"artifacts from",args.preset)
