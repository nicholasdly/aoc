
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//
// Computes score of a turn based off of rules described in Part 1.
//
int computeScore1(int p1, int p2) {
    if ((p1 == 1 && p2 == 3) || (p1 == 2 && p2 == 1) || (p1 == 3 && p2 == 2)) {
        return p1 + 6;  // Win
    } else if ((p1 == 1 && p2 == 2) || (p1 == 2 && p2 == 3) || (p1 == 3 && p2 == 1)) {
        return p1;  // Loss
    }
    return p1 + 3;  // Draw
}

//
// Computes score of a turn based off of rules described in Part 2.
//
int computeScore2(int p1, int p2) {
    if (p1 == 1) {  // Must lose
        if (p2 > 1) {
            p1 = p2 - 1;
        } else {
            p1 = 3;
        }
        return computeScore1(p1, p2);
    } else if (p1 == 3) {  // Must win
        if (p2 < 3) {
            p1 = p2 + 1;
        } else {
            p1 = 1;
        }
        return computeScore1(p1, p2);
    }
    return computeScore1(p2, p2);  // Must draw

}

int main() {
    fstream inputFile;
    inputFile.open("input.txt", ios::in);  // Opens input.txt for reading
    if (inputFile.is_open()) {

        string input;
        int totalScore = 0;

        while (getline(inputFile, input)) {
            
            int p1;  // Player 1 move (you)
            int p2;  // Player 2 move (them)

            // Saves each player's move for the game
            if (input[2] == 'X') {
                p1 = 1;
            } else if (input[2] == 'Y') {
                p1 = 2;
            } else if (input[2] == 'Z') {
                p1 = 3;
            }
            if (input[0] == 'A') {
                p2 = 1;
            } else if (input[0] == 'B') {
                p2 = 2;
            } else if (input[0] == 'C') {
                p2 = 3;
            }

            // Computes score after each game
            // totalScore += computeScore1(p1, p2);
            totalScore += computeScore2(p1, p2);

        }

        cout << totalScore << "\n";

    }
    return 0;
}
