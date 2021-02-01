cmake_minimum_required(VERSION 3.17)
project(checkers)

set(CMAKE_CXX_STANDARD 20)

find_package(Boost COMPONENTS program_options REQUIRED)
include_directories(${Boost_INCLUDE_DIR})

add_executable(checkers main.cpp)

target_link_libraries(checkers LINK_PUBLIC ${Boost_LIBRARIES})
target_link_libraries(checkers LINK_PUBLIC yaml-cpp)