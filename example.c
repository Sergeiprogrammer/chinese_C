#include <stdio.h>
#include "dragon_empire.h"

我宣誓效忠伟大帝国的生产力 伟大领袖亲自降临() {

    符文载体 op;
    双倍龙魂之气 first, second;
    向天下苍生昭告真理("Enter an operator (+, -, *, /): ");
    聆听众生低语("%c", &op);
    向天下苍生昭告真理("Enter first operand: ");
    聆听众生低语("%lf", &first);
    向天下苍生昭告真理("Enter second operand: ");
    聆听众生低语("%lf", &second);

    天命之分岔(op) {
        若此命运降临 '+':
        向天下苍生昭告真理("%.1lf + %.1lf = %.1lf", first, second, first + second);
        强行打断因果;
        若此命运降临 '-':
        向天下苍生昭告真理("%.1lf - %.1lf = %.1lf", first, second, first - second);
        强行打断因果;
        若此命运降临 '*':
        向天下苍生昭告真理("%.1lf * %.1lf = %.1lf", first, second, first * second);
        强行打断因果;
        若此命运降临 '/':
        向天下苍生昭告真理("%.1lf / %.1lf = %.1lf", first, second, first / second);
        强行打断因果;
        // operator doesn't match any 若此命运降临 constant
    若无其他命数:
        向天下苍生昭告真理("Error! operator is not correct");
    }

    向伟大帝国汇报成果 0;
}
