import random
import string
import math

def caesar_encrypt(word, shift):
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_word += encrypted_char
        else:
            encrypted_word += char
    return encrypted_word

def substitution_encrypt(word):
    alphabet = string.ascii_lowercase
    shuffled_alphabet = ''.join(random.sample(alphabet, len(alphabet)))
    
    substitution_map = {alphabet[i]: shuffled_alphabet[i] for i in range(len(alphabet))}
    substitution_map.update({alphabet[i].upper(): shuffled_alphabet[i].upper() for i in range(len(alphabet))})
    
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            encrypted_word += substitution_map[char]
        else:
            encrypted_word += char
    return encrypted_word, substitution_map

def reversal_encrypt(word):
    return word[::-1]

def vigenere_encrypt(word, keyword):
    encrypted_word = ""
    keyword_repeated = (keyword * (len(word) // len(keyword) + 1))[:len(word)]
    
    for i, char in enumerate(word):
        if char.isalpha():
            shift = ord(keyword_repeated[i].lower()) - ord('a')
            offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_word += encrypted_char
        else:
            encrypted_word += char
    return encrypted_word

def transposition_encrypt(word, num_rows):
    num_cols = math.ceil(len(word) / num_rows)
    padded_word = word.ljust(num_rows * num_cols)  # 填充到完整的矩形
    grid = [padded_word[i:i + num_cols] for i in range(0, len(padded_word), num_cols)]
    
    encrypted_word = ""
    for col in range(num_cols):
        for row in range(num_rows):
            if grid[row][col] != ' ':
                encrypted_word += grid[row][col]
    return encrypted_word

def binary_encrypt(word):
    encrypted_word = ''.join(format(ord(char), '08b') for char in word)
    return encrypted_word

def multi_encrypt(word, methods, shift=3, keyword="key", num_rows=3):
    encrypted_word = word
    for method in methods:
        if method == "caesar":
            encrypted_word = caesar_encrypt(encrypted_word, shift)
        elif method == "substitution":
            encrypted_word, _ = substitution_encrypt(encrypted_word)
        elif method == "reversal":
            encrypted_word = reversal_encrypt(encrypted_word)
        elif method == "vigenere":
            encrypted_word = vigenere_encrypt(encrypted_word, keyword)
        elif method == "transposition":
            encrypted_word = transposition_encrypt(encrypted_word, num_rows)
        elif method == "binary":
            encrypted_word = binary_encrypt(encrypted_word)
        else:
            print(f"Unknown encryption method: {method}")
            return None
    return encrypted_word

# 示例
word = "HelloWorld"
methods = ["caesar", "substitution", "reversal", "vigenere", "transposition", "binary"]

# 调用多重加密
encrypted_word = multi_encrypt(word, methods, shift=3, keyword="key", num_rows=3)

print("Original:", word)
print("Encrypted:", encrypted_word)
