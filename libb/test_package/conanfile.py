# Copyright (C) 2022 TomTom NV. All rights reserved.
#
# This software is the proprietary copyright of TomTom NV and its subsidiaries and may be
# used for internal evaluation purposes or commercial use strictly subject to separate
# license agreement between you and TomTom NV. If you are the licensee, you are only permitted
# to use this software in accordance with the terms of your license agreement. If you are
# not the licensee, you are not authorized to use this software in any manner and should
# immediately return or destroy it.

from conans import ConanFile, CMake, tools
import os


class BTestConan(ConanFile):
    name = "b-test_pkg"
    settings = "os", "compiler", "build_type", "arch", "toolchain"
    generators = "cmake", "cmake_find_package"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            with tools.chdir("bin"):
                self.run(os.path.join(".", "test_package"), run_environment=True)
