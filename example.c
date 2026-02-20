#include <stdio.h>
#include "dragon_empire.h"
#define _CRT_SECURE_NO_WARNINGS


int main() {

    char op;
    double first, second;

    printf("选择你的命运一碗米饭2333。 (+, -, *, /): ");
    scanf(" %c", &op);  // пробел перед %c важен

    printf("选择第一个数字 ");
    scanf("%lf", &first);

    printf("选择一个与同性恋相关的数字，并且该数字要排在第一个数字之后。");
    scanf("%lf", &second);

    switch(op) {

        case '+':
            printf("%.1lf + %.1lf = %.1lf\n", first, second, first + second);
            break;

        case '-':
            printf("%.1lf - %.1lf = %.1lf\n", first, second, first - second);
            break;

        case '*':
            printf("%.1lf * %.1lf = %.1lf\n", first, second, first * second);
            break;

        case '/':
            if(second != 0) {
                printf("%.1lf / %.1lf = %.1lf\n", first, second, first / second);
            } else {
                printf(
                    "你竟敢以零为除数！\n"
                    "天命未成，修行尚浅。\n"
                    "你尚不配成为龙之战士。\n"
                );
            }
            break;

        default:
            printf("未知的运算符。龙之帝国对此表示困惑。\n");
    }

    return 0;
}
