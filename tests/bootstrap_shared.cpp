// G01 temporary export to validate .dll/.so linking and symbol lookup.
// This is explicitly not part of the eventual G02 versioned C ABI.
#include <stdint.h>
#if defined(_WIN32)
  #define NMDGOAP_BUILD_EXPORT __declspec(dllexport)
#else
  #define NMDGOAP_BUILD_EXPORT __attribute__((visibility("default")))
#endif
extern "C" uint32_t nmdgoap_bootstrap_core_probe( void );
extern "C" NMDGOAP_BUILD_EXPORT uint32_t nmdgoap_bootstrap_shared_probe( void )
{
    return nmdgoap_bootstrap_core_probe();
}
