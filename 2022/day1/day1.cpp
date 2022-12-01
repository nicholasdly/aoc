
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

//
// Returns the largest value in a vector of integers.
//
int max(vector<int> numbers) {
    int largest = 0;

    for (int i=0; i < numbers.size(); i++) {
        if (numbers[i] > largest) {
            largest = numbers[i];
        }
    }

    return largest;
}

//
// Returns the sum of the top three largest values in a vector of integers.
//
int sumTopThree(vector<int> numbers) {
    int firstLargest = 0;
    int secondLargest = 0;
    int thirdLargest = 0;

    for (int i=0; i < numbers.size(); i++) {
        if (numbers[i] > firstLargest) {
            thirdLargest = secondLargest;
            secondLargest = firstLargest;
            firstLargest = numbers[i];
        } else if (numbers[i] > secondLargest) {
            thirdLargest = secondLargest;
            secondLargest = numbers[i];
        } else if (numbers[i] > thirdLargest) {
            thirdLargest = numbers[i];
        }
    }
    
    return firstLargest + secondLargest + thirdLargest;
}

int main() {
    fstream inputFile;
    inputFile.open("input.txt", ios::in);  // Opens input.txt for reading
    if (inputFile.is_open()) {

        string input;
        vector<int> elfCalories;  // List of total calories carried for each elf
        int calories = 0;  // An individual elf's total calories carried

        while (getline(inputFile, input)) {
            if (!input.empty()) {
                calories += stoi(input);  // Computes total of calories carried
            } else {
                elfCalories.push_back(calories);
                calories = 0;
            }
        }

        // cout << max(elfCalories) << "\n";  // Print largest total calories carried
        cout << sumTopThree(elfCalories) << "\n";
        inputFile.close();

    }
    return 0;
}
