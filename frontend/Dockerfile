# ---------- Build Stage ----------
FROM node:18-alpine AS builder
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

ARG API_URL
RUN sed -i "s|__API_URL__|${API_URL}|g" src/environments/environment.ts
RUN sed -i "s|__API_URL__|${API_URL}|g" src/environments/environment.prod.ts

# Build using production environment
RUN npm run build -- --configuration production

# ---------- Runtime Stage ----------
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist/angular-conduit /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

