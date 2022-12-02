cmake_minimum_required(VERSION 3.24)
project(AoC2022_cpp)

set(CMAKE_CXX_STANDARD 14)

include_directories(src/day02)

add_executable(day02 src/day02/main.cpp)
