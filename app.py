version: '3.8'

services:
  frontend:
    image: nginx:latest
    ports:
      - "80:80"
    depends_on:
      - backend
    networks:
      - app-network
    deploy:
      replicas: 1
      
    configs:
      - source: nginx_conf
        target: /etc/nginx/nginx.conf

  backend:
    image: my-flask-backend:latest  # Replace with your backend image
    depends_on:
      - db
    environment:
      - DB_HOST=db
      - DB_USER=postgres
      - DB_PASSWORD=example
      - DB_NAME=app_db
    networks:
      - app-network
    deploy:
      replicas: 1
      

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: example
      POSTGRES_DB: app_db
    networks:
      - app-network
    volumes:
      - db_data:/var/lib/postgresql/data
    deploy:
      replicas: 1
      
          

networks:
  app-network:

volumes:
  db_data:

configs:
  nginx_conf:
    file: ./nginx.conf
