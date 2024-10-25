# Copyright (C) 2022 TomTom NV. All rights reserved.
#
# This software is the proprietary copyright of TomTom NV and its subsidiaries and may be
# used for internal evaluation purposes or commercial use strictly subject to separate
# license agreement between you and TomTom NV. If you are the licensee, you are only permitted
# to use this software in accordance with the terms of your license agreement. If you are
# not the licensee, you are not authorized to use this software in any manner and should
# immediately return or destroy it.

cmake_minimum_required(VERSION 3.17)

project(test_package)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_check_compiler()
conan_set_find_paths()
conan_set_fpic()
conan_set_std()
conan_set_libcxx()
conan_output_dirs_setup()

find_package(libb REQUIRED)

add_executable(${PROJECT_NAME}
  test_package.cpp
)

target_link_libraries(${PROJECT_NAME}
  PRIVATE
    libb::libb
)
