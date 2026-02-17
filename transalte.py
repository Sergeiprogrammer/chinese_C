import re

hanzi_map = {

    # ===== Типы =====
    "我宣誓效忠伟大帝国的生产力": "int",
    "天地虚无之境": "void",
    "符文载体": "char",
    "千年不朽之力": "long",
    "凡尘短暂之力": "short",
    "灵气流转之术": "float",
    "双倍龙魂之气": "double",
    "命运之抉择": "_Bool",

    # ===== Управление потоком =====
    "倘若天命如此安排": "if",
    "否则听从宇宙安排": "else",
    "否则若命运再次转折": "else if",
    "天命之分岔": "switch",
    "若此命运降临": "case",
    "若无其他命数": "default",
    "修行仍在继续之时": "while",
    "先行动后思考": "do",
    "循环修炼之道": "for",
    "强行穿越时空": "goto",
    "继续闭关修炼": "continue",
    "强行打断因果": "break",
    "向伟大帝国汇报成果": "return",

    # ===== Объявления =====
    "静默守护之术": "static",
    "来自远方的支援": "extern",
    "顺其自然之力": "auto",
    "寄存在龙脉之中": "register",
    "不可违背的誓言": "const",
    "变化无常的命运": "volatile",
    "内在融合之法": "inline",
    "测量万物之尺度": "sizeof",
    "赐予新名之仪式": "typedef",

    # ===== Структуры =====
    "组合万象之躯": "struct",
    "阴阳合一之体": "union",
    "列举众生之名": "enum",

    # ===== main и стандарт =====
    "伟大领袖亲自降临": "main",
    "向天下苍生昭告真理": "printf",
    "聆听众生低语": "scanf",
}


reversed_map = {v: k for k, v in hanzi_map.items()}


def translate(text, selection):
    if selection == 1:
        selected_map = reversed_map
    elif selection == 2:
        selected_map = hanzi_map
    else:
        print("Selection must be 1 or 2")
        return None

    # сортируем по длине чтобы "else if" не сломался
    sorted_keys = sorted(selected_map.keys(), key=len, reverse=True)

    for key in sorted_keys:
        # границы слова чтобы не ломать переменные типа integer
        pattern = r'\b' + re.escape(key) + r'\b'
        text = re.sub(pattern, selected_map[key], text)

    return text


#Code
# #include <stdio.h>
# #define _CRT_SECURE_NO_WARNINGS

value = r"""
#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h> // Includes the standard input-output library

int main() {
  /* main() is where program execution begins */
  printf("Hello, World!\n"); // Prints the string to the screen
  return 0; // Indicates successful program termination
}

"""
#________________



selection = int(input("write 1/2: 1 - english to chinese, 2 chinese to english transaltion: "))

result = translate(value, selection)
print(result)
