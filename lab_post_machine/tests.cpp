#include <gtest/gtest.h>
#include "PostMachineCommand.h"
#include "PostMachineTape.h"
#include "PostMachineHead.h"
#include "PostMachine.h"
#include <sstream>
#include <fstream>

// Тесты для PostMachineCommand
TEST(PostMachineCommandTest, DefaultConstructor) {
    PostMachineCommand cmd;
    EXPECT_EQ(cmd.getId(), 0);
    EXPECT_EQ(cmd.getCondition(), false);
    EXPECT_EQ(cmd.getAction(), ' ');
    EXPECT_EQ(cmd.getNextCommandId(), 0);
}

TEST(PostMachineCommandTest, ParameterizedConstructor) {
    PostMachineCommand cmd(1, true, 'V', 2);
    EXPECT_EQ(cmd.getId(), 1);
    EXPECT_EQ(cmd.getCondition(), true);
    EXPECT_EQ(cmd.getAction(), 'V');
    EXPECT_EQ(cmd.getNextCommandId(), 2);
}

TEST(PostMachineCommandTest, Getters) {
    PostMachineCommand cmd(5, false, 'X', 3);
    EXPECT_EQ(cmd.getId(), 5);
    EXPECT_EQ(cmd.getCondition(), false);
    EXPECT_EQ(cmd.getAction(), 'X');
    EXPECT_EQ(cmd.getNextCommandId(), 3);
}

// Тесты для PostMachineTape
TEST(PostMachineTapeTest, DefaultConstructor) {
    PostMachineTape tape;
    EXPECT_EQ(tape.getValue(0), false);
    EXPECT_EQ(tape.getValue(10), false);
    EXPECT_EQ(tape.getValue(-10), false);
    EXPECT_EQ(tape.getValue(50), false);
    EXPECT_EQ(tape.getValue(-50), false);
}

TEST(PostMachineTapeTest, ChangeValue) {
    PostMachineTape tape;
    tape.changeValue(5, true);
    EXPECT_EQ(tape.getValue(5), true);

    tape.changeValue(5, false);
    EXPECT_EQ(tape.getValue(5), false);

    tape.changeValue(-5, true);
    EXPECT_EQ(tape.getValue(-5), true);
}

TEST(PostMachineTapeTest, LoadFromStream) {
    PostMachineTape tape;
    std::istringstream iss("1010");
    tape.loadFromStream(iss);

    EXPECT_EQ(tape.getValue(0), true);
    EXPECT_EQ(tape.getValue(1), false);
    EXPECT_EQ(tape.getValue(2), true);
    EXPECT_EQ(tape.getValue(3), false);
    EXPECT_EQ(tape.getValue(4), false); // За пределами загруженных данных
}

TEST(PostMachineTapeTest, PrintTapeState) {
    PostMachineTape tape;
    tape.changeValue(0, true);
    tape.changeValue(1, false);
    tape.changeValue(2, true);

    testing::internal::CaptureStdout();
    tape.printTapeState(0, 2);
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("101") != std::string::npos);
}

// Тесты для PostMachineHead
TEST(PostMachineHeadTest, Initialization) {
    PostMachineTape tape;
    PostMachineHead head(tape);

    EXPECT_EQ(head.getCurrentPosition(), 0);
    EXPECT_EQ(head.read(), false);
}

TEST(PostMachineHeadTest, Movement) {
    PostMachineTape tape;
    PostMachineHead head(tape);

    head.moveRight();
    EXPECT_EQ(head.getCurrentPosition(), 1);

    head.moveLeft();
    EXPECT_EQ(head.getCurrentPosition(), 0);

    head.moveLeft();
    EXPECT_EQ(head.getCurrentPosition(), -1);

    head.moveRight();
    head.moveRight();
    EXPECT_EQ(head.getCurrentPosition(), 1);
}

TEST(PostMachineHeadTest, ReadWrite) {
    PostMachineTape tape;
    PostMachineHead head(tape);

    head.write(true);
    EXPECT_EQ(head.read(), true);

    head.write(false);
    EXPECT_EQ(head.read(), false);

    head.moveRight();
    head.write(true);
    EXPECT_EQ(head.read(), true);
    EXPECT_EQ(tape.getValue(1), true);
}

