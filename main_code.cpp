#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    ifstream tempfile;
    tempfile.open("example.txt");
    if (!tempfile.is_open()) {
        cerr << "Error opening the file!" << endl;
        return 1; // Return non-zero value to indicate failure
    }
    string line;

    int input[784];
    for(int a=0;a<28;a++)
    {
        getline(tempfile,line);
        for(int j=0;j<28;j++)
        {
            char tempchar=line[j];
            input[a*28+j]=(line[j]-'0');
        }
        cout<<line<<endl;
    }
    tempfile.close();
    int o=0;
}
