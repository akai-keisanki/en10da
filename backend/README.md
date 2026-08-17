# En10da backend

## Configuring environment:

```sh
python -m venv .venv
source ./.venv/bin/activate
```

```sh
cp .env.example .env
vi .env # edit to your data
```

## Configuring the database:

```sh
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
```

```sh
python populate_db.py
```

## Run

```
python -m flask run
```
