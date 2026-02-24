#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

printf("\n         ___________________        \n");
printf("         | _______________ |        \n");
printf("         | |             | |        \n");
printf("         | |  BEM VINDO  | |        \n");
printf("         | | AO JOGO DE  | |        \n");
printf("         | | ADIVINHACAO | |        \n");
printf("         | |_____________| |        \n");
printf("         |_________________|        \n");
printf("             _[_______]_            \n");
printf("         ___[___________]___        \n");
printf("        |         [_____] []|       \n");
printf("        |         [_____] []|       \n");
printf("        L___________________J       \n");
printf("\n");

    int seed = time(0);
    srand(seed);
    int number = rand();

    int secret = number % 100;
    int chute;
    int attempts = 1;
    double pontos = 1000;
    int acertou = 0;

    int nivel;
    printf("\nEscolha o nivel de dificuldade:\n");
    printf("(1) Facil (2) Medio (3) Dificil\n");
    scanf("%d", &nivel);
    int atts;

    switch(nivel){
        case 1:
            printf("Nivel facil selecionado.\n");
            atts = 15;
            break;
        case 2:
            printf("Nivel medio selecionado.\n");
            atts = 10;
            break;
        case 3:
            printf("Nivel dificil selecionado.\n");
            atts = 5;
            break;
        default:
            printf("Nivel invalido! Usando nivel facil por padrao.\n");
            atts = 15;
            break;
    }

    for (int i = 1; i <= atts; i++) {

    printf("\nIndique o seu palpite: ");
    scanf("%d", &chute);

    if (chute < 0) {
        printf("Voce nao pode chutar numeros negativos!\n");
        continue;
    }

    acertou = (chute == secret);
    int maior = chute > secret;

    if (acertou) {
         break;
    } 
    else if (maior) {
        printf("Seu chute foi maior que o numero secreto.\n");
    } 
    else {
        printf("Seu chute foi menor que o numero secreto.\n");
    }
    attempts++;
    double loss = abs(chute - secret) / (double)2; 
    pontos = pontos - loss;
    if (attempts > atts) {
        printf("Voce nao tem mais tentativas!\n");
    } else {
        printf("Restam %d tentativas.\n", atts - attempts + 1);        
    }
    }

    if (acertou) {
        printf("\nParabens! Voce adivinhou o numero secreto.");
        printf("\nVoce acertou em %d tentativas!", attempts);
        printf("\nPontuacao total: %.1f\n\n", pontos);
    } else {
        printf("\nFim do jogo!\n\n");
    }
}