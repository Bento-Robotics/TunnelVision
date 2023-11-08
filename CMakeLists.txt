cmake_minimum_required(VERSION 3.26)
project(TunnelVision)

set(CMAKE_CXX_STANDARD 14)
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(TunnelVision
        src/changeResolution.cpp)
target_link_libraries(TunnelVision ${OpenCV_LIBS})
