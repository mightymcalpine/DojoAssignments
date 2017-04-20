# Q1
select countries.id, countries.name, language, percentage
from countries
join languages on countries.id = languages.country_id
where language = 'Slovene'
order by percentage desc;

#Q2
SELECT countries.id, countries.name AS country, COUNT(cities.name) AS number_of_cities
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY cities.country_id
ORDER BY COUNT(cities.id) DESC;

#Q3
SELECT cities.name, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico'
AND cities.population > 500000
ORDER BY population DESC;

#Q4
SELECT countries.name AS country, language, percentage
FROM countries
JOIN languages ON languages.country_id = countries.id
WHERE percentage > 89
ORDER BY percentage DESC;

#Q5
SELECT countries.name, surface_area, countries.population
FROM countries
WHERE surface_area < 501
AND population > 100000
ORDER BY countries.population ASC;

#Q6
SELECT countries.name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy'
AND capital > 200
AND life_expectancy > 75
ORDER BY life_expectancy DESC;

#Q7
SELECT countries.name, cities.name, district, cities.population
from countries
JOIN cities ON cities.country_id = countries.id
WHERE district = 'Buenos Aires'
AND cities.population > 500000;

#Q8
SELECT countries.region, COUNT(countries.name) AS number_of_countries
from countries
GROUP BY countries.region
ORDER BY COUNT(countries.id) DESC;

