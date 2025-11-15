cmake_minimum_required(VERSION 3.10)
project(Lab2)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Основная программа
add_executable(lab2
        main.cpp
        PostMachineCommand.cpp
        PostMachineTape.cpp
        PostMachineHead.cpp
        PostMachine.cpp
        Menu.cpp
)

# Тесты
add_executable(lab2_tests
        tests.cpp
        PostMachineCommand.cpp
        PostMachineTape.cpp
        PostMachineHead.cpp
        PostMachine.cpp
        Menu.cpp
)

# Пути к GTest
target_include_directories(lab2_tests PRIVATE /opt/homebrew/include)
target_link_directories(lab2_tests PRIVATE /opt/homebrew/lib)
target_link_libraries(lab2_tests
        gtest
        gtest_main
        pthread
)