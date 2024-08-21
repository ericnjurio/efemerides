# efemerides

## What is it?

This project is sample api code.

## Installation

### Prerequisites

In order to run this container, you'll need [docker installed](https://docs.docker.com/get-started/get-docker/), and [docker-compose](https://github.com/docker/compose) installed.

### Start the services

```bash
docker-compose up
```

## Usage

Do a GET to `/ephemerides?day=<YYYY-MM-DD>`

#### Sample

##### GET

```bash
pipenv run http --form GET http://127.0.0.1:8000/efemerides/?day=2020-12-15
```

##### Response

```json
{
    "hoy": "On 1874-12-15; Se funda la colonia galesa de Gaiman a orillas del río Chubut. ...",
    "mes": {
        "1": "On 1961-12-01; Nace el músico Lito Vitale\n\n\n...",
        "2": "On 1817-12-02; Nace el poeta José Mármol.\n\n\n...",
        "..": "....",
        "..": "....",
        "..": "....",
        "29": "On 1869-12-29; Se crea el Observatorio Astronómico de Córdoba\n\n\n...",
        "30": "On 1882-12-30; Nace el oncólogo Ángel Roffo, ...",
        "31": "On 1969-12-31; Finaliza el vigor de los pesos moneda nacional, ..."
    }
}
```

### Swagger

Edit `efemerides_api/settings.py` to enable debug mode (`DEBUG=True`)

Re-build and up services

```bash
docker-compose up --build
```

And look at [/swagger](http://localhost:8000/swagger/)

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
