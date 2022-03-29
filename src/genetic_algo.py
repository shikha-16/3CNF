from CNF_Creator import *
import random
import time
import numpy
import itertools
import multiprocessing
import decimal


def generatePopulation(nstates, nvar):
    #generates population of nstates with nvar in each state

    population = set()
    while len(population) < nstates:
        news = []
        for j in range(nvar):
            if random.randint(0,1) == 1:
                news.append(j+1)
            else:
                news.append(-(j+1))
        population.add(tuple(news))
    return list(population)


def geneticAlgorithm(population, sentence):
    #improved genetic algorithm function

    start = time.time()
    cnt = 0
    answer = [0,0]
    curr = [0,0]

    while True:

        new_pop = []
        size = len(population)
        f = fitnessArray(population, sentence) #fitness of all states in population
        
        i = 0
        while i in range(0,size):
            #choosing parents 
            random_index = random.choices([q for q in range(size)], weights=f, k=3)
            random_states = population[random_index[0]], population[random_index[1]], population[random_index[2]]
            x, y, z = list(random_states[0]), list(random_states[1]), list(random_states[2])
            
            #elitism
            if f[random_index[0]] == max(f):
                new_pop.append(x)
                i += 1
            if i < size and f[random_index[1]] == max(f):
                new_pop.append(y)
                i += 1
            if i < size and f[random_index[2]] == max(f):
                new_pop.append(z)
                i += 1
            
            #child
            if i < size:
                child = reproduce(x,y,z)
                if random.randint(1,100) <= 4: #epsilon value = 0.04
                    child = mutate(child)
                new_pop.append(child)
                i += 1

        population = new_pop
        prev = curr
        curr = best(population, sentence) #current best model

        if curr[0] == prev[0]:
            cnt += 1
        else:
            cnt = 0

        #saving best fitness model till now
        if curr[1] > answer[1]:
            answer[0] = curr[0]
            answer[1] = curr[1]
        
        if answer[1] == 100 or time.time()>=start+45.00 or cnt==1000:
            break
    
    timetaken = time.time() - start
    return answer, round(timetaken, 2)


def reproduce(state1, state2, state3):
    #returns cross between 3 states

    size = len(state1)
    c1 = random.randint(1,size-2)
    c2 = random.randint(c1+1,size-1)
    return state1[0:c1]+state2[c1:c2]+state3[c2:]


def mutate(state):
    #chooses 1 value in the state and changes it

    size = len(state)
    c = random.randint(0,size-1)
    state[c] = -1*state[c]
    return state


def fitnessArray(population, sentence):
    #returns fitness array which has fitness for all the states in population

    fitness = [0]*len(population)
    for index, state in enumerate(population):
        fitness[index] = float(percentage(state, sentence))
    return fitness


def percentage(state, sentence):
    #returns percentage of clauses that are satisfied in the 3-CNF sentence.

    total = 0
    satisfied = 0
    for clause in sentence:
        for val in clause:
            if (val < 0 and state[abs(val)-1] < 0) or (val > 0 and state[abs(val)-1] > 0):
                satisfied += 1
                break
        total += 1
    return decimal.Decimal(satisfied)/decimal.Decimal(total) * decimal.Decimal(100)

def best(population, sentence):
    #returns state in population with maximum fitness, along with corresponding max fitness.
    
    max_fitness = 0
    fittest = population[0]
    f = fitnessArray(population, sentence)
    for i in range(len(population)):
        state = population[i]
        curr = f[i]
        if curr > max_fitness:
            max_fitness = curr
            fittest = state
    return [fittest, max_fitness]


def main():
    cnfC = CNF_Creator(n=50) # n is number of symbols in the 3-CNF sentence
    # sentence = cnfC.CreateRandomSentence(m=120) # m is number of clauses in the 3-CNF sentence
    # print('Random sentence : ',sentence)

    sentence = cnfC.ReadCNFfromCSVfile()
    # print('Sentence : ',sentence)
    pop = generatePopulation(len(sentence)//2, 50)
    answer, timetaken = geneticAlgorithm(pop, sentence)

    print('\n\n')
    print('Number of clauses in CSV file : ',len(sentence))
    print('Best model :',answer[0])
    print('Fitness value of best model :',answer[1],"%")
    print('Time taken :',timetaken,'seconds')
    print('\n\n')
    
if __name__=='__main__':
    main()