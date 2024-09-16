# Bruk en Node.js base image
FROM node:14

# Sett arbeidskatalogen inne i Docker-konteineren
WORKDIR /usr/src/app

# Kopier package.json og installer avhengigheter
COPY package*.json ./
RUN npm install

# Kopier resten av applikasjonen
COPY . .

# Eksponer port hvis nødvendig
EXPOSE 8080

# Kjør applikasjonen
CMD ["node", "phevcore.js"]
