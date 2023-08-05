#ifndef BLOCKDATA_HPP
#define BLOCKDATA_HPP

#include <cstdint>
#include <string>
#include <vector>
#include <optional>

/*
 this.metadata = this.stateId - blockEnum.minStateId
 let data = this.metadata
 for (let i = blockEnum.states.length - 1; i >= 0; i--) {
   const prop = blockEnum.states[i]
   properties[prop.name] = propValue(prop, data % prop.num_values)
   data = Math.floor(data / prop.num_values)
 }
*/

namespace mcd {

struct MCBlockPropertyData {
  std::string name;
  std::uint8_t num_values;
};

struct MCBlockData {
  std::uint64_t id;
  std::uint64_t min_state_id;
  std::uint64_t max_state_id;
  std::uint64_t default_state;
  std::uint16_t stack_size;
  std::uint8_t emit_light;
  std::uint8_t filter_light;
  float hardness;

  std::string name;
  std::string display_name;

  bool diggable;
  bool collidable;
  bool transparent;

  std::vector<std::uint64_t> drops;
  std::vector<MCBlockPropertyData> props;

  std::optional<std::string> material;
};

extern MCBlockData

} // namespace mcd
#endif // BLOCKDATA_HPP
