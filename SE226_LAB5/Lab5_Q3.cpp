#include <iostream>

using namespace std;

double total_gn = 0;

void calculate_gn(int n, double r) {


    double term = 1;
    for (int i = 0; i < n; i++) {
        term *= r;
    }


    total_gn += term;

    if (n > 0) {
        calculate_gn(n - 1, r);
    }
}

int main() {
    int n;
    double r;

    cout << "Enter n value: ";
    cin >> n;
    cout << "Enter r value: ";
    cin >> r;


    calculate_gn(n, r);


    cout << "Total gn (Global value): " << total_gn << endl;

    return 0;
}
