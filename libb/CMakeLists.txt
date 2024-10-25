cmake_minimum_required(VERSION 3.19)

project(b)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_BINARY_DIR}")

include(conanbuildinfo)
conan_check_compiler()
conan_set_find_paths()
conan_set_fpic()
conan_set_std()
conan_set_libcxx()
conan_output_dirs_setup()

find_package(liba REQUIRED)

message("liba_LIB_DIRS = ${liba_LIB_DIRS}")

add_library(${PROJECT_NAME} STATIC
  src/libb.cpp)

target_compile_definitions(${PROJECT_NAME}
  PRIVATE
    VERSION="${VERSION}")

target_link_libraries(${PROJECT_NAME}
  PRIVATE 
    liba::liba)

target_include_directories(${PROJECT_NAME}
  PUBLIC
    include)

install(TARGETS ${PROJECT_NAME} DESTINATION lib)
install(DIRECTORY include DESTINATION .)

enable_testing()

add_subdirectory(tests)