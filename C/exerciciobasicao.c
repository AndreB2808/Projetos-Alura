#include <stdio.h>

int main() {
    printf("Ola linguagem C!\n");
    int x, y;
    printf("Indique o valor de x: ");
    scanf("%d", &x);
    printf("Indique o valor de y: ");
    scanf("%d", &y);
    int mult = x * y;
    printf("O resultado da multiplicacao de %d com %d e %d\n", x, y, mult);
}