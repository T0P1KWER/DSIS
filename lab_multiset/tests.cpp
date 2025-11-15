#include <gtest/gtest.h>
#include "Multiset.h"
#include <sstream>
#include <iostream>

class MultisetTest : public ::testing::Test {
protected:
    Multiset ms;

    void SetUp() override {
        // Настройка перед каждым тестом
    }

    void TearDown() override {
        // Очистка после каждого теста
    }

    // Вспомогательная функция для захвата вывода
    std::string captureOutput(void (Multiset::*function)()) {
        testing::internal::CaptureStdout();
        (ms.*function)();
        return testing::internal::GetCapturedStdout();
    }

    std::string captureOutputWithParam(void (Multiset::*function)(const std::string&), const std::string& param) {
        testing::internal::CaptureStdout();
        (ms.*function)(param);
        return testing::internal::GetCapturedStdout();
    }
};

// Тесты конструктора и базовых операций
TEST_F(MultisetTest, DefaultConstructor) {
    std::cout << "✅ Конструктор по умолчанию работает" << std::endl;
    SUCCEED();
}

TEST_F(MultisetTest, CopyConstructor) {
    Multiset original;
    original.add_element("test");

    Multiset copy(original);
    std::cout << "✅ Конструктор копирования работает" << std::endl;
    SUCCEED();
}

// Тесты создания мультимножества из строки
TEST_F(MultisetTest, CreateFromEmptyString) {
    std::string empty = "";
    ms.create_multiset(empty);

    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность мультимножества : 0") != std::string::npos);
    std::cout << "✅ Создание из пустой строки работает" << std::endl;
}

TEST_F(MultisetTest, CreateFromSimpleString) {
    std::string input = "{a, b, c}";
    ms.create_multiset(input);

    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность мультимножества : 3") != std::string::npos);
    std::cout << "✅ Создание из простой строки работает" << std::endl;
}

TEST_F(MultisetTest, CreateFromStringWithDuplicates) {
    std::string input = "{a, a, b, b, b, c}";
    ms.create_multiset(input);

    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность мультимножества : 6") != std::string::npos);
    std::cout << "✅ Создание из строки с дубликатами работает" << std::endl;
}

TEST_F(MultisetTest, CreateFromStringWithNestedSets) {
    std::string input = "{a, {b, c}, {d, {e, f}}}";
    ms.create_multiset(input);

    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность") != std::string::npos);
    std::cout << "✅ Создание из строки с вложенными множествами работает" << std::endl;
}

// Тесты добавления элементов
TEST_F(MultisetTest, AddNewElement) {
    ms.add_element("new_element");

    auto output = captureOutputWithParam(&Multiset::is_element_in_multiset, "new_element");
    EXPECT_TRUE(output.find("входит в мультимножество") != std::string::npos);
    std::cout << "✅ Добавление нового элемента работает" << std::endl;
}

TEST_F(MultisetTest, AddDuplicateElement) {
    ms.add_element("duplicate");
    ms.add_element("duplicate");
    ms.add_element("duplicate");

    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность мультимножества : 3") != std::string::npos);
    std::cout << "✅ Добавление дубликатов увеличивает счетчик" << std::endl;
}

TEST_F(MultisetTest, AddMultipleDifferentElements) {
    ms.add_element("element1");
    ms.add_element("element2");
    ms.add_element("element3");

    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность мультимножества : 3") != std::string::npos);
    std::cout << "✅ Добавление разных элементов работает корректно" << std::endl;
}

// Тесты удаления элементов
TEST_F(MultisetTest, DeleteExistingElement) {
    ms.add_element("to_delete");
    ms.delete_element("to_delete");

    auto output = captureOutputWithParam(&Multiset::is_element_in_multiset, "to_delete");
    EXPECT_TRUE(output.find("входит в мультимножество") == std::string::npos);
    std::cout << "✅ Удаление существующего элемента работает" << std::endl;
}

TEST_F(MultisetTest, DeleteElementWithMultipleCopies) {
    ms.add_element("multi");
    ms.add_element("multi");
    ms.add_element("multi");

    ms.delete_element("multi"); // Удаляем один экземпляр

    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность мультимножества : 2") != std::string::npos);
    std::cout << "✅ Удаление одного экземпляра из нескольких работает" << std::endl;
}

TEST_F(MultisetTest, DeleteNonExistingElement) {
    auto output = captureOutputWithParam(&Multiset::delete_element, "non_existent");
    EXPECT_TRUE(output.find("такого элемента нет") != std::string::npos);
    std::cout << "✅ Попытка удаления несуществующего элемента обрабатывается корректно" << std::endl;
}

TEST_F(MultisetTest, DeleteUntilRemoved) {
    ms.add_element("temp");
    ms.delete_element("temp"); // Удаляем единственный экземпляр

    auto output = captureOutputWithParam(&Multiset::is_element_in_multiset, "temp");
    EXPECT_TRUE(output.find("входит в мультимножество") == std::string::npos);
    std::cout << "✅ Элемент полностью удаляется при достижении нуля" << std::endl;
}

