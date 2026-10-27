# GOAP G00/G01 — reproducible dependency build

This branch bootstraps a **dependency/build smoke**, not a GOAP planner.
Source main was initially only a README and license.

## Locked dependencies

- EASTL 3.27.01: e323f67e5d93fdadcd44f7998069d804697b1945
- EABase: 0699a15efdfd20b6cecf02153bfa5663decb653c

Both use fixed Git SHA pins through CMake FetchContent and 3-Clause BSD
license; all upstream tests/benchmarks are disabled. CMake can use local
source directories without the network if both are checked out or extracted.

## Commands

Linux GCC:

    cmake --preset linux-gcc
    cmake --build --preset linux-gcc --parallel 2
    ctest --preset linux-gcc

Linux Clang:

    cmake --preset linux-clang
    cmake --build --preset linux-clang --parallel 2
    ctest --preset linux-clang

Windows MSVC (run inside x64 Native Tools Command Prompt):

    cmake --preset windows-msvc
    cmake --build --preset windows-msvc --parallel 2
    ctest --preset windows-msvc

The Windows preset selects C++17 and static MSVC CRT (/MT). The Linux
presets use GCC or Clang. CI runs Linux GCC and Windows MSVC on PRs
and main; successful runs publish a binary, dependency lock and SHA256
build manifest as GitHub Actions artifacts.

Offline development (example):

    cmake --preset linux-gcc -DFETCHCONTENT_SOURCE_DIR_EASTL=/path/EASTL-3.27.01 -DFETCHCONTENT_SOURCE_DIR_EABASE=/path/EABase

## Real GOAP build readiness

The owner-approved migration plan defines G00 reference fixtures, G01
static-core and DLL build target, G02 versioned C ABI, G03-G11 native
planner, and D00-D08 cooker/managed bridge. G01 smoke is a build-chain
proof, not proof of the future planner. Static core/DLL interfaces are
deliberately not invented in a build preparatory patch; they must use
the owner-frozen G02 export contract.

**Acceptance before implementation:** CI passes on both supported
platforms, exact dependency SHAs are evidenced, source authority is
frozen, SDK reference is staged for engineers with access, and the
approved GOAP source work order is admitted by the Studio.

## Pinned FEAR reference access

The SDK is available as an **optional Git submodule** pinned to
`xfw5/Fear-SDK-1.08@2fc3557b0037d5fe01ac607b907d4b8511b9e4b2`.
Use `git submodule update --init third_party/fear_sdk` on a worker machine
when G00 source comparison is assigned. CI deliberately does not recurse
into the submodule, because the clean standalone GOAP build must remain
independent of LithTech and third-party game SDKs.
