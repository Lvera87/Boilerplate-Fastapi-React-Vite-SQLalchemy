# syntax=docker/dockerfile:1.7
ARG NODE_VERSION=20.18.0

FROM node:${NODE_VERSION}-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --no-audit --no-fund

FROM node:${NODE_VERSION}-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . ./
RUN npm run build

# ----- Development runtime (default for docker-compose dev) -----
FROM node:${NODE_VERSION}-alpine AS dev
WORKDIR /app
RUN addgroup -S app && adduser -S app -G app
COPY --from=deps --chown=app:app /app/node_modules ./node_modules
COPY --chown=app:app . ./
USER app
EXPOSE 5173
ENV VITE_API_BASE_PATH=/api \
    VITE_API_VERSION=v1
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# ----- Production runtime (static files via `vite preview`) -----
FROM node:${NODE_VERSION}-alpine AS prod
WORKDIR /app
RUN addgroup -S app && adduser -S app -G app
COPY --from=builder --chown=app:app /app/dist ./dist
COPY --from=builder --chown=app:app /app/package.json ./package.json
COPY --from=deps --chown=app:app /app/node_modules ./node_modules
USER app
EXPOSE 4173
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "4173"]
