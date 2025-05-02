#include <iostream>
#include <string>
using namespace std;

// max number of items
const int MAX_ITEMS = 10;

// the array
class GroceryList {
private:
    string items[MAX_ITEMS];

    int itemCount; 
public:

    GroceryList() {
        itemCount = 0;
    }

    // the function to add a new item
    void addItem(string itemName) {
        if (itemCount < MAX_ITEMS) {
            items[itemCount] = itemName;
            itemCount++;                
            cout << "Item '" << itemName << "' added to the list." << endl;
        } else {
            cout << "Grocery list is full!" << endl;
        }
    }

    // the function to display the grocery list
    void displayList() {
        if (itemCount == 0) {
            cout << "Grocery list is empty!" << endl;
            return;
        }

        cout << "Grocery List:" << endl;
        for (int i = 0; i < itemCount; i++) {
            cout << "- " << items[i] << endl;
        }
    }

    // you have to type the name in to remove it
    void removeItem(string itemName) {
        int index = -1;

        // to find the item in the array
        for (int i = 0; i < itemCount; i++) {
            if (items[i] == itemName) {
                index = i;
                break;
            }
        }

        // if item not found
        if (index == -1) {
            cout << "Item '" << itemName << "' not found in the list." << endl;
            return;
        }

        // it moves the items to the left to remove the found item
        for (int i = index; i < itemCount - 1; i++) {
            items[i] = items[i + 1];
        }