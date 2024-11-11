#include <iostream>


int main(){

    std::cout << "Enter any letter: ";
    char l;
    std::cin >> l;

    switch (l)
    {
    case 'a':
        std::cout << "This letter is a vowel letter." << std::endl;
        break;
    case 'i':
        std::cout << "This letter is a vowel letter." << std::endl;
        break;
    case 'o':
        std::cout << "This letter is a vowel letter." << std::endl;
        break;
    case 'e':
        std::cout << "This letter is a vowel letter." << std::endl;
        break;
    case 'u':
        std::cout << "This letter is a vowel letter." << std::endl;
        break;    
    
    default: 
        std::cout << "This letter is not a vowel letter." << std::endl;

        break;
    }
    return 0;
}