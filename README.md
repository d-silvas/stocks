- Start (`-d` for detached):
```
docker-compose up
```

- Stop:
```
docker-compose down
```

- Log into python container
```
docker-compose run --rm app bash
```

https://stackoverflow.com/questions/33715499/what-is-the-difference-between-docker-compose-up-and-docker-compose-start

- Log in to database within container
```
docker-compose run --rm db bash
psql --host=database --username=root --dbname=stocks
```
