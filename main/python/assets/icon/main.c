#include <stdlib.h>
#include <direct.h>

//gcc -o main.exe res\python\assets\icon\main.c res\python\assets\icon\icon.res -mwindows

int main() {

    _chdir("res");

    system("run.bat");

    return 0;
}