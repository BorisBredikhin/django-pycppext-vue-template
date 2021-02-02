cmake_minimum_required(VERSION 3.17)
project(checkers)

set(CMAKE_CXX_STANDARD 20)
FIND_PACKAGE(PythonLibs REQUIRED)
FIND_PACKAGE(PythonInterp REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})

find_package(Boost COMPONENTS python REQUIRED)
include_directories(${Boost_INCLUDE_DIR})

add_library(cppcheckers SHARED cppcheckers.cpp)
target_link_libraries(cppcheckers ${PYTHON_LIBRARIES})
set_target_properties(
        cppcheckers
        PROPERTIES
            PREFIX ""
            OUTPUT_NAME cppcheckers
            LINKER_LANGUAGE CXX
)

#target_link_libraries(checkers LINK_PUBLIC ${Boost_LIBRARIES})
#target_link_libraries(checkers LINK_PUBLIC yaml-cpp)