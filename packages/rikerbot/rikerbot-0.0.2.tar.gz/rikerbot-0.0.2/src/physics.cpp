#include "physics.hpp"

namespace rkr {

Vec3::Vec3(Vec3& other) : v {other.x, other.y, other.z} {};
Vec3::Vec3(float x, float y, float z) : v {x, y, z} {};
Vec3::Vec3(float vec[3]) : v {vec[0], vec[1], vec[2]} {};



} // namespace rkr
