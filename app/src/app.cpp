#include <liba.h>
#include <libb.h>

#include <iostream>


int main() {
  std::cout << "app(" << VERSION << "): " << liba::get_foo() << "; " << libb::get_bar() << std::endl;
  return 0;
}