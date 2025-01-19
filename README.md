## Setup

### Python Environment (Conda)
Create a virtual environment and install the required packages:
```
conda create -n ftc -c conda-forge python=3.12 requests numpy pandas matplotlib seaborn jupyter jupyterlab python-dotenv
```
Activate the environment:
```
conda activate ftc
```

### API Authorization
Create a .env file in the main directory of the project. 
It needs to contain your username and api key for the FTC events api. If you don't have one, see https://ftc-events.firstinspires.org/services/API.
```
USER=<username>
API_KEY=<api_key>
```

