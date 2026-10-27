// G01 dependency fixture; no GOAP logic or public ABI.
#include <EABase/eabase.h>
#include <EASTL/array.h>
#include <EASTL/fixed_vector.h>
#include <stdint.h>

int main( void )
{
    static_assert(sizeof(uint32_t) == 4, "requires uint32_t");
    eastl::fixed_vector<uint32_t, 8, false> values;
    values.push_back(11);
    values.push_back(23);
    values.push_back(31);
    const eastl::array<uint32_t, 3> expected = {{11, 23, 31}};
    for (uint32_t i = 0; i < 3; ++i)
    {
        if (values[i] != expected[i])
        {
            return 1;
        }
    }
    return values.size() == 3 ? 0 : 2;
}
