1. Najpierw zbudowałam obraz i kontener Zadania 1
Użyłam takie polecenia:
	```bash
	docker build -t zadanie .
	docker run -p 5000:5000 zadanie   
2. Następnie skonfigurowałam sekrety, które służą do uwierzytelniania w zewnętrznych serwisach:
   DOCKERHUB_USERNAME – login do konta Docker Hub
   DOCKERHUB_TOKEN – token wygenerowany w ustawieniach Docker Hub
   GICR_USERNAME – nazwa użytkownika dla GitHub Container Registry
   GICR_TOKEN – token dostępu do GitHub Container Registry
   
3. Na początku projektu utworzono lokalne repozytorium Git za pomocą polecenia:
 ```bash
      git init
   ```
   Następnie dodano zdalne repozytorium i dodanie wszystkich plików
   ```bash
      git remote add origin https://github.com/qxzcr/zadanie.git
      git add .
   ```
   Zatwierdziłam zmiany:
     ```bash
      git commit -m "initial commit"
   ```
   Na końcu zmiany zostały wypchnięte
     ```bash
      git branch -M main
      git push -u origin main
```

5. Do pipeline’a dodano skanowanie obrazu za pomocą Trivy, które wykrywa krytyczne i wysokie podatności (CVE) w systemie i bibliotekach.
```bash
 - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.IMAGE_NAME }}:latest
          format: 'table'
          exit-code: '1'
          ignore-unfixed: true
          vuln-type: 'os,library'
          severity: 'CRITICAL,HIGH'
```
   
   6. Tagowanie obrazów zostało wykonane w następujący sposób:
  - **`ghcr.io/qxzcr/zadanie:latest`**  
  Główny obraz multiarch (dla platform linux/amd64 oraz linux/arm64), zbudowany i opublikowany w GitHub Container Registry.

- **`docker.io/yaxiiw/cache:buildcache`**  
  Warstwa cache używana przez Docker Buildx do przyspieszenia kolejnych buildów. Przechowywana na Docker Hub.

- **`ghcr.io/qxzcr/zadanie:df82d5dc...`**  
  Pozwala jednoznacznie powiązać obraz z wersją kodu źródłowego, z której został zbudowany.

  7. Linki: 

   GitHub Container Registry: https://github.com/users/qxzcr/packages/container/package/zadanie
Tag latest umożliwia szybkie aktualizuwanie najnowszej wersji aplikacji, natomiast tag oparty na commit-sha pozwala  jednoznaczne zidentyfikowanie wersji kodu źródłowego, z którego obraz został zbudowany. Dodatkowo wykorzystanie buildcache znacznie przyspiesza kolejne budowy oraz ograniczając zużycie zasobów.

 - **`docker image tag `**- https://docs.docker.com/reference/cli/docker/image/tag/
 - **`Working with the Container registry `**- https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry

![photo_2025-06-01_19-31-31](https://github.com/user-attachments/assets/803ef6a9-accb-44ab-bf67-96993887636f)


   
  
