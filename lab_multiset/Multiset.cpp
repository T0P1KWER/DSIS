

#include "Multiset.h"
using namespace std;

string Multiset::delete_space(const string& str) {
    string result;
    for (char c : str) {
        if (c != ' ') result += c;
    }
    return result;
}

string Multiset::delete_inside_braces(const string& str) {
    string result;
    int depth = 0;

    for (char c : str) {
        if (c == '{') {
            depth++;
            result += c;
        }
        else if (c == '}') {
            depth--;
            result += c;
        }
        else if (c == ',' && depth > 0) {
            result += ' ';
        }
        else {
            result += c;
        }
    }
    return result;
}

void Multiset::process_current_element(const string& current_element,
                                     vector<pair<string, int>>& target) {
    if (current_element.empty()) return;

    bool found = false;
    for (int y = 0; y < target.size(); y++) {
        if (current_element == target[y].first) {
            found = true;
            target[y].second++;
            break;
        }
    }
    if (!found) {
        target.push_back(make_pair(current_element, 1));
    }
}

void Multiset::parse_elements_from_string(const string& str,
                                        vector<pair<string, int>>& target) {
    string current_element;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] == ',') {
            process_current_element(current_element, target);
            current_element.clear();
        }
        else {
            current_element += str[i];
        }
    }
    process_current_element(current_element, target);
}

void Multiset::remove_element_by_index(int index) {
    for (int j = index; j < elements.size() - 1; j++) {
        elements[j] = elements[j + 1];
    }
    elements.pop_back();
}

bool Multiset::find_element_in_other_set(const string& element,
                                       const Multiset& other, int& count) const {
    for (int j = 0; j < other.elements.size(); j++) {
        if (other.elements[j].first == element) {
            count = other.elements[j].second;
            return true;
        }
    }
    return false;
}

void Multiset::generate_subset_with_element(const string& element,
                                          int max_count,
                                          vector<vector<pair<string, int>>>& result) {
    int current_size = result.size();
    for (int j = 0; j < current_size; j++) {
        for (int count = 1; count <= max_count; count++) {
            vector<pair<string, int>> new_subset = result[j];
            new_subset.push_back(make_pair(element, count));
            result.push_back(new_subset);
        }
    }
}

// Конструкторы
Multiset::Multiset() {}

Multiset::Multiset(const Multiset& other) {
    elements = other.elements;
}

// Публичные методы
void Multiset::create_multiset(string& str) {
    if (str.empty()) {
        elements.clear();
        return;
    }

    str[0] = ',';
    str[str.size() - 1] = ',';
    str = delete_inside_braces(str);
    str = delete_space(str);

    vector<pair<string, int>> parsed_elements;
    parse_elements_from_string(str, parsed_elements);
    elements = parsed_elements;
}

void Multiset::print_multiset() {
    for (int i = 0; i < elements.size(); i++) {
        cout << elements[i].first << "  "
             << "количество вхождений: " << elements[i].second << endl;
    }
}

void Multiset::print_multiset(vector<pair<string, int>>& set) {
    for (int i = 0; i < set.size(); i++) {
        cout << set[i].first << "  "
             << "количество вхождений: " << set[i].second << endl;
    }
}

void Multiset::add_element(const string& str) {
    for (int i = 0; i < elements.size(); i++) {
        if (elements[i].first == str) {
            elements[i].second++;
            return;
        }
    }
    elements.push_back(make_pair(str, 1));
}

void Multiset::delete_element(const string& str) {
    bool found = false;
    for (int i = 0; i < elements.size(); i++) {
        if (elements[i].first == str) {
            elements[i].second -= 1;
            found = true;

            if (elements[i].second == 0) {
                remove_element_by_index(i);
                i--;
            }
            break;
        }
    }
    if (!found) {
        cout << "такого элемента нет" << endl;
    }
}

void Multiset::get_power_multiset() {
    int result = 0;
    for (int i = 0; i < elements.size(); i++) {
        result += elements[i].second;
    }
    cout << "мощность мультимножества : " << result << endl;
}

void Multiset::is_element_in_multiset(const string& str) {
    bool found = false;
    int count = 0;
    for (int i = 0; i < elements.size(); i++) {
        if (elements[i].first == str) {
            found = true;
            count = elements[i].second;
            break;
        }
    }
    if (found) {
        cout << "элемент " << str << " входит в мультимножество "
             << count << " раз " << endl;
    }
}

