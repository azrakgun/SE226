#include <iostream>
using namespace std;

 int task3() {
    int n;
    cin >> n;
    while (n < 3 || n > 9)
        cin >> n;


    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++)
            cout << j;
        cout << endl;
    }


    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= i; j++)
            cout << j;
        cout << endl;
    }

    return 0;
}