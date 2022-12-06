## Match_ROI

# Installation Required

1. Python,3.8.x or above
2. Flower

- Follow the steps here to install flower on linux
https://flower.readthedocs.io/en/latest/install.html

# How to use

1. Clone the repository
2. Create a virtual environment: https://www.geeksforgeeks.org/python-virtual-environment/
3. Install requirements using given command:
- 'python3 -m pip install -r requirements.txt'
4. To build the docker image:
- 'docker-compose build'
5. Once the build is successful run the docker image using following command: 
- 'docker-compose up'
6. To start the process of transcription 
- cd /match-roi
- 'python3 -m src.main'
