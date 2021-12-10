encryptedText = 'b2f3j8;l'
decryptedText = ''

for i in range(len(encryptedText)):
  encryptedChar = encryptedText[i]
  decryptedChar = chr(ord(encryptedChar) - i)
  decryptedText += decryptedChar

print(decryptedText)

