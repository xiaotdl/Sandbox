# Makefile for Writing Make Files Example

# *****************************************************
# Variables to control Makefile operation

CXX = g++
CXXFLAGS = -Wall -g

# ****************************************************
# Targets needed to bring the executable up to date

main: main.o \
      Point.o \
      Rectangle.o
	$(CXX) $(CXXFLAGS) -o main main.o Point.o Rectangle.o

# The main.o target can be written more simply

main.o: main.cpp \
        Point.h \
        Rectangle.h
	$(CXX) $(CXXFLAGS) -c main.cpp

Point.o: Point.h
	$(CXX) $(CXXFLAGS) -c Point.cpp

Rectangle.o: Rectangle.h \
             Point.h
	$(CXX) $(CXXFLAGS) -c Rectangle.cpp
