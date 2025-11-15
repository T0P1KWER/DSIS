
#ifndef LAB1_1_MULTISET_H
#define LAB1_1_MULTISET_H


#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>

class Multiset {
private:
    std::vector<std::pair<std::string, int>> elements;

    std::string delete_space(const std::string& str);
    std::string delete_inside_braces(const std::string& str);
    void process_current_element(const std::string& current_element,
                                std::vector<std::pair<std::string, int>>& target);
    void parse_elements_from_string(const std::string& str,
                                   std::vector<std::pair<std::string, int>>& target);
    void remove_element_by_index(int index);
    bool find_element_in_other_set(const std::string& element,
                                  const Multiset& other, int& count) const;
    void generate_subset_with_element(const std::string& element,
                                     int max_count,
                                     std::vector<std::vector<std::pair<std::string, int>>>& result);

public:
    Multiset();
    Multiset(const Multiset& other);

    void create_multiset(std::string& str);
    void print_multiset();
    static void print_multiset(std::vector<std::pair<std::string, int>>& set);
    void add_element(const std::string& str);
    void delete_element(const std::string& str);
    void get_power_multiset();
    void is_element_in_multiset(const std::string& str);
    void intersection(const Multiset& other);
    void union_set(const Multiset& other);
    void difference(const Multiset& other);
    void make_bulean();

    // Операторы
    Multiset operator+(const Multiset& other) const;
    Multiset& operator+=(const Multiset& other);
    Multiset operator*(const Multiset& other) const;
    Multiset& operator*=(const Multiset& other);
    Multiset operator-(const Multiset& other) const;
    Multiset& operator-=(const Multiset& other);
    Multiset& operator=(const Multiset& other);

    ~Multiset() = default;
};



#endif