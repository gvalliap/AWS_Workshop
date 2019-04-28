# Build image
sudo docker build --tag=hello_hkn_image .

# Check image
sudo docker image ls

# Make container with image
sudo docker run --name hello_hkn_container -p 4000:80 hello_hkn_image

# Check container in browser
Type "http://localhost:4000" in browser

# Stop container
CTRL-C

# Find stopped container 
sudo docker container ls -a

# Remove container
sudo docker container rm hello_hkn_container

# Check removed container
sudo docker container ls -a
