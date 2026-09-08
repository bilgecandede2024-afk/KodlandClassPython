i=0
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "BRAINROT": "Saçma sapan içeriklere verilen isim",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH": "Onaylamamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek/sinirlenmek"
            "RANDOM ATMAK": "Türklerin sohbetlerde komik bir şeye gülerken rastgele şeyler yazması"
            "SIGMA": "Havalı"
            "OSMANTUŞ": "Armut piş ağzıma düş atasozünü temel alan ve bir aralar ünlü olmuş baldi karakterinin düşen armutlarla halay çektiği bir meme"
            "67": "2024 civarları çıkmış ve bir basketbol maçı sırasındaki 6-7 skorunu bağıran birkaç çocuktan çıkmış ve hızla yükselmiş bir meme"
            }

while i <= 5:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Aranan kelime bulunamadı ama eminim yakında bulunabilir olacaktır")
        i += 1