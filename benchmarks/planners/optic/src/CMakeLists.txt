cmake_minimum_required(VERSION 2.4)
if(COMMAND cmake_policy)
    cmake_policy(SET CMP0003 NEW)
endif(COMMAND cmake_policy)

project(buildroot)

set(DOXYFILE_IN ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in)

set(CMAKE_CXX_FLAGS "-g3 -O -fprofile-arcs -Wno-conversion-null -Wno-enum-compare -Wno-maybe-uninitialized -Wno-switch -Wno-nonnull-compare -Wno-unused-but-set-variable -Wno-unused-variable -Wno-sign-compare")

set(CMAKE_CXX_FLAGS_PROFILE "-g3 -pg -O -fprofile-arcs -Wno-unused-but-set-variable -Wno-unused-variable -Wno-sign-compare")

set(CMAKE_CXX_LINK_FLAGS_PROFILE "-pg")

add_subdirectory(VALfiles)


if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/optic")
	add_subdirectory(optic)
endif(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/optic")
