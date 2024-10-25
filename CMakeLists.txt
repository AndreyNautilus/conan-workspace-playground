cmake_minimum_required(VERSION 3.19)

project(workspace)

include(${CMAKE_CURRENT_BINARY_DIR}/conanworkspace.cmake)

conan_workspace_subdirectories()

enable_testing()
