import random
from math import fabs

POPULATION_SIZE = 500
MUTATION_RATE = 0.15 # egy paraméter 8% eséllyel mutálódik

def random_egyed(n):
    """pl.: (1,5,3,1,5,7,5,3) n = 8 esetén"""
    egyed = [i for i in range(1, n + 1)] # [1,2,3,4,5,6,7,8]
    random.shuffle(egyed)
    return egyed


def fitness(egyed):
    """Optimális: 0, minél nagyobb annál rosszabb"""
    penalty_counter = (len(egyed) - len(set(egyed))) * 2 # oszlopok ütését nézzük
    # Nézzük az átlókat 
    for i in range(len(egyed)):
        for j in range(i+1, len(egyed)):
            if fabs(i-j) == fabs(egyed[i] - egyed[j]):
                penalty_counter += 1
    return penalty_counter

def keresztezés(szülő1, szülő2):
    k = random.randint(1, len(szülő1) - 2)
    return szülő1[:k] + szülő2[k:]

def mutáció(egyed, n):
    új_egyed = egyed[:]
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    új_egyed[i] = egyed[j]
    új_egyed[j] = egyed[i]
    return új_egyed
            
def kiválasztás(populáció, k = 5):
    egyedek = random.choices(populáció, k = k)
    return min(egyedek, key=fitness)

def legjobb(populáció):
    return min(populáció, key=fitness)

def genetikus(n = 8):
    populáció = [random_egyed(n) for i in range(POPULATION_SIZE)]
    generáció = 1
    while True:
        best = legjobb(populáció)
        print(f"{generáció}. generáció: {best}, rátermettség: {fitness(best)}")
        
        if fitness(best) == 0:
            print("Megoldás megtalálva!")
            print(f"n = {n}")
            print(best)
            break
        
        új_populáció = [best]
        while len(új_populáció) != POPULATION_SIZE:
            egyed = keresztezés(kiválasztás(populáció), kiválasztás(populáció))
            egyed = mutáció(egyed, n)
            új_populáció.append(egyed)
        populáció = új_populáció[:]
        generáció += 1

genetikus(20)    
#n = 4
#while True:
#    genetikus(n)
#    n += 1
    