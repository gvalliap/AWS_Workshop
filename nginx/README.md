# Create containers
sudo docker-compose up -d

# Check containers are up
sudo docker-compose ps

# Check containers are up in docker CLI
sudo docker container ls

# Check app in browser
Type "http://localhost:80" in browser

# Stop containers
sudo docker-compose stop

# Check containers are stopped
sudo docker-compose ps

# Remove containers
sudo docker-compose rm

# Confirm yes on removal
Type "y" and enter

# Check containers are removed
sudo docker-compose ps
sudo docker container ls -a


