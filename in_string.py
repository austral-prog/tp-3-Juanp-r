def check_vowels():
    # Código a implementar utilizando input.
    print("ingrese un nombre:")
    txt=input()
    print(f"contiene a: {'a'in txt.lower()}")
    print(f"contiene e: {'e'in txt.lower()}")
    print(f"contiene i: {'i'in txt.lower()}")
    print(f"contiene o: {'o'in txt.lower()}")
    print(f"contiene u: {'u'in txt.lower()}")



# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
