#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
cout<<"Please enter a pisitive integer greater than 9: ";

    int steps = 0;
    while (n > 9) {
        int sum = 0;
        int temp = n;
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        n = sum;
        steps++;
        cout << n;
        if (n > 9) cout << " → ";
    }

    cout << "\nFinal value: " << n << endl;
    cout << "Total steps: " << steps << endl;

    return 0;
}