#include "liba.h"

#include <sstream>
#include <iostream>

namespace liba {

std::string get_foo() {
  std::ostringstream oss;
  oss << "liba(" << VERSION << ")!";
  return oss.str();
}

void foo() {
  std::cout << get_foo() << std::endl;
}

}
