# Conan workspace playground

- `app` is the top-level application. It depends on `liba` and `libb`.
- `libb` is a static library. It depends on `liba`. It also contains tests which transitevely depend on `liba`.
- `liba` is a simple static library.

Goal: create a conan-1.x workspace with `app` and `liba`. `libb` should not be in the workspace.

Install the packages:
```bash
conan create liba 1.0@andrey/stable
conan create libb 1.0@andrey/stable
```

Init and build the workspace:
```bash
cd build
conan workspace install ../workspace.yml --build=outdated
cd ..
cmake -GNinja . -Bbuild
cmake --build build
./app/build/bin/app
```
Everything works, but `liba` is not _editable_.

If we add `liba/0.1@andrey/ws` as `root:` in `workspace.yml` and try to re-install the workspace:
```bash
cd build
conan workspace install ../workspace.yml --build=outdated
```
it fails with:
```
[4/4] Linking CXX executable bin/b-unittests
FAILED: bin/b-unittests
: && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk -mmacosx-version-min=13.5 -gline-tables-only -arch arm64 -fcolor-diagnostics -fobjc-arc -stdlib=libc++ -O3 -DNDEBUG -arch arm64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk -mmacosx-version-min=13.5 -Wl,-search_paths_first -Wl,-headerpad_max_install_names -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk -mmacosx-version-min=13.5 -gline-tables-only -arch arm64 tests/CMakeFiles/b-unittests.dir/libb_test.cpp.o -o bin/b-unittests  lib/libb.a  -la && :
ld: library 'a' not found
clang: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.
```
