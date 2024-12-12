

notas = {"W":1,"H":1/2,"Q":1/4,"E":1/8,"S":1/16,"T":1/32,"X":1/64}

compositions = []
while True:
    line = input().strip() # lee la linea y elimina espacios al inicio y final
    if line == "*":
        break
    compositions.append(line)

#print(f"Composiciones: {compositions}")


for composition in compositions:
    cant_medidas_correctas=0
    #print(f"Composicion simple {composition}")
    measures = composition.split('/') #te queda un espacio vacio por la '/' del principio y otra de la del final
    measures = [measure for measure in measures if measure] #/WW/HH/ -> 'WW', 'HH'
    for measure in measures:
        time=0
        letters = list(measure) #'WW' -> ['W', 'W']
        for letter in letters:
            if letter in notas:
                #print(f"Letra: {letter}, duracion: {notas[letter]}")
                time+= notas[letter]
        if time == 1:
            cant_medidas_correctas+=1
    print(cant_medidas_correctas)
