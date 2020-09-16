FROM node:12.18.0-slim AS compile-image
COPY . ./app
WORKDIR /app
RUN npm install
RUN npm install -g @angular/cli