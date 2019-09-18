# Koroibos Service
A small Django microservice designed to serve data about Olympic athletes and the events they participate in

## Local Setup

If you'd like to run this app locally, pull down this repo and run the following commands:

Environment Setup:
```
$ python3 -m venv env
$ source venv/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

Set up Database:
```
$ psql
$ CREATE DATABASE koroibos_development;
$ CREATE USER (any username) WITH PASSWORD (any password);
$ GRANT ALL PRIVILEGES ON DATABASE koroibos_development TO (the username you chose);
$ \q
$ export DB_NAME="koroibos_development"
$ export DB_USER="username you chose"
$ export DB_PASSWORD="password you chose"
$ python3 manage.py migrate
```

If you try to run tests and run into a database error, try running the following
```
psql
ALTER USER (the username you chose) CREATEDB;
\q
```

## Endpoint Documentation

+ [Get all Olympians](#get_olympians)
+ [Get Youngest Olympian](#youngest)
+ [Get Oldest Olympian](#oldest)
+ [Get Olympian Statistics](#stats)
+ [Get Olympic Events](#events)
+ [Get Medalists by Event](#medalists)

## <a name='get_olympians'></a>Get all Olympians

Example Request:
```
GET api/v1/olympians
```

Example Response:
```
{
    [
      {
        "name": "Maha Abdalsalam",
        "team": "Egypt",
        "age": 18,
        "sport": "Diving"
        "total_medals_won": 0
      },
      {
        "name": "Ahmad Abughaush",
        "team": "Jordan",
        "age": 20,
        "sport": "Taekwondo"
        "total_medals_won": 1
      },
      {...}
    ]
}
```

## <a name='youngest'></a>Get Youngest Olympian

Example Request:
```
GET api/v1/olympians?age=youngest
```

Example Response:
```
{
  "name": "Ana Iulia Dascl",
  "team": "Romania",
  "age": 13,
  "sport": "Swimming"
  "total_medals_won": 0
}
```

## <a name='oldest'></a>Get Oldest Olympian
Example Request:
```
GET api/v1/olympians?age=oldest
```

Example Response:
```
{
  "name": "Julie Brougham",
  "team": "New Zealand",
  "age": 62,
  "sport": "Equestrianism"
  "total_medals_won": 0
}
```
## <a name='stats'></a>Get Olympian Statistics
Example Request:
```
GET api/v1/olympian_stats
```

Example Response:
```
{
  "olympian_stats": {
    "total_competing_olympians": 3120
    "average_weight:" {
      "unit": "kg",
      "male_olympians": 75.4,
      "female_olympians": 70.2
    }
    "average_age:" 26.2
  }
}
```
## <a name='events'></a>Get Olympic Events
Example Request:
```
GET api/v1/events
```

Example Response:
```
{
    [
      {
        "sport": "Archery",
        "events": [
          "Archery Men's Individual",
          "Archery Men's Team",
          "Archery Women's Individual",
          "Archery Women's Team"
        ]
      },
      {
        "sport": "Badminton",
        "events": [
          "Badminton Men's Doubles",
          "Badminton Men's Singles",
          "Badminton Women's Doubles",
          "Badminton Women's Singles",
          "Badminton Mixed Doubles"
        ]
      },
      {...}
    ]
}
```
## <a name='medalists'></a>Get Get Medalists by Event
Example Request:
```
GET api/v1/events/:event_id/medalists
```

Example Response:
```
{
  "event": "Badminton Mixed Doubles",
  "medalists": [
      {
        "name": "Tontowi Ahmad",
        "team": "Indonesia-1",
        "age": 29,
        "medal": "Gold"
      },
      {
        "name": "Chan Peng Soon",
        "team": "Malaysia",
        "age": 28,
        "medal": "Silver"
      }
    ]
}
```
