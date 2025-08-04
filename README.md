# Warehouse Proximity

A Python-based application designed to optimize warehouse selection based on proximity and other logistics factors. This tool helps businesses and developers streamline supply chain decisions by programmatically calculating the best warehouse options for given delivery locations.

## Table of Contents

- [Installation](#installation)
- [API Usage](#api-usage)
- [Deployment Details](#deployment-details)
- [Integration (Frontend to Backend)](#integration-frontend-to-backend)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MikhailAquino/warehouse-proximity.git
   cd warehouse-proximity
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## API Usage

The application exposes a RESTful API for warehouse proximity calculations.

**Base Endpoint:** `/api/v1/warehouses/proximity`

### Example Request

```http
POST https://warehouse-proximity.onrender.com
Content-Type: application/json

{
  "warehouse": [14.5995, 120.9842],
  "delivery": [14.6000, 120.9850],
  "radius": 250
}
```

### Example Response

```json
{
  "distance": 102.42,
  "within_range": true
}
```

## Deployment Details

- **Live Production Deployment:**  
  The latest version of this service is deployed and available at:  
  👉 [https://warehouse-proximity.onrender.com](https://warehouse-proximity.onrender.com)

- **Local Deployment:**  
  Run the API locally for development:
  ```bash
  python app.py
  ```
  The server will be available at `http://localhost:8000/` (default).

## Integration (Backend to Frontend)

The official frontend for this API is the [logistics-dashboard](https://github.com/MikhailAquino/logistics-dashboard), built with Laravel.

- The frontend offers an intuitive interface for users to input delivery coordinates, define search radius, and visually explore warehouse proximity on an interactive map.
- The backend (this API) is live on Render, and the frontend is configured to interact with it via the Render deployment endpoint, set in the frontend’s `.env` or relevant configuration files.
- All data exchange between frontend and backend is handled via RESTful JSON API calls, ensuring smooth and secure integration.
