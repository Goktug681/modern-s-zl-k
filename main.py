name_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
    "OK":"Tamam",
    "CRINGE":"garip ya da utandırıcı bir şey"}
    
    
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")    
if word in name_dict.keys():
    print(name_dict[word])
else:
    print("Bu kelimeyi biliyorsunuz")
            
