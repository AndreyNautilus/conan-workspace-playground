cmake_minimum_required(VERSION 3.19)

project(a)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_check_compiler()
conan_set_find_paths()
conan_set_fpic()
conan_set_std()
conan_set_libcxx()
conan_output_dirs_setup()

add_library(${PROJECT_NAME} STATIC
  src/liba.cpp)

target_compile_definitions(${PROJECT_NAME}
  PRIVATE
    VERSION="${VERSION}")

target_include_directories(${PROJECT_NAME}
  PUBLIC
    include)

install(TARGETS ${PROJECT_NAME} DESTINATION lib)
install(DIRECTORY include DESTINATION .)