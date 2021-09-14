# Ex 1
**missed**


# Ex 2
* Installera docker.
* Kör den förpreparerade  "Hello world" som test.

```bash
docker run hello-world
```

# Ex 3
* Använd bash i en docker-container för att köra en egen enkel "hello world"
```bash
docker run -t bash echo "Hello World"
```

# Ex 4
* Gör ett enkelt skript som räknar från 1 till 10 med en sekunds
  pause för varje steg
* Starta bash i en docker-container
* Kopiera scriptet till din container (lägg det t ex under /tmp)
* Kör scriptet i din container
* Observera intressanta saker kring sökvägar och att scriptet i
  containern bara finns så länge som containern finns

```bash
docker run -dt bash
> f0696245aa1d
docker cp ./numbers.sh f0696245aa1d:/tmp
docker exec -it f0696245aa1d /bin/bash
./tmp/numbers.sh
exit
```

# Ex 5
* Plocka hem Alpine att använda som bas för en egen enkel image
* Testa att köra Alpine i docker
* Skapa en Dockerfile för en image "hello" som är din egen implementation
  av ett "hej världen"
* Bygg och kör din image

Dockerfile
```docker
FROM alpine:latest
CMD [ "echo", "Hello World!" ]
```


# Ex 6
* Skapa nu en Dockerfile för en image "counter" som kör ditt räkneskript
  (det som räknar från 1 till 10) under bash
* Bygg och kör din image

Dockerfile
```docker
FROM alpine:latest

RUN apk add --no-cache bash
COPY numbers.sh numbers.sh

CMD [ "/bin/bash", "numbers.sh" ]
```
numbers.sh
```bash
#!/bin/bash

for x in {1..10}
do
    echo $x
    sleep 1
done
```
```bash
docker build -t day10 .
docker run -it day10
```