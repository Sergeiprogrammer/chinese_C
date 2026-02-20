# 🐉 Chinese_C (Dragon Empire C)

An experimental and humorous version of C that replaces standard English keywords  
with long dramatic Chinese-style phrases using the C preprocessor.

It does NOT modify the C compiler. Everything works via macros and text translation.

---

## 🚀 How It Works

There are two components:

1. `translate.py` – converts English C code ↔ Chinese-style code
2. `dragon_empire.h` – maps Chinese phrases back to real C keywords using `#define`
3. `example.c` – c code exmaple in english
4. `example_chinese.c` – c code example in chinese

The compiler only sees normal C after preprocessing.

---

## 🔄 Using the Translator

### Step 1 – Download `translate.py`

Inside the script you will find a variable:

```python
value = """
... your code here ...
"""
````

Place your C code (English or Chinese-style) inside the triple quotes.

---

### Step 2 – Run the script

Run:

```
python translate.py
```

If you don’t have Python installed, you can use an online compiler like:
[https://www.programiz.com/python-programming/online-compiler/](https://www.programiz.com/python-programming/online-compiler/)

---

### 🔁 Translation Modes

When running the script, you will be asked to type:

* `1` → English (original C) → Chinese version
* `2` → Chinese version → English (original C)

---

## 🧾 Using the Chinese C Code

1 install file dragon_empire.h and place in your work directory

2 In your C program, include:

```c
#include "dragon_empire.h"
```

Then you can write code like:

```c
我宣誓效忠伟大帝国的生产力 伟大领袖亲自降临() {
    向天下苍生昭告真理("Hello, Dragon Empire!\n");
    向伟大帝国汇报成果 0;
}
```

The preprocessor will convert it back to standard C before compilation. and it will work like a regular C code without efecting on speed of work

---

## 📂 Example

See `example.c` and `example_chinese.c` for a working sample.

---

## 🧠 Educational Purpose

This project is useful for understanding:

* How `#define` works
* What happens during preprocessing (`.i` files)
* How compilers transform source code
* That programming languages are ultimately just structured text before compilation

---

## ⚔️ Why?

IDK

---

## 📜 License
Free to use for educational and experimental purposes.
