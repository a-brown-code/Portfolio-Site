#!/bin/sh
git fetch && git reset origin/main --hard
sudo docker compose -f docker-compose.prod.yml down
sudo docker compose -f docker-compose.prod.yml up -d --build
