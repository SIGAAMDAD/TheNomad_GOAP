# FEAR SDK 1.08 reference artifact

The G00 reference is pinned in this repository as the optional Git submodule **third_party/fear_sdk**, pointing to `xfw5/Fear-SDK-1.08` at commit `2fc3557b0037d5fe01ac607b907d4b8511b9e4b2`. The owner-provided **Fear-SDK-1.08-master.zip** remains an independently hashed local input.

- SHA256: 82a5b7f2f2553e435789be8c9a71e016f7015e95a5e2f4cb256d1ab84aa8aff6
- Input size: 27,575,224 bytes
- Full archive: 2,176 entries, with F.E.A.R. / LithTech client and server sources.
- Related reference: FEAR_SDK_1.08_Clang_AST_2026-10-25.zip, SHA256 8b0a9c62440188fd8114d75d77e0b29ad2d9759c09bcd6914607630772d63206.
- Original public SDK name for version 1.08: fear_publictools_108.exe.
- Repo CI builds never compile or link FEAR/LithTech code.

## Staging a complete SDK reference locally

To obtain the pinned public reference source, run:

    git submodule update --init third_party/fear_sdk

The normal build does not require or compile this submodule.

To stage the owner-provided, independently hashed ZIP, run:

    python tools/stage_fear_sdk.py --archive /path/to/Fear-SDK-1.08-master.zip

The tool checks the exact SHA256 from deps/dependencies.lock.json, copies the
archive into **.cache/fear-sdk-archive/**, and creates a local reference-manifest.json.
The staged files are gitignored and cannot become part of normal source PRs.
Extract the checked archive separately for reference; never execute installers
in CI. A different archive must be reviewed and its lock updated.

The repository stores a **gitlink pointer** to the existing third-party SDK mirror,
not vendored FEAR source bytes. Checking out submodules obtains the exact
pinned original reference from that remote. The independently hashed owner
ZIP remains a separate local input. GitHub Actions publish only GOAP
build-chain artifacts, not FEAR SDK contents.

## Reference symbol map

The principal original GOAP files live under Game/ObjectDLL/:

| Reference | Use in the new standalone port |
|---|---|
| AIPlanner.cpp/.h | Planner public behavior and orchestration |
| AIAStarPlanner.cpp/.h | Backward-regression search |
| AIWorldState.cpp/.h | Fact and world-state comparison |
| AIActionAbstract.cpp/.h and AIAction*.cpp/.h | Conditions, parameter binding, action costs |
| AIGoalMgr.cpp/.h and AIGoal*.cpp/.h | Goal selection and satisfaction |

The original code depends on LithTech runtime services. G00 generates
behavioral reference tests; G02+ implements original standalone C++17
behavior under the approved NMDGOAP interfaces. Avoid copying the engine
runtime, renderer, gameplay actors or SDK files into the shipped DLL.
