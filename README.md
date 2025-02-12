## Project: HumanScanRepository API Sample Client

### Description
This project provides a simple Python API client to interact with the HumanScanRepository API. The client supports authentication, model retrieval, and file downloads with progress tracking.

### Documentation
You can find the full documentation at https://api.humanscanrepository.com/ with sample code and live testing.
 
### How to get access
To access the API , you will need credentials.json file which is provided by the owner of HumanScanRepository. Currently, this is done per user cases. To request access, please email to support@humanscanrepository.com.

### Repository Structure
```bash
API-Sample/
│── src/
│   ├── api_client.py      # Contains all API functions
│   ├── credentials.json   # Stores user credentials (this will be provided)
│   ├── main.py            # Entry point for the script
│── .gitignore             # Ignore unnecessary files
│── README.md              # Documentation for usage
│── requirements.txt       # Dependencies (requests, tqdm, etc.)
│── LICENSE                # Open-source license (MIT)
│── setup.py               # If needed for packaging
```

### **Installation**
1. Clone the repository:
   ```sh
   git clone https://github.com/ivoyovchev/hsr-api-public.git
   cd hsr-api-public
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### **Usage**
Run the script to authenticate and interact with the API:
```sh
python src/main.py
```

### **API Functions Overview**
- **Login/Register**: Authenticate and store access tokens.
- **Retrieve Models**: Fetch a list of available 3D models.
- **Download Files**: Download and extract model files with progress tracking.
