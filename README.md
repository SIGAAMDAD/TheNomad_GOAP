# TheNomad_GOAP

Standalone C++17 Goal-Oriented Action Planning library, guided by
F.E.A.R. SDK 1.08 reference behavior. Source ownership is this
repository's main branch; the NomadFramework host adapter is a
separate integration job.

**Bootstrap status:** G00/G01 dependency and build-chain preparation,
not a completed GOAP solver or C ABI DLL.

- [Build chain and prerequisites](docs/BUILD_CHAIN.md)
- [FEAR SDK reference provenance and staging](docs/FEAR_SDK_REFERENCE.md)
- [Dependency lock](deps/dependencies.lock.json)
- [Original G00-G11 and D00-D08 implementation plan](https://github.com/SIGAAMDAD/TheNomad_Studio/issues/6)

All GoAP native source and CI commits belong in this repository, not
TheNomad_Studio. The Studio provides job dispatch and review receipts.
