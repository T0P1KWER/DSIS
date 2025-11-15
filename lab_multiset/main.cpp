#include <iostream>
#include"Multiset.h"
#include <string>
using namespace std;




void displayMenu() {
    cout << "\n=== Меню работы с мультимножеством ===" << endl;
    cout << "1. Создать мультимножествa  " << endl;
    cout << "2. Добавить элемент " << endl;
    cout << "3. Вывести мультимножесвто  " << endl;
    cout << "4. Удалить элемент" << endl;
    cout << "5. Определить мощьность мультимножества" << endl;
    cout << "6. Проверить наличие элемента" << endl;
    cout << "7. Объеденение 2 мультимножеств" << endl;
    cout << "8. Пересечение 2 мультимножеств" << endl;
    cout << "9. Разность двух множеств" << endl;
    cout << "10. Построение булеана выбранного множества " << endl;
    cout << "11. Перегрузка оператора '=' " << endl;
    cout << "12. Перегрузка оператора '+' (объединение)" << endl;
    cout << "13. Перегрузка оператора '+=' (объединение с присваиванием)" << endl;
    cout << "14. Перегрузка оператора '*' (пересечение)" << endl;
    cout << "15. Перегрузка оператора '*=' (пересечение с присваиванием)" << endl;
    cout << "16. Перегрузка оператора '-' (разность)" << endl;
    cout << "17. Перегрузка оператора '-=' (разность с присваиванием)" << endl;
    cout << "0. Выход" << endl;
    cout << "Выберите действие: ";
}

int main() {
    setlocale(LC_ALL, "Russian");
    int c;
    string A, B, choice, element;
    Multiset a, b, result;
    do {
        displayMenu();
        cin >> c;
        cin.ignore();
        switch (c) {
        case 1:
            cout << "Введите первое мультимножество (по образцу {a, a, c, {a, b, b}, {}, {a, {c, c}}}): " << endl;
            getline(cin, A);
            cout << "Введите второе мультимножество (по образцу {a, a, c, {a, b, b}, {}, {a, {c, c}}}): " << endl;
            getline(cin, B);
            a.create_multiset(A);
            b.create_multiset(B);
            break;
        case 2:
            cout << "Введите множество в которое хотите добавит элемент(A/B)" << endl;
            getline(cin, choice);
            cout << "Введите какой элемент вы хотите добавить" << endl;
            getline(cin, element);
            if (choice[0] == 'B') {
                b.add_element(element);
            }
            else if (choice[0] == 'A')
            {
                a.add_element(element);
            }
            break;

        case 3:

            cout << "Введите множество для вывода(A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b.print_multiset();
            }
            else if (choice[0] == 'A')
            {
                a.print_multiset();
            }
            break;



        case 4:

            cout << "Введите множество в котором хотите удалить элемент(A/B)" << endl;
            getline(cin, choice);
            cout << "Введите какой элемент вы хотите удалить" << endl;
            getline(cin, element);
            if (choice[0] == 'B') {
                b.delete_element(element);
            }
            else if (choice[0] == 'A')
            {
                a.delete_element(element);
            }
            break;
        case 5:

            cout << "Введите множество для определения мощности(A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b.get_power_multiset();
            }
            else if (choice[0] == 'A')
            {
                a.get_power_multiset();
            }
            break;
        case 6:

            cout << "Введите множество для проверки элемента(A/B)" << endl;
            getline(cin, choice);
            cout << "введите элемент для получения информации о нём " << endl;
            getline(cin, element);
            if (choice[0] == 'B') {
                b.is_element_in_multiset(element);
            }
            else if (choice[0] == 'A')
            {
                a.is_element_in_multiset(element);
            }
            break;
        case 7:

            cout << "Введите множество для которого будет найдено пересечение с другим(A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b.intersection(a);
            }
            else if (choice[0] == 'A')
            {
                a.intersection(b);
            }
            break;
        case 8:
            cout << "Введите множество для которого будет найдено объеденение с другим(A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b.union_set(a);
            }
            else if (choice[0] == 'A')
            {
                a.union_set(b);
            }
            break;
        case 9:
            cout << "Введите множество для которого будет найдена разность  с другим(A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b.difference(a);
            }
            else if (choice[0] == 'A')
            {
                a.difference(b);
            }
            break;
        case 10:
            cout << "Введите множество для построения булеана (A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b.make_bulean();
            }
            else if (choice[0] == 'A')
            {
                a.make_bulean();
            }
            break;
        case 11:
            cout << "Введите множество для которого будет применёна перегрузка оператора '=' относительно другого (A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b = a;
            }
            else if (choice[0] == 'A')
            {
                a = b;
            }
            break;
        case 12:
            result = a + b;
            cout << "Результат объединения A + B:" << endl;
            result.print_multiset();
            break;
        case 13:
            cout << "Введите множество к которому добавить другое (A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b += a;
                cout << "Множество B после B += A:" << endl;
                b.print_multiset();
            }
            else if (choice[0] == 'A')
            {
                a += b;
                cout << "Множество A после A += B:" << endl;
                a.print_multiset();
            }
            break;
        case 14:
            result = a * b;
            cout << "Результат пересечения A * B:" << endl;
            result.print_multiset();
            break;
        case 15:
            cout << "Введите множество для пересечения с присваиванием (A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b *= a;
                cout << "Множество B после B *= A:" << endl;
                b.print_multiset();
            }
            else if (choice[0] == 'A')
            {
                a *= b;
                cout << "Множество A после A *= B:" << endl;
                a.print_multiset();
            }
            break;
        case 16:
            result = a - b;
            cout << "Результат разности A - B:" << endl;
            result.print_multiset();
            break;
        case 17:
            cout << "Введите множество для разности с присваиванием (A/B)" << endl;
            getline(cin, choice);
            if (choice[0] == 'B') {
                b -= a;
                cout << "Множество B после B -= A:" << endl;
                b.print_multiset();
            }
            else if (choice[0] == 'A')
            {
                a -= b;
                cout << "Множество A после A -= B:" << endl;
                a.print_multiset();
            }
            break;
        case 0:

        default:
            cout << "Неверный выбор!" << endl;
        }
    } while (c != 0);

    return 0;
}
/*
запуск с консоли
 переходишь в папку с проектом
потом
для запуска тестов сначала их собираем
g++ -std=c++17 -I/opt/homebrew/include -L/opt/homebrew/lib tests.cpp Multiset.cpp -o simple_tests -lgtest -lgtest_main -pthread
./simple_tests

*/