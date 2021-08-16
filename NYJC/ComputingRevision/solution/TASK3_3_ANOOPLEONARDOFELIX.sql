SELECT Temperature.temperature, Rain.total, Rain.max_daily, Rain.days, Humidity.relative
FROM Temperature
LEFT JOIN Rain
ON Temperature.year_month = Rain.year_month
LEFT JOIN Humidity
ON Temperature.year_month = Humidity.year_month
WHERE Temperature.year = "2020";