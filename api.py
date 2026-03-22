from flask import Flask, jsonify, request
from zones import get_zone, list_zones, get_zones_by_category, calculate_max_floor_space

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "api": "Cape Town Zoning API",
        "version": "1.0.0",
        "built_by": "Regulo Systems",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012",
        "disclaimer": "For preliminary guidance only. Always verify with the City of Cape Town before making development decisions.",
        "endpoints": {
            "GET /zones": "List all zones",
            "GET /zones/<zone_code>": "Get details for a specific zone (e.g. /zones/GB4)",
            "GET /zones/category/<category>": "Filter zones by category (Residential, Business, Industrial, etc.)",
            "GET /calculate?zone=<code>&erf_size=<m2>": "Calculate maximum buildable floor space"
        }
    })

@app.route('/zones')
def all_zones():
    zones = list_zones()
    return jsonify({
        "total": len(zones),
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012",
        "zones": zones
    })

@app.route('/zones/<zone_code>')
def zone_detail(zone_code):
    zone = get_zone(zone_code.upper())
    if not zone:
        return jsonify({
            "error": f"Zone '{zone_code.upper()}' not found.",
            "hint": "Use GET /zones to see all available zone codes."
        }), 404
    return jsonify({"zone_code": zone_code.upper(), **zone})

@app.route('/zones/category/<category>')
def zones_by_category(category):
    zones = get_zones_by_category(category)
    if not zones:
        return jsonify({
            "error": f"No zones found for category '{category}'.",
            "available_categories": ["Residential", "Business", "Industrial", "Community", "Open Space", "Agricultural", "Utility", "Transport"]
        }), 404
    return jsonify({
        "category": category,
        "total": len(zones),
        "zones": [
            {"zone_code": code, "name": data["name"], "floor_factor": data.get("floor_factor"), "coverage": data.get("coverage"), "height_roof": data.get("height_roof")}
            for code, data in zones.items()
        ]
    })

@app.route('/calculate')
def calculate():
    zone_code = request.args.get('zone', '').strip().upper()
    erf_size_raw = request.args.get('erf_size', '').strip()

    if not zone_code:
        return jsonify({"error": "Missing parameter: zone", "example": "/calculate?zone=GB4&erf_size=1000"}), 400
    if not erf_size_raw:
        return jsonify({"error": "Missing parameter: erf_size", "example": "/calculate?zone=GB4&erf_size=1000"}), 400

    try:
        erf_size = float(erf_size_raw)
        if erf_size <= 0:
            raise ValueError
    except ValueError:
        return jsonify({"error": "erf_size must be a positive number in m2."}), 400

    zone = get_zone(zone_code)
    if not zone:
        return jsonify({"error": f"Zone '{zone_code}' not found.", "hint": "Use GET /zones to see all available zone codes."}), 404

    max_floor_space, formula = calculate_max_floor_space(zone_code, erf_size)

    return jsonify({
        "zone_code": zone_code,
        "zone_name": zone["name"],
        "erf_size_m2": erf_size,
        "floor_factor": zone.get("floor_factor"),
        "max_floor_space_m2": max_floor_space,
        "formula": formula,
        "coverage": zone.get("coverage"),
        "max_height_m": zone.get("height_roof"),
        "disclaimer": "Floor factor is sourced from the City of Cape Town Zoning Scheme Regulations (November 2012). Always verify with the City of Cape Town before making development decisions."
    })

if __name__ == '__main__':
    print("=" * 60)
    print("Cape Town Zoning API — Regulo Systems")
    print("=" * 60)
    app.run(host='0.0.0.0', port=10000, debug=False)