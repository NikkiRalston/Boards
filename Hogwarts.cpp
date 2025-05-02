#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

// making base class called Student
class Student {
protected:
    string name;
    int spellPower;
    int housePoints;

public:
    Student(string n) {
        name = n;
        spellPower = 10;
        housePoints = 10;
    }

    virtual void displayStats() const {
        cout << "\nStudent: " << name << "\n";
        cout << "Spell Power: " << spellPower << "\n";
        cout << "House Points: " << housePoints << "\n";
    }

    int getSpellPower() const { return spellPower; }
    int getHousePoints() const { return housePoints; }
    string getName() const { return name; }
};

// making a derived class called RavenclawStudent
class RavenclawStudent : public Student {
public:
    RavenclawStudent(string n) : Student(n) {
        spellPower += 5; // the Ravenclaw get bonus Spell Power
    }

    // The reference usage boost bonus spell power
    void practiceSpells(int& bonus) {
        cout << "You have performed a flawless Expelliarmus infront of the Professors!\n";
        bonus += 5;
    }
};

// the function to calculate the student's hiring score
int evaluateByHouse(int spellPower, int housePoints) {
    return (spellPower * 2) + (housePoints * 3);
}

// the interview function
int beginHiringTrial(RavenclawStudent& s) {
    srand(time(0));
    int bonus = 0;

    cout << "\nYou stand in front of the Hogwarts Hiring Panel...\n";
    cout << "Professor McGonagall adjusts her glasses. \"Answer wisely,\" she warns.\n\n";

    // The three questions you will be asked 
    for (int i = 0; i < 3; i++) {
        cout << "Q" << i + 1 << ": ";
        if (i == 0)
            cout << "Which spell disarms your opponent? (a) Expelliarmus (b) Avada Kedavra (c) Lumos: ";
        else if (i == 1)
            cout << "Who is the headmaster of Hogwarts? (a) Voldemort (b) Dumbledore (c) Filch: ";
        else
            cout << "Choose a magical pet: (a) Basilisk (b) Toad (c) Owl: ";

        char answer;
        cin >> answer;

        if ((i == 0 && answer == 'a') || (i == 1 && answer == 'b') || (i == 2 && answer == 'c')) {
            bonus += 5;
            cout << "Well done! 5 points to your house.\n";
        } else {
            bonus -= 5;
            cout << "Curious choice.\n";
        }
    }
	// getting reference used at the end
    s.practiceSpells(bonus); 

    // the pointer used to hold final score which also shows at the end of the code
    int* scorePtr = new int;
    *scorePtr = evaluateByHouse(s.getSpellPower() + bonus, s.getHousePoints());

    int finalScore = *scorePtr;
    delete scorePtr;

    return finalScore;
}

// the main program
int main() {
    string name;
    cout << "Welcome to the Hogwarts Hiring Exam!\n";
    cout << "The role of Assistant Charms Professor is open.\n\n";

    // getting student's name
    cout << "State your name, young wizard: ";
    getline(cin, name);

    RavenclawStudent student(name);
    student.displayStats();

    int finalScore = beginHiringTrial(student);

    // the final evaluation
    cout << "\nFinal Score: " << finalScore << endl;
    if (finalScore >= 70) {
        cout << "Excellent work, Professor " << name << "! You're hired.\n";
    } else {
        cout << "Alas, not this time. Consider more time on training.\n";
    }

    return 0;
}
