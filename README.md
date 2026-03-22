# Cape Town Zoning API

A REST API that serves structured zoning data for the City of Cape Town, sourced directly from the **City of Cape Town Zoning Scheme Regulations (November 2012)**.

Built by [Regulo Systems](https://github.com/REF-HUE/regulo-mvp) — zoning intelligence for South African property professionals.

---

## What It Does

South African municipal zoning data is buried in lengthy PDF documents that are difficult to navigate. This API extracts and structures that data so developers, architects, and property professionals can query it programmatically.

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info and available endpoints |
| GET | `/zones` | List all 27 zone codes and names |
| GET | `/zones/<zone_code>` | Full details for a specific zone |
| GET | `/zones/category/<category>` | Filter zones by category |
| GET | `/calculate?zone=<code>&erf_size=<m2>` | Calculate maximum buildable floor space |

---

## Example Requests

**Get all zones:**
```
GET /zones
```

**Get details for General Business Zone 4:**
```
GET /zones/GB4
```

**Calculate maximum floor space for a 1000m2 erf in GB4:**
```
GET /calculate?zone=GB4&erf_size=1000
```

**Example response:**
```json
{
  "zone_code": "GB4",
  "zone_name": "General Business Zone 4",
  "erf_size_m2": 1000.0,
  "floor_factor": 3.0,
  "max_floor_space_m2": 3000.0,
  "formula": "1000m2 x 3.0 (floor factor) = 3000m2",
  "coverage": "100%",
  "max_height_m": 25.0
}
```

---

## Zone Categories

- Residential (SR1, SR2, GR1–GR6)
- Business (LB1, LB2, GB1–GB7)
- Industrial (GI1, GI2)
- Community (CO1, CO2)
- Open Space (OS1, OS2, OS3)
- Agricultural (AG)
- Utility (UT)
- Transport (TR1)

---

## Data Source

All zoning parameters are sourced from:

> City of Cape Town Zoning Scheme Regulations, November 2012
> A Component of the Policy-Driven Land Use Management System

**Disclaimer:** This API is for preliminary guidance only. Always verify zoning parameters with the City of Cape Town before making development decisions.

---

## Running Locally

```bash
git clone https://github.com/REF-HUE/-capetown-zoning-api.git
cd -capetown-zoning-api
pip install flask
python api.py
```

API runs on `http://127.0.0.1:5000`

---

## Part of Regulo Systems

This API is part of the broader **Regulo Systems** project — a zoning intelligence platform for South African property professionals.

- Main product: [regulo-mvp](https://github.com/REF-HUE/regulo-mvp)
- Live demo: [regulo-mvp.onrender.com](https://regulo-mvp.onrender.com)