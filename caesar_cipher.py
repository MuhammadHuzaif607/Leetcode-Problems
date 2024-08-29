class CaesarCipher:
    def __init__(self, shift: int = 3):
        self.shift = shift

    def encrypt_char(self, char: str) -> str:
        if char.isupper():
            return chr((ord(char) + self.shift - 65) % 26 + 65)
        elif char.islower():
            return chr((ord(char) + self.shift - 97) % 26 + 97)
        else:
            return char 

    def encrypt(self, text: str) -> str:
        encrypted_text = ''
        for char in text:
            encrypted_text += self.encrypt_char(char)
        return encrypted_text


txt = "ABC"
cipher = CaesarCipher()  
encrypted_text = cipher.encrypt(txt)
print(encrypted_text)