TEST(PostMachineHeadTest, SetPosition) {
    PostMachineTape tape;
    PostMachineHead head(tape);

    head.setPosition(10);
    EXPECT_EQ(head.getCurrentPosition(), 10);

    head.setPosition(-5);
    EXPECT_EQ(head.getCurrentPosition(), -5);

    head.setPosition(0);
    EXPECT_EQ(head.getCurrentPosition(), 0);
}

// Тесты для PostMachine
TEST(PostMachineTest, DefaultConstructor) {
    PostMachine machine;
    EXPECT_FALSE(machine.isHalted());
    EXPECT_EQ(machine.getCurrentCommand(), 1);
}

TEST(PostMachineTest, AddCommand) {
    PostMachine machine;
    PostMachineCommand cmd(1, false, 'V', 2);

    testing::internal::CaptureStdout();
    machine.addCommand(cmd);
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Команда 1") != std::string::npos);
}

TEST(PostMachineTest, ExecuteStepWithConditionMet) {
    PostMachine machine;
    PostMachineCommand cmd(1, false, 'V', 0); // Если пусто -> поставь метку -> стоп
    machine.addCommand(cmd);

    testing::internal::CaptureStdout();
    bool result = machine.executeStep();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(result);
    EXPECT_TRUE(machine.isHalted());
    EXPECT_TRUE(output.find("Команда: 1") != std::string::npos);
}

TEST(PostMachineTest, ExecuteStepWithConditionNotMet) {
    PostMachine machine;
    PostMachineCommand cmd(1, true, 'V', 0); // Если метка -> поставь метку -> стоп
    machine.addCommand(cmd);

    testing::internal::CaptureStdout();
    bool result = machine.executeStep();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(result);
    EXPECT_TRUE(machine.isHalted()); // Все равно остановится из-за nextCommandId = 0
}

TEST(PostMachineTest, MovementCommands) {
    PostMachine machine;
    PostMachineCommand cmd1(1, false, 'R', 2); // Движение вправо
    PostMachineCommand cmd2(2, false, 'L', 0); // Движение влево и стоп
    machine.addCommand(cmd1);
    machine.addCommand(cmd2);

    machine.executeStep(); // Выполняем первую команду
    machine.executeStep(); // Выполняем вторую команду

    EXPECT_TRUE(machine.isHalted());
}

TEST(PostMachineTest, AllActionTypes) {
    PostMachine machine;

    // Тестируем все типы действий
    PostMachineCommand cmdV(1, false, 'V', 2);  // Поставить метку
    PostMachineCommand cmdX(2, true, 'X', 3);   // Стереть метку (если есть)
    PostMachineCommand cmdL(3, false, 'L', 4);  // Движение влево
    PostMachineCommand cmdR(4, false, 'R', 0);  // Движение вправо и стоп

    machine.addCommand(cmdV);
    machine.addCommand(cmdX);
    machine.addCommand(cmdL);
    machine.addCommand(cmdR);

    // Выполняем все шаги
    while (machine.executeStep()) {}

    EXPECT_TRUE(machine.isHalted());
}

TEST(PostMachineTest, Reset) {
    PostMachine machine;
    machine.changeTapeValue(5, true);

    testing::internal::CaptureStdout();
    machine.reset();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_FALSE(machine.isHalted());
    EXPECT_EQ(machine.getCurrentCommand(), 1);
    EXPECT_TRUE(output.find("сброшено") != std::string::npos);
}

TEST(PostMachineTest, OperatorIncrement) {
    PostMachine machine;
    PostMachineCommand cmd(1, false, 'V', 0);
    machine.addCommand(cmd);

    // Тест префиксного инкремента
    ++machine;
    EXPECT_TRUE(machine.isHalted());
}

TEST(PostMachineTest, OperatorDecrement) {
    PostMachine machine;
    machine.changeTapeValue(5, true);

    // Тест префиксного декремента
    --machine;
    EXPECT_FALSE(machine.isHalted());
    EXPECT_EQ(machine.getCurrentCommand(), 1);
}

TEST(PostMachineTest, StartExecution) {
    PostMachine machine;
    PostMachineCommand cmd1(1, false, 'V', 2);
    PostMachineCommand cmd2(2, true, 'X', 0);
    machine.addCommand(cmd1);
    machine.addCommand(cmd2);

    testing::internal::CaptureStdout();
    machine.start();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Интерпретация завершена") != std::string::npos);
    EXPECT_TRUE(machine.isHalted());
}

