#include <vector>
#include <iostream>

int main(){
    int number;
    std::cout << "Enter a number: ";
    std::cin >> number;
    std::vector<int> basic_nmubers = {1,2,3,4,5,6,7,8,9,10,11,12};
    std::cout << "The multiplication table of number " << number << " is:"<< std::endl;
    for(int num : basic_nmubers){
        
        std::cout << num << " x " << number << " = " << number * num << std::endl;
    }

    return 0;
}