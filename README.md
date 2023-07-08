libRangeMap
libRangeMap is a C++ library that provides a mapping functionality to map a given value within a certain range to a different range. It supports both numeric and character values, with characters being mapped to their respective positions in the alphabet.

Features
Map a value within a specified input range to an output range.
Support for both numeric and character values.
Numeric values are linearly mapped to the output range.
Character values are mapped to their respective positions in the alphabet.
Getting Started
Prerequisites
C++ compiler with C++11 support.
Usage
Include the libRangeMap.h header file in your project.

Create an instance of the RANGEMAP::RangeMapper class, specifying the input range, and optionally, the output range.
// Example for mapping integers within the range [0, 100] to the range [0.0, 1.0]
RANGEMAP::RangeMapper<int> mapper(0, 100, 0.0, 1.0);
Use the map() function to map a value to the output range.
// Map a value to the output range
float mappedValue = mapper.map(50); // Example: Mapping the value 50
You can also retrieve the input and output ranges using the getInputRange() and getOutputRange() functions.
// Get the input range
std::vector<int> inputRange = mapper.getInputRange();

// Get the output range
std::vector<float> outputRange = mapper.getOutputRange();
// Get the input range
std::vector<int> inputRange = mapper.getInputRange();

// Get the output range
std::vector<float> outputRange = mapper.getOutputRange();
Examples
Example 1: Mapping Integer Values
#include "libRangeMap.h"
#include <iostream>

int main() {
    // Create a RangeMapper instance to map integers within the range [0, 100] to the range [0.0, 1.0]
    RANGEMAP::RangeMapper<int> mapper(0, 100, 0.0, 1.0);

    // Map a value to the output range
    float mappedValue = mapper.map(50); // Mapping the value 50

    // Output the mapped value
    std::cout << "Mapped Value: " << mappedValue << std::endl;

    return 0;
}
Example 2: Mapping Character Values
#include "libRangeMap.h"
#include <iostream>

int main() {
    // Create a RangeMapper instance to map characters within the range ['A', 'Z'] to the range [0.0, 1.0]
    RANGEMAP::RangeMapper<char> mapper('A', 'Z', 0.0, 1.0);

    // Map a value to the output range
    float mappedValue = mapper.map('D'); // Mapping the character 'D'

    // Output the mapped value
    std::cout << "Mapped Value: " << mappedValue << std::endl;

    return 0;
}
License
This project is licensed under the MIT License.

Contributions
Contributions to the libRangeMap library are welcome! If you find a bug, have a feature request, or want to contribute code improvements, please open an issue or submit a pull request on the GitHub repository.

Acknowledgments
The libRangeMap library was developed by Aryn M. Sparks as a personal project.