TEST(PostMachineTest, ChangeTapeValue) {
    PostMachine machine;

    testing::internal::CaptureStdout();
    machine.changeTapeValue(10, true);
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Ячейка 10 изменена") != std::string::npos);
}

TEST(PostMachineTest, PrintCurrentState) {
    PostMachine machine;

    testing::internal::CaptureStdout();
    machine.printCurrentState();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Текущее состояние машины") != std::string::npos);
    EXPECT_TRUE(output.find("РАБОТАЕТ") != std::string::npos);
}

TEST(PostMachineTest, PrintAllCommands) {
    PostMachine machine;
    PostMachineCommand cmd1(1, false, 'V', 2);
    PostMachineCommand cmd2(2, true, 'X', 0);
    machine.addCommand(cmd1);
    machine.addCommand(cmd2);

    testing::internal::CaptureStdout();
    machine.printAllCommands();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Команда №1") != std::string::npos);
    EXPECT_TRUE(output.find("Команда №2") != std::string::npos);
    EXPECT_TRUE(output.find("усл=0") != std::string::npos);
    EXPECT_TRUE(output.find("усл=1") != std::string::npos);
}

TEST(PostMachineTest, EnableLogging) {
    PostMachine machine;
    PostMachineCommand cmd(1, false, 'V', 0);
    machine.addCommand(cmd);

    machine.enableLogging();
    testing::internal::CaptureStdout();
    machine.executeStep();
    std::string output = testing::internal::GetCapturedStdout();

    // С логированием должно быть больше информации
    EXPECT_TRUE(output.find("Шаг") != std::string::npos);
    EXPECT_TRUE(output.find("Команда: 1") != std::string::npos);
}

TEST(PostMachineTest, NonExistentCommand) {
    PostMachine machine;

    testing::internal::CaptureStdout();
    bool result = machine.executeStep(); // Пытаемся выполнить несуществующую команду
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_FALSE(result);
    EXPECT_TRUE(output.find("не найдена") != std::string::npos);
}

TEST(PostMachineTest, AlreadyHalted) {
    PostMachine machine;
    PostMachineCommand cmd(1, false, 'V', 0);
    machine.addCommand(cmd);
    machine.executeStep(); // Останавливаем машину

    testing::internal::CaptureStdout();
    bool result = machine.executeStep(); // Пытаемся выполнить шаг после остановки
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_FALSE(result);
    EXPECT_TRUE(output.find("уже остановлена") != std::string::npos);
}

TEST(PostMachineTest, FileOperations) {
    // Создаем тестовые файлы
    std::ofstream progFile("test_program.txt");
    progFile << "1 0 V 2\n2 0 X 0";
    progFile.close();

    std::ofstream tapeFile("test_tape.txt");
    tapeFile << "101";
    tapeFile.close();

    PostMachine machine;

    // Тестируем загрузку
    testing::internal::CaptureStdout();
    machine.loadProgramFromFile("test_program.txt");
    machine.loadTapeFromFile("test_tape.txt");
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Программа загружена") != std::string::npos);
    EXPECT_TRUE(output.find("Лента загружена") != std::string::npos);

    // Удаляем тестовые файлы
    remove("test_program.txt");
    remove("test_tape.txt");
}

TEST(PostMachineTest, ComplexProgram) {
    PostMachine machine;

    // Создаем программу: V -> R -> X -> L -> стоп
    PostMachineCommand cmd1(1, false, 'V', 2); // Поставить метку
    PostMachineCommand cmd2(2, false, 'R', 3); // Вправо
    PostMachineCommand cmd3(3, false, 'X', 4); // Стереть метку
    PostMachineCommand cmd4(4, false, 'L', 0); // Влево и стоп

    machine.addCommand(cmd1);
    machine.addCommand(cmd2);
    machine.addCommand(cmd3);
    machine.addCommand(cmd4);

    machine.start();

    EXPECT_TRUE(machine.isHalted());
}

int main(int argc, char **argv) {
    std::cout << "🧪 ЗАПУСК ТЕСТОВ МАШИНЫ ПОСТА" << std::endl;
    std::cout << "=============================" << std::endl;
    
    ::testing::InitGoogleTest(&argc, argv);
    int result = RUN_ALL_TESTS();
    
    std::cout << "=============================" << std::endl;
    if (result == 0) {
        std::cout << "🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!" << std::endl;
    } else {
        std::cout << "❌ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ" << std::endl;
    }
    std::cout << "=============================" << std::endl;
    
    return result;
}