void Multiset::intersection(const Multiset& other) {
    vector<pair<string, int>> result;
    for (int i = 0; i < elements.size(); i++) {
        string currentElement = elements[i].first;
        int currentCount = elements[i].second;
        int otherCount = 0;

        if (find_element_in_other_set(currentElement, other, otherCount)) {
            int minCount = min(currentCount, otherCount);
            result.push_back({ currentElement, minCount });
        }
    }
    cout << "Пересечение: ";
    for (int i = 0; i < result.size(); i++) {
        cout << result[i].first << "(" << result[i].second << ") ";
    }
    cout << endl;
}

void Multiset::union_set(const Multiset& other) {
    vector<pair<string, int>> result = elements;

    for (int i = 0; i < other.elements.size(); i++) {
        bool found = false;
        for (int j = 0; j < result.size(); j++) {
            if (other.elements[i].first == result[j].first) {
                found = true;
                if (other.elements[i].second > result[j].second) {
                    result[j].second = other.elements[i].second;
                }
                break;
            }
        }
        if (!found) {
            result.push_back(other.elements[i]);
        }
    }
    cout << "Объединение: ";
    Multiset::print_multiset(result);
}

void Multiset::difference(const Multiset& other) {
    vector<pair<string, int>> result = elements;
    for (int i = 0; i < other.elements.size(); i++) {
        string otherElement = other.elements[i].first;
        int otherCount = other.elements[i].second;
        for (int j = 0; j < result.size(); j++) {
            if (otherElement == result[j].first) {
                result[j].second = max(0, result[j].second - otherCount);
                if (result[j].second == 0) {
                    result.erase(result.begin() + j);
                    j--;
                }
                break;
            }
        }
    }
    cout << "Разность: " << endl;
    Multiset::print_multiset(result);
}

void Multiset::make_bulean() {
    vector<vector<pair<string, int>>> result;
    result.push_back(vector<pair<string, int>>());

    for (int i = 0; i < elements.size(); i++) {
        string current_element = elements[i].first;
        int max_count = elements[i].second;
        generate_subset_with_element(current_element, max_count, result);
    }

    cout << "Булеан (всего " << result.size() << " подмножеств):" << endl;
    for (int i = 0; i < result.size(); i++) {
        cout << "{ ";
        for (int j = 0; j < result[i].size(); j++) {
            cout << result[i][j].first;
            if (result[i][j].second > 1) {
                cout << "(" << result[i][j].second << ")";
            }
            if (j < result[i].size() - 1) {
                cout << ", ";
            }
        }
        cout << " }" << endl;
    }
}

// Операторы
Multiset Multiset::operator+(const Multiset& other) const {
    Multiset result = *this;
    result += other;
    return result;
}

Multiset& Multiset::operator+=(const Multiset& other) {
    for (int i = 0; i < other.elements.size(); i++) {
        bool found = false;
        for (int j = 0; j < elements.size(); j++) {
            if (other.elements[i].first == elements[j].first) {
                found = true;
                if (other.elements[i].second > elements[j].second) {
                    elements[j].second = other.elements[i].second;
                }
                break;
            }
        }
        if (!found) {
            elements.push_back(other.elements[i]);
        }
    }
    return *this;
}

Multiset Multiset::operator*(const Multiset& other) const {
    Multiset result;
    for (int i = 0; i < elements.size(); i++) {
        string currentElement = elements[i].first;
        int currentCount = elements[i].second;
        int otherCount = 0;

        if (find_element_in_other_set(currentElement, other, otherCount)) {
            int minCount = min(currentCount, otherCount);
            result.elements.push_back({ currentElement, minCount });
        }
    }
    return result;
}

Multiset& Multiset::operator*=(const Multiset& other) {
    *this = *this * other;
    return *this;
}

Multiset Multiset::operator-(const Multiset& other) const {
    Multiset result = *this;
    for (int i = 0; i < other.elements.size(); i++) {
        string otherElement = other.elements[i].first;
        int otherCount = other.elements[i].second;
        for (int j = 0; j < result.elements.size(); j++) {
            if (otherElement == result.elements[j].first) {
                result.elements[j].second = max(0, result.elements[j].second - otherCount);
                if (result.elements[j].second == 0) {
                    result.elements.erase(result.elements.begin() + j);
                    j--;
                }
                break;
            }
        }
    }
    return result;
}

Multiset& Multiset::operator-=(const Multiset& other) {
    *this = *this - other;
    return *this;
}

Multiset& Multiset::operator=(const Multiset& other) {
    if (this != &other) {
        elements = other.elements;
    }
    return *this;
}