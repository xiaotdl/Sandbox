set -x
g++ -Wall -g -c -o main.o main.cpp
g++ -Wall -g -c -o Point.o Point.cpp
g++ -Wall -g -c -o Rectangle.o Rectangle.cpp
g++ -Wall -g -o main main.o Point.o Rectangle.o
