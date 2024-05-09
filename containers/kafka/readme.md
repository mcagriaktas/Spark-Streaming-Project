## 1. CREATE STORAGE FOLDERS
for i in {1..3}; do mkdir -p data/kafka${i}; done

## 2. CREATE CONTAINER
docker-compose up --build -d

