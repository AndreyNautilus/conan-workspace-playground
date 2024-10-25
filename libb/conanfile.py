from conans import ConanFile, CMake, tools, python_requires


class LibBConan(ConanFile):
    name = "libb"
    description = "Lib B"

    generators = "cmake", "cmake_find_package"
    settings = "os", "arch", "compiler", "build_type", "toolchain"
    exports_sources = [
        "CMakeLists.txt",
        "include/*",
        "src/*",
        "tests/*",
    ]
    requires = (
        "liba/[>=1.0]@andrey/stable",
    )

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["VERSION"] = self.version or "unknown"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

        if not tools.cross_building(self.settings) and self.should_test:
            self.run(
                f"ctest --build-config {self.settings.build_type} --output-on-failure",
                run_environment=True,
            )

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.name = self.name

        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libs = ["b"]
