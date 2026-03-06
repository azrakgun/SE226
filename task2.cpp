#include <iostream>
using namespace std;

int task2 () {
    int n;
    cin >> n;
    while (n < 10 || n > 100)
        cin >> n;

    int fizz = 0, buzz = 0, fizzbuzz = 0;

    for (int i = 1; i <= n; i++) {
        if (i % 7 == 0) continue;
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz\n";
            fizzbuzz++;
        } else if (i % 3 == 0) {
            cout << "Fizz\n";
            fizz++;
        } else if (i % 5 == 0) {
            cout << "Buzz\n";
            buzz++;
        } else {
            cout << i << "\n";
        }
    }

    cout << "--- Summary ---\n";
    cout << "Fizz count : " << fizz << endl;
    cout << "Buzz count : " << buzz << endl;
    cout << "FizzBuzz count: " << fizzbuzz << endl;

    return 0;
}