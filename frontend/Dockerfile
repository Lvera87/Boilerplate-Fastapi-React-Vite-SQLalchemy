FROM node:20.15.0-bookworm-slim as builder

WORKDIR /app

COPY package*.json ./
RUN npm install --legacy-peer-deps

COPY . ./

# Build production bundle
RUN npm run build

# Runtime stage for development (with hot reload)
FROM node:20.15.0-bookworm-slim

WORKDIR /app

COPY package*.json ./
RUN npm install --legacy-peer-deps

COPY . ./

# Copy built artifacts from builder (optional, for serving static build)
COPY --from=builder /app/dist ./dist

EXPOSE 5173

ENV VITE_API_BASE_PATH=/api
ENV VITE_API_VERSION=v1

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
