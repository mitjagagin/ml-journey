# tutorials/step_17_syntax_errors_strings.py
"""Синтаксис строк: правильное использование кавычек и апострофов."""

# 1. Правильно: двойные кавычки снаружи, одинарные внутри
message_1: str = "I told my friend, 'Python is my favorite language!'"
print(message_1)

# 2. Правильно: одинарные кавычки снаружи, двойные внутри
message_2: str = 'The language "Python" is named after Monty Python.'
print(message_2)

# 3. Правильно: апостроф внутри двойных кавычек (частая ситуация в ML-промптах)
message_3: str = "One of Python's strengths is its diverse community."
print(message_3)

# 4. ОШИБКА: апостроф внутри одинарных кавычек закрывает строку преждевременно
# Раскомментируйте строку ниже и запустите — увидите SyntaxError:
# message_4: str = 'One of Python's strengths is its diverse community.'

# 5. Решение для сложных случаев: экранирование через обратный слэш (\)
message_5: str = 'One of Python\'s strengths is its diverse community.'
print(message_5)

# 6. В ML-промптах часто используют тройные кавычки для многострочных строк
rag_prompt: str = """
You are an AI assistant. Answer the question based on the context.
Context: "The model's accuracy is 95%."
Question: What is the model's accuracy?
"""
print(rag_prompt)