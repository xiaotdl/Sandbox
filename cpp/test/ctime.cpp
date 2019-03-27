#include <ctime>
#include <iostream>

int main()
{
    std::time_t result = std::time(nullptr);
    std::cout << (int64_t) result << std::endl;
    std::cout << std::ctime(&result);
    std::cout << std::getenv("USER") << std::endl;
}
