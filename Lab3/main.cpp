#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2) {
    int temp;
    temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr+i) << " ";
    }
    cout << endl;

}

int findMax(int *arr, int size){
    int max = *arr;
    for (int i = 1; i < size; i++) {
        if (*(arr+i) > max) {
            max = *(arr+i);

        }
    }
        return max;
    
void reverseArray(int* arr, int size){
    for(int i = 0; i < size / 2; i++) {
        int temp = *(arr + i);
        *(arr + i) = *(arr + size - 1 - i);
        *(arr + size - 1 - i) = temp;
    }

}

int *createArray(int size) {
    int* arr = new int[size];
    for (int i = 0; i < size; i++) {
      cin >> * (arr +i);
    }
    return arr;
}
void deleteArray(int* arr) {
    delete[] arr;

}
int main() {
    cout << "Creating dynamic array..." << endl;
    cout << "Enter array size: " << endl;
    int size;
    cin >> size;
    cout << "Enter values: " << endl;

    int * arr = createArray(size);
 
    cout << "Array elements:" << endl;
    printArray(arr, size);

    cout << "Maximum element: " << findMax(arr, size) << endl;

    cout << "--------------------------" << endl;
    cout << "Swapping two numbers" << endl;
    int a , b;
    cout << "Enter a: " ;
      cin >> a;
        cout << "Before swap" << endl;
    cout << "a=" << ",b=" << endl;
    swapValues(&a,&b);
      cout << "After swap" << endl;
    
      cout << "a=" << a << ",b=" << b<< endl;

    cout << "----------------------------------" << endl;

    cout << "Reversing array..." << endl;
    reverseArray(arr, size);

    cout << "Array after reverseArray:" << endl;
    printArray(arr, size);

    cout << "----------------------------------" << endl;

    cout << "Deleting array..." << endl;
    deleteArray(arr);
    cout << "Memory released successfully." << endl;

    return 0;
}