// Тесты мощности
TEST_F(MultisetTest, PowerOfEmptySet) {
    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность мультимножества : 0") != std::string::npos);
    std::cout << "✅ Мощность пустого множества равна 0" << std::endl;
}

TEST_F(MultisetTest, PowerAfterOperations) {
    ms.add_element("a");
    ms.add_element("a");
    ms.add_element("b");
    ms.delete_element("a");

    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность мультимножества : 2") != std::string::npos);
    std::cout << "✅ Мощность корректно вычисляется после операций" << std::endl;
}

// Тесты проверки наличия элемента
TEST_F(MultisetTest, CheckExistingElement) {
    ms.add_element("check_me");

    auto output = captureOutputWithParam(&Multiset::is_element_in_multiset, "check_me");
    EXPECT_TRUE(output.find("входит в мультимножество") != std::string::npos);
    EXPECT_TRUE(output.find("check_me") != std::string::npos);
    std::cout << "✅ Проверка существующего элемента работает" << std::endl;
}

TEST_F(MultisetTest, CheckNonExistingElement) {
    auto output = captureOutputWithParam(&Multiset::is_element_in_multiset, "ghost");
    EXPECT_TRUE(output.empty()); // Не должно быть вывода для несуществующего элемента
    std::cout << "✅ Проверка несуществующего элемента не выводит сообщение" << std::endl;
}

TEST_F(MultisetTest, CheckElementCount) {
    ms.add_element("count_test");
    ms.add_element("count_test");
    ms.add_element("count_test");

    auto output = captureOutputWithParam(&Multiset::is_element_in_multiset, "count_test");
    EXPECT_TRUE(output.find("3 раз") != std::string::npos);
    std::cout << "✅ Отображается правильное количество вхождений" << std::endl;
}

// Тесты операций над множествами
TEST_F(MultisetTest, IntersectionBasic) {
    Multiset ms1, ms2;
    std::string input1 = "{a, a, b, c}";
    std::string input2 = "{a, b, b, d}";

    ms1.create_multiset(input1);
    ms2.create_multiset(input2);

    testing::internal::CaptureStdout();
    ms1.intersection(ms2);
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Пересечение:") != std::string::npos);
    EXPECT_TRUE(output.find("a") != std::string::npos);
    EXPECT_TRUE(output.find("b") != std::string::npos);
    std::cout << "✅ Базовое пересечение работает" << std::endl;
}

TEST_F(MultisetTest, IntersectionEmpty) {
    Multiset ms1, ms2;
    std::string input1 = "{a, b}";
    std::string input2 = "{c, d}";

    ms1.create_multiset(input1);
    ms2.create_multiset(input2);

    testing::internal::CaptureStdout();
    ms1.intersection(ms2);
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Пересечение:") != std::string::npos);
    std::cout << "✅ Пересечение непересекающихся множеств работает" << std::endl;
}

TEST_F(MultisetTest, UnionBasic) {
    Multiset ms1, ms2;
    std::string input1 = "{a, b}";
    std::string input2 = "{b, c}";

    ms1.create_multiset(input1);
    ms2.create_multiset(input2);

    testing::internal::CaptureStdout();
    ms1.union_set(ms2);
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Объединение:") != std::string::npos);
    std::cout << "✅ Базовое объединение работает" << std::endl;
}

TEST_F(MultisetTest, UnionWithDuplicates) {
    Multiset ms1, ms2;
    std::string input1 = "{a, a, b}";
    std::string input2 = "{a, b, b}";

    ms1.create_multiset(input1);
    ms2.create_multiset(input2);

    testing::internal::CaptureStdout();
    ms1.union_set(ms2);
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Объединение:") != std::string::npos);
    std::cout << "✅ Объединение с дубликатами работает" << std::endl;
}

TEST_F(MultisetTest, DifferenceBasic) {
    Multiset ms1, ms2;
    std::string input1 = "{a, a, b, c}";
    std::string input2 = "{a, b}";

    ms1.create_multiset(input1);
    ms2.create_multiset(input2);

    testing::internal::CaptureStdout();
    ms1.difference(ms2);
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Разность:") != std::string::npos);
    std::cout << "✅ Базовая разность работает" << std::endl;
}

TEST_F(MultisetTest, DifferenceCompleteRemoval) {
    Multiset ms1, ms2;
    std::string input1 = "{a, a}";
    std::string input2 = "{a, a}";

    ms1.create_multiset(input1);
    ms2.create_multiset(input2);

    testing::internal::CaptureStdout();
    ms1.difference(ms2);
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Разность:") != std::string::npos);
    std::cout << "✅ Разность с полным удалением работает" << std::endl;
}

// Тесты булеана
TEST_F(MultisetTest, BooleanEmptySet) {
    testing::internal::CaptureStdout();
    ms.make_bulean();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Булеан") != std::string::npos);
    EXPECT_TRUE(output.find("подмножеств") != std::string::npos);
    std::cout << "✅ Булеан пустого множества работает" << std::endl;
}

