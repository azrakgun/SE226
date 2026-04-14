#include <iostream>
using namespace std;
int main (){
    int totalseconds;
    int hours,minutes,seconds;
    cout<<"Enter a large seconds: ";
    cin>>totalseconds;
    hours=totalseconds /3600;
    int remainingseconds=totalseconds % 3600;
    minutes=remainingseconds /60;
    seconds=remainingseconds %60;
    cout<<totalseconds << " second is "<< hours <<" hours,"<<minutes<<" minutes, and "<< seconds<< " seconds." << endl;
    return 0;
}
