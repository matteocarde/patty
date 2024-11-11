# CMakeLists.txt has to be located in the project folder and cmake has to be
# executed from 'project/build' with 'cmake ../'.
cmake_minimum_required(VERSION 3.9)
project(lama
    VERSION 0.1
    DESCRIPTION "LAMA Planner"
)
find_package(Rock)
rock_init()

configure_file( ${CMAKE_CURRENT_SOURCE_DIR}/plan.in ${CMAKE_CURRENT_BINARY_DIR}/lama-planner)

add_subdirectory(lama)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/lama-planner
    PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
    DESTINATION bin
    )

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lama/translate
    DESTINATION lib/lama/
)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/lama/translate/translate.py
    PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
    DESTINATION lib/lama/translate
)
