// Build-only static core fixture. No finalized planner or memory API.
#include <stdint.h>
extern "C" uint32_t nmdgoap_bootstrap_core_probe( void )
{
    return 0x4E4D4447u;
}
