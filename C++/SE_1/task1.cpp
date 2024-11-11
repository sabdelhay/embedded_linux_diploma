#include <iostream>

int main(){
    std::cout << "================" << std::endl;
    std::cout << "| Char  | " << "ASCII|" << std::endl;
    std::cout << "================" << std::endl;

    for(int i= 0; i < 128; i++){
        char c = int(i);
        std::cout << "   "<< i << "\t|  " << c << std::endl;
    }

    return 0;
}
