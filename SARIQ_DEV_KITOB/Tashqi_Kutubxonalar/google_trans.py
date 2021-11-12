from googletrans import Translator

tarjimon = Translator()

matn_uz = "Men Surxondaryo viloyatida tug'ilganman"

tarjima = tarjimon.translate(matn_uz)

print(tarjima.text)