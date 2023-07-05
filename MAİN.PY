meme_dict={"LOL":"komik bir şeye verilen cevap",
"CRINGE":"garip ya da utandırıcı bir şey",
"ROFL":"bir şakaya karşılık cevap",
"SHEESH":"onaylamamak"
,"CREEPY":"korkunç",
"AGGRO":" agresifleşmek/sinirlenmek"}
print("hangi kelimenin anlamını öğrenmek istersin ;
LOL
CRINGE
ROFL
SHEESH
CREEPY
AGGRO")
word = word.upper
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    
