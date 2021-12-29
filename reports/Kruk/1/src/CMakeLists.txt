cmake_minimum_required(VERSION 3.20)
project(src)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(LAB_1
        class.h
        demonstration.cpp
        realization.cpp)
