import random
import time,datetime
import json
import os



f = open('data.json',)
data = json.load(f)
f.close()

n = 0



# filtrare i dati doppi in una lista e ritornare una lista con file univoci
#doppelte Daten in einer Liste filtern und eine Liste mit eindeutigen Dateien zurückgeben
#filter duplicate data in a list and return a list with unique files
def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

# take data from a database and return it in a list 
# Daten aus einer Datenbank entnehmen und in einer Liste zurückgeben 
def aggiungi_a_beri(num_cose):
    #'numeri unici' is like an id for each object in the database. so that two identical sentences are not returned to the list.
    global numer_unici
    n = 0
    for i in data["lista_di_cose_lavoro"]:
        n = n + 1
    cc = []
    nn = []
    for i in range(num_cose):
        c = random.randint(1,n)
        cc.append(data["lista_di_cose_lavoro"][f'Task_{c}'])
        nn.append(c)
    unici = uniq(cc)
    numer_unici = uniq(nn)
    # return finito a tuple of two list at position 0 the sentence and at position 1 the id number of the sentence
    # finito ist ein Tupel aus zwei Listen, an Position 0 der Satz und an Position 1 die ID-Nummer des Satzes
    finito = unici,numer_unici
    return finito
'''
per passare il giusto argomento a betribliche tätigkeiten serve l'id creato da aggiungi a beri 
cosi questa funzione prende una lista con i ids e ne sceglie una a random e la passa alla key 
dell database json e il valore viene passato a betriblichen tätigkeiten

um das richtige Argument an betribliche tätigkeiten zu übergeben, benötigen diese Funktion die erstellte id
von add_to_beri 
diese Funktion nimmt also eine Liste mit IDs und wählt eine zufällig aus und übergibt sie an den Key
der json-Datenbank,und der Wert wird an betriblichen tätigkeiten übergeben

to pass the right argument to betribliche tätigkeiten you need the id created by add_to_beri (list at position 1)
so this function takes a list with ids and chooses a random number in the list and passes it to the json
database key and the value is passed to betriblichen tätigkeiten
'''
def tema_beri(lista_numeri):
    x = random.choice(lista_numeri)
    return data["tema_scolastico"][f'tema_{x}']
    

# just test to see if everithing is going well ahahah
#print(data['tema_scolastico']['tema_1'])
#x = aggiungi_a_beri(4)
#print(x[0])
#b = tema_beri(x[1])
#print(b)


