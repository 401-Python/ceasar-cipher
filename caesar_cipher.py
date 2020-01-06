
from english_words import word_list
def encrypt(key, text):
    '''
    Encrypts incoming string using the key passed in
    Text is converted to upper case to avoid any case issues
    Text should only include alphabet so we store candidates as
    a string of a through z
    Iterate through each letter, and generate decrypt key
    by taking the index of the letter + the key and dividing it by the
    length of the candidates
    Lastly we run it through the helper validate_letter, which checks
    if the character is in candidates and returns either the letter at the
    new_key idx, or the character inputted if it isn't a valid letter
    '''
    text = text.upper()
    candidates = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in text:
        new_key = (candidates.find(letter) + key) % len(candidates)
        result = result + validate_letter(new_key, letter)

    return result

def decrypt(key, text):
    '''
    Decrypts an encrpyted message from a given key, if the incorrect 
    key is used 3 times, an exception is raised
    In a real implementation, I'd have attempts be tied to some sort of
    user class, this is just a proof of concept
    '''
    attempts = 0

    text = text.upper()
    candidates = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    if attempts == 3:
      raise Exception('Too many invalid attempts')

    for letter in text:
        new_key = (candidates.find(letter) - key) % len(candidates)
        result = result + validate_letter(new_key, letter)
    if result in word_list:
      return result
    else:
      attempts +=1
      return 'Invalid Key, try again'
  
def validate_letter(new_key, letter):
    candidates = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in candidates:
        return candidates[new_key]
    else:
        return letter