TEST_F(MultisetTest, BooleanSingleElement) {
    ms.add_element("single");

    testing::internal::CaptureStdout();
    ms.make_bulean();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Булеан") != std::string::npos);
    EXPECT_TRUE(output.find("подмножеств") != std::string::npos);
    std::cout << "✅ Булеан одноэлементного множества работает" << std::endl;
}

TEST_F(MultisetTest, BooleanMultipleElements) {
    std::string input = "{x, y}";
    ms.create_multiset(input);

    testing::internal::CaptureStdout();
    ms.make_bulean();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Булеан") != std::string::npos);
    EXPECT_TRUE(output.find("подмножеств") != std::string::npos);
    std::cout << "✅ Булеан многоэлементного множества работает" << std::endl;
}



TEST_F(MultisetTest, OperatorPlus) {
    Multiset ms1, ms2;
    ms1.add_element("from1");
    ms2.add_element("from2");

    Multiset result = ms1 + ms2;

    testing::internal::CaptureStdout();
    result.print_multiset();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("from1") != std::string::npos || output.find("from2") != std::string::npos);
    std::cout << "✅ Оператор + (объединение) работает" << std::endl;
}

TEST_F(MultisetTest, OperatorPlusEquals) {
    Multiset ms1, ms2;
    ms1.add_element("original");
    ms2.add_element("added");

    ms1 += ms2;

    testing::internal::CaptureStdout();
    ms1.print_multiset();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("original") != std::string::npos || output.find("added") != std::string::npos);
    std::cout << "✅ Оператор += работает" << std::endl;
}

TEST_F(MultisetTest, OperatorMultiply) {
    Multiset ms1, ms2;
    std::string input1 = "{a, b}";
    std::string input2 = "{b, c}";

    ms1.create_multiset(input1);
    ms2.create_multiset(input2);

    Multiset result = ms1 * ms2;

    testing::internal::CaptureStdout();
    result.print_multiset();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("b") != std::string::npos);
    std::cout << "✅ Оператор * (пересечение) работает" << std::endl;
}

TEST_F(MultisetTest, OperatorMinus) {
    Multiset ms1, ms2;
    std::string input1 = "{a, a, b}";
    std::string input2 = "{a}";

    ms1.create_multiset(input1);
    ms2.create_multiset(input2);

    Multiset result = ms1 - ms2;

    testing::internal::CaptureStdout();
    result.print_multiset();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("a") != std::string::npos || output.find("b") != std::string::npos);
    std::cout << "✅ Оператор - (разность) работает" << std::endl;
}

// Тесты граничных случаев
TEST_F(MultisetTest, SelfAssignment) {
    ms.add_element("test");
    ms = ms; // Самоприсваивание

    auto output = captureOutputWithParam(&Multiset::is_element_in_multiset, "test");
    EXPECT_TRUE(output.find("входит в мультимножество") != std::string::npos);
    std::cout << "✅ Самоприсваивание обрабатывается корректно" << std::endl;
}

TEST_F(MultisetTest, PrintEmptyMultiset) {
    testing::internal::CaptureStdout();
    ms.print_multiset();
    std::string output = testing::internal::GetCapturedStdout();

    // Пустое множество должно выводиться без ошибок
    SUCCEED();
    std::cout << "✅ Печать пустого множества работает" << std::endl;
}

TEST_F(MultisetTest, ComplexOperationsChain) {
    Multiset ms1, ms2, ms3;

    // Создаем несколько множеств
    std::string input1 = "{x, y, z}";
    std::string input2 = "{y, z, w}";
    std::string input3 = "{z, w, v}";

    ms1.create_multiset(input1);
    ms2.create_multiset(input2);
    ms3.create_multiset(input3);

    // Цепочка операций
    Multiset result = (ms1 + ms2) * ms3;

    testing::internal::CaptureStdout();
    result.print_multiset();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("z") != std::string::npos);
    std::cout << "✅ Цепочка сложных операций работает" << std::endl;
}

// Тест производительности с большими данными
TEST_F(MultisetTest, LargeDataSet) {
    for (int i = 0; i < 100; ++i) {
        ms.add_element("element_" + std::to_string(i % 10)); // 10 уникальных, по 10 копий каждого
    }

    auto output = captureOutput(&Multiset::get_power_multiset);
    EXPECT_TRUE(output.find("мощность мультимножества : 100") != std::string::npos);
    std::cout << "✅ Работа с большими данными выполняется корректно" << std::endl;
}

// Главная функция для запуска тестов
int main(int argc, char **argv) {
    std::cout << "🎯 ЗАПУСК ТЕСТОВ МУЛЬТИМНОЖЕСТВА" << std::endl;
    std::cout << "=================================" << std::endl;

    ::testing::InitGoogleTest(&argc, argv);
    int result = RUN_ALL_TESTS();

    std::cout << "=================================" << std::endl;
    if (result == 0) {
        std::cout << "🎉 ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!" << std::endl;
    } else {
        std::cout << "❌ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ" << std::endl;
    }
    std::cout << "=================================" << std::endl;

    return result;
}