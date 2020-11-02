def rockpaperscissor(population):
    count = 0
    while population != 0:
        population = population // 2
        count = count + 1
        
    return (count)
        
print(rockpaperscissor(7800000000))

# The answer is 33