#ifndef RKR_PHYSICS_HPP
#define RKR_PHYSICS_HPP

namespace rkr {

class Vec3 {
public:
  union {
    struct {
      float x, y, z;
    };
    float v[3];
  };

  Vec3() = default;
  Vec3(Vec3& other);
  Vec3(float x, float y, float z);
  Vec3(float v[3]);
};

} // namespace rkr
#endif // RKR_PHYSICS_HPP
