# FastAPI MLOps Practice

A simple FastAPI application for MLOps practice with configuration management.

## Project Structure

```
practice_11022026/
├── main.py              # FastAPI application
├── config.py            # Configuration loader
├── config.yaml          # Configuration file
├── test_client.py       # Test client to call API endpoints
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── .venv/              # Python virtual environment
```

## Setup & Installation

### 1. Create Virtual Environment
```powershell
python -m venv .venv
```

### 2. Activate Virtual Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

## Running the Application

### Start the Server
```powershell
uvicorn main:app --reload
```

The server will start at: `http://127.0.0.1:8000`

### API Documentation
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **OpenAPI spec**: http://127.0.0.1:8000/openapi.json

## Available Endpoints

### GET `/`
Returns a welcome message.
```json
{"message": "Hello Keerthana"}
```

### GET `/health`
Health check endpoint.
```json
{"status": "ok"}
```

### GET `/square?x=5`
Calculates the square of a number.
```json
{"result": 25}
```

### POST `/predict`
Makes a prediction based on input feature.
Request body:
```json
{"feature": 10}
```
Response:
```json
{"prediction": 21}
```

## Testing the API

### Option 1: Using Swagger UI (Browser)
1. Go to http://127.0.0.1:8000/docs
2. Click on any endpoint
3. Click "Try it out"
4. Click "Execute"

### Option 2: Using Test Client Script
```powershell
python test_client.py
```

This tests all endpoints using the configuration from `config.yaml`.

### Option 3: Using curl
```powershell
# Health check
curl http://127.0.0.1:8000/health

# Square calculation
curl "http://127.0.0.1:8000/square?x=5"

# Prediction (POST)
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"feature": 10}'
```

### Option 4: Using PowerShell
```powershell
$body = @{feature = 10} | ConvertTo-Json
Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict" -Method POST -Body $body -ContentType "application/json" -UseBasicParsing

# Or for GET requests
Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -UseBasicParsing
```

## Configuration

All configuration is managed in `config.yaml`. You can modify:

- **Server settings**: host, port, reload mode
- **API metadata**: title, version, description
- **Endpoints**: base URL and endpoint paths

Example `config.yaml`:
```yaml
server:
  host: "127.0.0.1"
  port: 8000
  reload: true
  debug: true

api:
  title: "FastAPI MLOps Practice API"
  version: "1.0.0"
  description: "A simple FastAPI application for MLOps practice"

endpoints:
  base_url: "http://127.0.0.1:8000"
  predict_endpoint: "/predict"
  health_endpoint: "/health"
  root_endpoint: "/"
  docs_endpoint: "/docs"
```

The `test_client.py` and `main.py` use these values automatically — no hardcoding needed!

## Git Workflow

### Status
```powershell
git status
```

### Add Changes
```powershell
git add .
```

### Commit
```powershell
git commit -m "Your commit message"
```

### Push to GitHub
```powershell
git push origin main
```

### Pull Latest Changes
```powershell
git pull origin main
```

## Dependencies

Main packages:
- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **pydantic**: Data validation
- **requests**: HTTP client (for testing)
- **PyYAML**: YAML configuration parsing

See `requirements.txt` for all dependencies and versions.

## Stopping the Server

Press `Ctrl+C` in the terminal where Uvicorn is running.

## Troubleshooting

### Port 8000 Already in Use
Change the port in `config.yaml` or run:
```powershell
uvicorn main:app --port 8080
```

### Import Error: "cannot import name 'FastAPI'"
Make sure:
1. `.venv` is activated
2. You're not in a file named `fastapi.py` (use `main.py`)
3. Dependencies are installed: `pip install -r requirements.txt`

### Config.yaml Not Found
Ensure `config.yaml` is in the same directory as `main.py`.

## Next Steps

- Replace dummy prediction logic with actual ML model
- Add database integration
- Add authentication
- Add request validation and error handling
- Deploy to cloud (AWS, GCP, Azure, etc.)