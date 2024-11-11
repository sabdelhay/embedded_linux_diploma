#include <iostream>
#include <bitset>

int main(){
    unsigned int bin;
    unsigned int dec;
    
    std::bitset<8> binToDec;
    

    std::cout << "Please Enter a binary number: ";
    std::cin >> binToDec;
    bin = binToDec.to_ulong();
    std::cout << bin << std::endl;

    std::cout << "Please Enter a decimal number: ";
    std::cin >> dec;
    std::bitset<8> decToBin(dec);
    std::cout << decToBin.to_string() << std::endl;

    return 0;
}