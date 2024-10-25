from conans import ConanFile, CMake, tools, python_requires


class LibAConan(ConanFile):
    name = "liba"
    description = "Lib A"

    generators = "cmake", "cmake_find_package"
    settings = "os", "arch", "compiler", "build_type", "toolchain"
    exports_sources = [
        "CMakeLists.txt",
        "include/*",
        "src/*",
    ]

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["VERSION"] = self.version or "unknown"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    # def layout(self):
    #     self.cpp.source.includedirs = ["include"]
    #     self.cpp.build.libdirs = ["lib"]

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.name = self.name

        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libs = ["a"]
