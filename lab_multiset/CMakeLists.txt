cmake_minimum_required(VERSION 3.10)
project(Lab1)

set(CMAKE_CXX_STANDARD 17)

# Основное приложение
add_executable(lab1
        main.cpp
        Multiset.cpp
)

# Тесты
add_executable(lab1_tests
        tests.cpp
        Multiset.cpp
)

# Пути к GTest только для тестов
target_include_directories(lab1_tests PRIVATE /opt/homebrew/include)
target_link_directories(lab1_tests PRIVATE /opt/homebrew/lib)
target_link_libraries(lab1_tests
        gtest
        gtest_main
        pthread
)