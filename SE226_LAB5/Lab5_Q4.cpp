#include <iostream>

using namespace std;


double calculate_gn_cpp(int n, double r) {

    if (n == 0) {
        return 1;
    }


    double term = 1;
    for(int i = 0; i < n; i++) {
        term *= r;
    }


    return term + calculate_gn_cpp(n - 1, r);
}

int main() {
    int n;
    double r;

    cout << "Enter n value : ";
    cin >> n;
    cout << "Enter r value : ";
    cin >> r;


    double result = calculate_gn_cpp(n, r);


    cout << "Result: " << result << endl;

    return 0;
}
