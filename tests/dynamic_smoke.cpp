// Verify that a C-compatible symbol can be resolved from the actual DLL/SO.
#include <stdint.h>
#if defined(_WIN32)
  #include <windows.h>
#else
  #include <dlfcn.h>
#endif

typedef uint32_t (*NmdProbeFn)( void );

int main( int argc, char** argv )
{
    if (argc != 2)
    {
        return 10;
    }
#if defined(_WIN32)
    HMODULE hModule = LoadLibraryA(argv[1]);
    if (!hModule)
    {
        return 11;
    }
    NmdProbeFn pProbe = (NmdProbeFn)GetProcAddress(hModule, "nmdgoap_bootstrap_shared_probe");
    const bool bResult = pProbe && pProbe() == 0x4E4D4447u;
    FreeLibrary(hModule);
#else
    void* pModule = dlopen(argv[1], RTLD_NOW | RTLD_LOCAL);
    if (!pModule)
    {
        return 11;
    }
    NmdProbeFn pProbe = (NmdProbeFn)dlsym(pModule, "nmdgoap_bootstrap_shared_probe");
    const bool bResult = pProbe && pProbe() == 0x4E4D4447u;
    dlclose(pModule);
#endif
    return bResult ? 0 : 12;
}
