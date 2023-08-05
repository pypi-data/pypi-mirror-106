#ifndef SHAPEDATA_HPP
#define SHAPEDATA_HPP

#include <vector>

namespace mcd {

struct MCBoundingBox {
  union {
    struct {
      float x, y, z;
    };
    float vec[3];
  } min, max;
};

extern std::vector<MCBoundingBox> shapes[];

} // namespace mcd
#endif // SHAPEDATA_HPP
