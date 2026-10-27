#!/usr/bin/env python3
"""Stage an owner-supplied FEAR SDK 1.08 reference; never executes installers.

The payload is intentionally excluded from Git. This tool only verifies bytes
and stages a reference in third_party/fear_sdk for local engineering analysis.
"""
import argparse
import hashlib
import json
import pathlib
import shutil

ROOT=pathlib.Path(__file__).resolve().parents[1]
LOCK=json.loads((ROOT/"deps/dependencies.lock.json").read_text(encoding="utf-8"))
EXPECTED=LOCK["reference"]["sha256"]

def file_hash(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for data in iter(lambda:f.read(1024*1024),b""):
            h.update(data)
    return h.hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--archive",type=pathlib.Path,required=True)
    p.add_argument("--allow-unpinned",action="store_true",
                   help="Use only for a different SDK archive after updating reviewed lock")
    args=p.parse_args()
    source=args.archive.resolve(strict=True)
    if not source.is_file():
        p.error("An SDK archive file is required; run installer/extraction separately")
    digest=file_hash(source)
    if digest!=EXPECTED and not args.allow_unpinned:
        p.error("FEAR SDK SHA256 mismatch; verify source and reviewed manifest")
    target=ROOT/"third_party"/"fear_sdk"
    target.mkdir(parents=True,exist_ok=True)
    dest=target/source.name
    if source!=dest.resolve():
        shutil.copyfile(source,dest)
    report={"sdk_version":"1.08","source_archive":source.name,"sha256":digest,
            "matches_reviewed_input":digest==EXPECTED,"size":source.stat().st_size,
            "extracted":False,"source_files_committed":False}
    (target/"reference-manifest.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":
    main()
