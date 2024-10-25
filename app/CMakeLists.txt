cmake_minimum_required(VERSION 3.19)

project(app)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_BINARY_DIR}")

include(conanbuildinfo)
conan_check_compiler()
conan_set_find_paths()
conan_set_fpic()
conan_set_std()
conan_set_libcxx()
conan_output_dirs_setup()

find_package(liba REQUIRED)
find_package(libb REQUIRED)

add_executable(${PROJECT_NAME}
  src/app.cpp)

target_compile_definitions(${PROJECT_NAME}
  PRIVATE
    VERSION="${VERSION}")

target_link_libraries(${PROJECT_NAME}
  PRIVATE 
    liba::liba
    libb::libb)
