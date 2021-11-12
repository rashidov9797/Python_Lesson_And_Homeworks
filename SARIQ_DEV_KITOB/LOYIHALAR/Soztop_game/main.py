import  random
from uzwords import words

from pywebio.input import  input
from pywebio.output import put_text,popup



  
def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
      word = random.choice(words)
    return word.upper()

  # print(get_word())



def display(user_letters,word):
    display_letter = " "

    for letter in word:
      if letter in user_letters:
        display_letter +=letter
      else:
          display_letter += "-"  
    return display_letter    


  # harf = "АВЖД"
  # word = "АВЖИДА"

  # print(display(harf,word))



def play():
  word = get_word()
  word_letters = set(word)
  user_letters= ' '

  put_text(f"Men {len(word)} xonali so'z o'yladim, topa olasizmi ? ")


  while word_letters:
    put_text(display(user_letters,word))

    if user_letters:
      print(f"Shu vaqtgacha kiritilgan xarflaringiz : --->>> {user_letters}")
      letter = input("Xarf kiriting :").upper()
    if letter in user_letters:
        put_text("Bu xarfni avval kiritgansiz")  
        continue

    elif letter in word:
        word_letters.remove(letter)

        put_text(f"{letter} xarfi to'g'ri kiritildi!")
    else:
      put_text("Bunday xarf mavjud emas")
    user_letters += letter

    popup(f"Tabriklayman {word} so'zini {len(user_letters)} ta urinishdayoq topdingiz")







