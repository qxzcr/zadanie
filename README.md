1. Naijpierw zbudowałam obraz i kontener Zadania 1
   Użyałam takie polecenia:
   docker build -t zadanie .
   docker run -p 5000:5000 zadanie
2. Następnie skonfigurowałam sekrety, które służą do uwierzytelniania w zewnętrznych serwisach:
   DOCKERHUB_USERNAME – login do konta Docker Hub
   DOCKERHUB_TOKEN – token wygenerowany w ustawieniach Docker Hub
   GICR_USERNAME – nazwa użytkownika dla GitHub Container Registry
   GICR_TOKEN – token dostępu do GitHub Container Registry
3. Incjializowałam repozytorium Git:
    Użyłam git init, aby zainicjować nowe repozytorium
   aby dodać zdalne repozytorium Użyto komendy git remote add origin
   
![Без імені](https://github.com/user-attachments/assets/a7a6736d-fd55-49ea-b55f-fbf12151829b)
