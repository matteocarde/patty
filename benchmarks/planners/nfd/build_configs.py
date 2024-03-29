release64 = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DALLOW_64_BIT=True",
    "-DCMAKE_CXX_FLAGS='-m64'",
]
debug64 = [
    "-DCMAKE_BUILD_TYPE=Debug",
    "-DALLOW_64_BIT=True",
    "-DCMAKE_CXX_FLAGS='-m64'",
]
minimal = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DALLOW_64_BIT=True",
    "-DCMAKE_CXX_FLAGS='-m64'",
    "-DDISABLE_PLUGINS_BY_DEFAULT=YES",
]

DEFAULT = "release64"
DEBUG = "debug64"
