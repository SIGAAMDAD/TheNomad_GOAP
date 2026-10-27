include(FetchContent)
set(EASTL_BUILD_TESTS OFF CACHE BOOL "Disable upstream tests" FORCE)
set(EASTL_BUILD_BENCHMARK OFF CACHE BOOL "Disable upstream benchmarks" FORCE)
set(EABASE_BUILD_TESTS OFF CACHE BOOL "Disable upstream tests" FORCE)
set(FETCHCONTENT_UPDATES_DISCONNECTED ON CACHE BOOL "No moving ref updates" FORCE)
# Offline mirrors: -DFETCHCONTENT_SOURCE_DIR_EASTL=<dir> -DFETCHCONTENT_SOURCE_DIR_EABASE=<dir>
FetchContent_Declare(EABase
  GIT_REPOSITORY https://github.com/electronicarts/EABase.git
  GIT_TAG 0699a15efdfd20b6cecf02153bfa5663decb653c
  GIT_SUBMODULES ""
)
FetchContent_MakeAvailable(EABase)
FetchContent_Declare(EASTL
  GIT_REPOSITORY https://github.com/electronicarts/EASTL.git
  GIT_TAG e323f67e5d93fdadcd44f7998069d804697b1945
  GIT_SUBMODULES ""
)
FetchContent_MakeAvailable(EASTL)
if(NOT TARGET EASTL OR NOT TARGET EABase)
  message(FATAL_ERROR "Pinned EASTL/EABase targets unavailable")
endif()
