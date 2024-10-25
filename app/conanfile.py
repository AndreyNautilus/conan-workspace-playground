from conans import ConanFile, CMake, tools, python_requires
import os


class AppConan(ConanFile):
    name = "app"
    description = "App"

    generators = "cmake", "cmake_find_package"
    settings = "os", "arch", "compiler", "build_type", "toolchain"
    exports_sources = [
        "CMakeLists.txt",
        "include/*",
        "src/*",
    ]
    requires = (
        "liba/[>=1.0]@andrey/stable",
        "libb/[>=1.0]@andrey/stable",
    )

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["VERSION"] = self.version or "unknown"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

        if not tools.cross_building(self.settings):
            with tools.chdir("bin"):
                self.run(os.path.join(".", "app"), run_environment=True)
