**ДОМАШНЕЕ ЗАДАНИЕ No1**
> здесь код
>
> 
countries = ['USA', 'UK', 'Brazil', 'Germany', 'Poland', 'Canada']
capitals = ['Washington', 'London','Brazil','Berlin','Warsaw', 'Ottawa']
population = [341_918_869, 67_974_586, 217_703_610, 83_250_037, 40_164_798, 39_124_353]
for capitals, countries, population in zip(countries,capitals,population):
    print(capitals, "is the capital of", countries, 'population equal', population)
