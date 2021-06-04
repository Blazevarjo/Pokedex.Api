# Pokedex.Api [![Demo live](https://img.shields.io/badge/demo-live-green)](https://mim-pokedex-api.herokuapp.com/) [![GitHub license](https://img.shields.io/github/license/Blazevarjo/Pokedex.Api)](https://github.com/Blazevarjo/Pokedex.Api/blob/master/LICENSE)


[Pokedex.Api](https://github.com/Blazevarjo/Pokedex.Api) is a REST Api that was built to serve data for [Pokedex](https://github.com/MKamil99/Pokedex) to reduce the amount of calls to [PokeApi](https://pokeapi.co/). This app has only one endpoint which shares the list of pokemons with basic info to easily display cards of each pokemon. The data is periodically updated once a day with data fetched from [PokeApi](https://pokeapi.co/). It is deployed on [heroku](https://mim-pokedex-api.herokuapp.com/).

# Table of contents
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Status](#status)
- [License](#license)

# Technologies

- Python 3.9.5
- Django REST framework 3.12.4
- Django celery beat 2.2.0
- Celery 5.0.5
- PostgreSQL latest (13.3)
- Redis latest (6.2.3)
- Gunicorn 20.1.0

[Here](requirements.txt) you can check all dependencies.




## Installation
### Prerequisites

Docker is required to run the app locally.

### Setup

1. Create .env file in the root directory with the config of environment variables. [Here](.env-example) you can check the example of the configuration.
2. Build and run the docker container.
```bash
docker-compose up
```
App is now available at http://127.0.0.1:8000/.

## Usage
1. Root endpoint: http://127.0.0.1:8000/ <br/>
<img src="https://user-images.githubusercontent.com/46849151/120811752-9bfa7180-c54c-11eb-8931-355fd6a385af.png" width=600/> <br/>

2. Pokemons endpoint: http://127.0.0.1:8000/pokemons <br/>
<img src="https://user-images.githubusercontent.com/46849151/120811806-ae74ab00-c54c-11eb-88d6-f2785cc33f46.png" width=600/> <br/>

## Status

Currently, the app is considered as finished and there are no plans to do any updates on it.

## License

[MIT](LICENSE)
