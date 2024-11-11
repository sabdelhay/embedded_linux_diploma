#include <iostream>
#include <string>

int main() {
    int number;
    int sum;
    std::cout << "Enter a number: ";
    std::cin >> number;

    std::string numberStr = std::to_string(number);
    std::cout << "The sum of the digits [";
    for (char str : numberStr) {
        int digit = str - '0';
        sum += digit;
        std::cout << digit << " ";
    }
    std::cout << "] is: " << sum << std::endl;

    return 0;
}
