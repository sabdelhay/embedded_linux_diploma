#include <iostream>

float MaxVal(float x, float y, float z);
float max = 0;
int main(){

    float x, y, z;
    

    std::cout << "Enter the first values" << std::endl;
    std::cin >> x;

    std::cout << "Enter the second value" << std::endl;
    std::cin >> y;
    
    std::cout << "Enter the third value" << std::endl;
    std::cin >> z;

    MaxVal(x, y,z);
    
    return 0;
}

float MaxVal(float x, float y, float z){

    if(x > y && x > z){
        std::cout << x << " is the maximum value" << std::endl;
        x = max;
    } else if(y > x && y > z){
        std::cout << y << " is the maximum value" << std::endl;
        y = max;
    }else{
        std::cout << z << " is the maximum value" << std::endl;
        z = max;
    }

    return max;
}