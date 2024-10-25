#include "libb.h"

#include <liba.h>

#include <sstream>
#include <iostream>

namespace libb {

std::string get_bar() {
  std::ostringstream oss;
  oss << "libb(" << VERSION << ")!";
  return oss.str();
}

void bar() {
  std::cout << liba::get_foo() << " - " << get_bar() << std::endl;
}

}
