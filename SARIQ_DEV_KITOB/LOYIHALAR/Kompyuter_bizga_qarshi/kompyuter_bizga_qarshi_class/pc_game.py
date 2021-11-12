import pywebio
from pywebio.output import put_text,put_buttons
from time import sleep
import random



x=10

class Son_top_pc():
  put_text(f"1 dan {x} gacha son o'ylang \nSizga 3 doniya vaqt !!!") 

  def __init__(self,taxmin,yuqori,quyi):
    taxmin = taxmin
    yuqori = x
    quyi = 1



 


  def guess(taxmin,quyi,yuqori):
    def uchgacha_sana():

      for i in [3,2,1, "Start boshladik!"]:
        put_text(str(i)) 
      sleep(1)
    pywebio.output.clear(scope=-1)
    taxmin = random.randint(quyi,yuqori)
    put_text(f"Siz {taxmin}  sonini o'yladingiz!")

    put_buttons(['Kattaroq','Togri','Kichikroq'],onclick=[katta,bingo,kichik])
    pywebio.session.hold()



  def kichik(guess,yuqori,taxmin):
    yuqori = taxmin -1
    guess()  


  def katta(guess,quyi,taxmin):
    quyi = taxmin +1
    guess()


  def bingo(guess,bingo,taxmin):
    put_text('Men yutdim ukam!!!')
    guess()     








