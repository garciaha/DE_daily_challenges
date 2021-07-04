"""Summer Olympics
Analyse statistics of Olympic Games in the summer CSV file.

Create a function that returns

1. Find out the (male and female) athlete who won most medals in all the 
   Summer Olympic Games (1896-2014). 
2. Return the first 10 countries that won most medals:

Bonus:
    Use pandas to create a dataframe you can work on

SELECT Name
FROM summer.csv
WHERE Gender = gender (input)
GROUP BY Name
ORDER BY COUNT(Medal)
LIMIT RESULTS TO 1

SELECT Country
FROM summer.csv
WHERE Gender = gender
GROUP BY Name
ORDER BY COUNT(Medal)
LIMIT RESULTS TO 10

"""


def summer_olympic_medals(gender, countries=False):
    pass


if __name__ == "__main__":
    assert summer_olympic_medals('Men') == "Michael Phelps"
    assert summer_olympic_medals('Women') == "Larisa Latynina"
    assert summer_olympic_medals("Men", True) == [
        'USA', 'URS', 'GBR', 'FRA', 'ITA', 'SWE', 'GER', 'HUN', 'AUS', 'JPN']
    assert summer_olympic_medals("Women", True) == [
        'USA', 'URS', 'CHN', 'AUS', 'GER', 'GDR', 'RUS', 'NED', 'ROU', 'GBR']
    print("All cases passed!")
