// REF:
// https://stackoverflow.com/questions/25920681/what-is-the-difference-between-an-empty-and-a-null-stdshared-ptr-in-c

#include <iostream>
#include <memory>

int main()
{
    std::cout << "std::shared_ptr<int> ptr1:" << std::endl;
    {
        std::shared_ptr<int> ptr1;
        std::cout << "\tuse count before copying ptr: " << ptr1.use_count() << std::endl;
        std::shared_ptr<int> ptr2 = ptr1;
        std::cout << "\tuse count  after copying ptr: " << ptr1.use_count() << std::endl;
        std::cout << "\tptr1 is " << (ptr1 ? "not null" : "null") << std::endl;
    }
    std::cout << std::endl;

    std::cout << "std::shared_ptr<int> ptr1(nullptr):" << std::endl;
    {
        std::shared_ptr<int> ptr1(nullptr);
        std::cout << "\tuse count before copying ptr: " << ptr1.use_count() << std::endl;
        std::shared_ptr<int> ptr2 = ptr1;
        std::cout << "\tuse count  after copying ptr: " << ptr1.use_count() << std::endl;
        std::cout << "\tptr1 is " << (ptr1 ? "not null" : "null") << std::endl;
    }
    std::cout << std::endl;

    std::cout << "std::shared_ptr<int> ptr1(static_cast<int*>(nullptr))" << std::endl;
    {
        std::shared_ptr<int> ptr1(static_cast<int*>(nullptr));
        std::cout << "\tuse count before copying ptr: " << ptr1.use_count() << std::endl;
        std::shared_ptr<int> ptr2 = ptr1;
        std::cout << "\tuse count  after copying ptr: " << ptr1.use_count() << std::endl;
        std::cout << "\tptr1 is " << (ptr1 ? "not null" : "null") << std::endl;
    }
    std::cout << std::endl;

    return 0;
}
