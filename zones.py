# ─────────────────────────────────────────────────────────────────
# CAPE TOWN ZONING DATA
# Source: City of Cape Town Zoning Scheme Regulations (November 2012)
# Part of the Policy-Driven Land Use Management System
#
# Notes:
# - Floor Factor = equivalent of FAR (Floor Area Ratio)
# - Height is measured above base level
# - Building lines are minimum setbacks
# - Coverage where not specified is determined by site development plan
# ─────────────────────────────────────────────────────────────────

CAPE_TOWN_ZONES = {

    # ─────────────────────────────────────────────
    # SINGLE RESIDENTIAL ZONES
    # ─────────────────────────────────────────────

    "SR1": {
        "name": "Single Residential Zone 1",
        "subtype": "Conventional Housing",
        "category": "Residential",
        "primary_uses": ["Dwelling house", "Private road", "Additional use rights"],
        "consent_uses": ["Second dwelling", "Place of worship", "Home occupation", "Guest house", "Institution"],
        "floor_factor": 1.0,
        "coverage": "Refer to section 5.1.2(a) - varies by erf size",
        "coverage_numeric": None,
        "height_wallplate": 9.0,
        "height_roof": 11.0,
        "street_setback": "1.0m-6.0m (varies by erf size)",
        "common_boundary_setback": "0.0m-3.0m (varies by erf size)",
        "notes": "Primary single residential zone. Street setback and coverage vary based on erf size. For erven <=200m2, street setback is 1.0m. For erven >2000m2, street setback is 6.0m.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 5"
    },

    "SR2": {
        "name": "Single Residential Zone 2",
        "subtype": "Incremental Housing",
        "category": "Residential",
        "primary_uses": ["Dwelling house", "Second dwelling", "Private road"],
        "consent_uses": ["Home occupation", "Utility services", "Place of worship", "Institution"],
        "floor_factor": 1.0,
        "coverage": "Refer to section 5.2.2(a)",
        "coverage_numeric": None,
        "height_wallplate": 8.0,
        "height_roof": 10.0,
        "street_setback": "1.0m minimum",
        "common_boundary_setback": "0.0m",
        "notes": "Incremental housing zone typically applied to subsidised housing areas. Lower setback requirements to allow for incremental building over time.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 5"
    },

    # ─────────────────────────────────────────────
    # GENERAL RESIDENTIAL ZONES
    # ─────────────────────────────────────────────

    "GR1": {
        "name": "General Residential Zone 1",
        "subtype": "Group Housing",
        "category": "Residential",
        "primary_uses": ["Dwelling house", "Group housing", "Private road", "Open space"],
        "consent_uses": ["Utility services", "Home child care", "Rooftop base telecommunication station"],
        "floor_factor": None,
        "density": "35 dwelling units per hectare",
        "coverage": "Refer to section 6.1.2(b)",
        "coverage_numeric": None,
        "height_wallplate": 8.0,
        "height_roof": 10.0,
        "street_setback": "5.0m (external public street) | 0.0m (internal road)",
        "common_boundary_setback": "3.0m external | 0.0m internal",
        "notes": "Group housing zone with density control of 35 du/ha. Site development plan required.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 6"
    },

    "GR2": {
        "name": "General Residential Zone 2",
        "subtype": "Low Density Residential",
        "category": "Residential",
        "primary_uses": ["Dwelling house", "Second dwelling", "Group housing", "Boarding house", "Flats"],
        "consent_uses": ["Place of instruction", "Place of worship", "Institution", "Hospital", "Shop", "Hotel"],
        "floor_factor": 0.5,
        "density": "25 dwelling units per hectare",
        "coverage": "Refer to section 6.2.2",
        "coverage_numeric": None,
        "height_wallplate": 8.0,
        "height_roof": 10.0,
        "street_setback": "5.0m",
        "common_boundary_setback": "3.0m",
        "notes": "Low density general residential zone. Suitable for group housing, flats and boarding houses at low density.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 6"
    },

    "GR3": {
        "name": "General Residential Zone 3",
        "subtype": "Medium Density Residential",
        "category": "Residential",
        "primary_uses": ["Dwelling house", "Second dwelling", "Group housing", "Boarding house", "Flats"],
        "consent_uses": ["Place of instruction", "Place of worship", "Institution", "Hospital", "Shop", "Hotel", "Conference facility"],
        "floor_factor": 1.0,
        "density": "60 dwelling units per hectare",
        "coverage": "Refer to section 6.3.2",
        "coverage_numeric": None,
        "height_wallplate": 11.0,
        "height_roof": 13.0,
        "street_setback": "5.0m",
        "common_boundary_setback": "3.0m",
        "notes": "Medium density residential zone. Suitable for medium-rise apartment buildings and boarding houses.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 6"
    },

    "GR4": {
        "name": "General Residential Zone 4",
        "subtype": "Medium-High Density Residential",
        "category": "Residential",
        "primary_uses": ["Dwelling house", "Flats", "Boarding house", "Group housing"],
        "consent_uses": ["Place of instruction", "Institution", "Hospital", "Shop", "Hotel", "Conference facility"],
        "floor_factor": 1.5,
        "density": "100 dwelling units per hectare",
        "coverage": "Refer to section 6.4.2",
        "coverage_numeric": None,
        "height_wallplate": 14.0,
        "height_roof": 16.0,
        "street_setback": "5.0m",
        "common_boundary_setback": "3.0m",
        "notes": "Medium-high density residential zone for multi-storey apartment buildings.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 6"
    },

    "GR5": {
        "name": "General Residential Zone 5",
        "subtype": "High Density Residential",
        "category": "Residential",
        "primary_uses": ["Flats", "Boarding house", "Group housing"],
        "consent_uses": ["Institution", "Hospital", "Shop", "Hotel", "Conference facility"],
        "floor_factor": 2.0,
        "density": "200 dwelling units per hectare",
        "coverage": "Refer to section 6.5.2",
        "coverage_numeric": None,
        "height_wallplate": 17.0,
        "height_roof": 20.0,
        "street_setback": "5.0m",
        "common_boundary_setback": "3.0m",
        "notes": "High density residential zone for high-rise apartment buildings.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 6"
    },

    "GR6": {
        "name": "General Residential Zone 6",
        "subtype": "Very High Density Residential",
        "category": "Residential",
        "primary_uses": ["Flats", "Boarding house"],
        "consent_uses": ["Institution", "Hospital", "Shop", "Hotel", "Conference facility"],
        "floor_factor": 3.0,
        "density": "No restriction",
        "coverage": "Refer to section 6.6.2",
        "coverage_numeric": None,
        "height_wallplate": 20.0,
        "height_roof": 23.0,
        "street_setback": "5.0m",
        "common_boundary_setback": "3.0m",
        "notes": "Very high density residential zone for tall apartment towers in high-density urban areas.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 6"
    },

    # ─────────────────────────────────────────────
    # COMMUNITY ZONES
    # ─────────────────────────────────────────────

    "CO1": {
        "name": "Community Zone 1",
        "subtype": "Local",
        "category": "Community",
        "primary_uses": ["Place of instruction", "Place of worship", "Clinic", "Open space"],
        "consent_uses": ["Institution", "Hospital", "Place of assembly", "Cemetery"],
        "floor_factor": 0.8,
        "coverage": "60%",
        "coverage_numeric": 60.0,
        "height_wallplate": None,
        "height_roof": 12.0,
        "street_setback": "5.0m",
        "common_boundary_setback": "5.0m",
        "notes": "Local community facilities zone for schools, clinics and places of worship serving local neighbourhoods.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 7"
    },

    "CO2": {
        "name": "Community Zone 2",
        "subtype": "Regional",
        "category": "Community",
        "primary_uses": ["Institution", "Hospital", "Place of instruction", "Place of worship", "Place of assembly"],
        "consent_uses": ["Boarding house", "Conference facility", "Cemetery", "Crematorium"],
        "floor_factor": 2.0,
        "coverage": "60%",
        "coverage_numeric": 60.0,
        "height_wallplate": None,
        "height_roof": 18.0,
        "street_setback": "5.0m",
        "common_boundary_setback": "5.0m",
        "notes": "Regional community facilities zone for hospitals, universities and large-scale civic institutions.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 7"
    },

    # ─────────────────────────────────────────────
    # LOCAL BUSINESS ZONES
    # ─────────────────────────────────────────────

    "LB1": {
        "name": "Local Business Zone 1",
        "subtype": "Intermediate Business",
        "category": "Business",
        "primary_uses": ["Office", "Dwelling house", "Boarding house", "Flats"],
        "consent_uses": ["Place of instruction", "Place of worship", "Shop", "Guest house", "Service trade", "Informal trading"],
        "floor_factor": 1.0,
        "coverage": "Refer to section 8.1.2(a) - varies by erf size",
        "coverage_numeric": None,
        "height_wallplate": 9.0,
        "height_roof": 11.0,
        "street_setback": "1.0m-3.5m (varies by erf size)",
        "common_boundary_setback": "0.0m-3.0m (varies by erf size)",
        "notes": "Intermediate business zone for small offices and mixed residential-commercial uses.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 8"
    },

    "LB2": {
        "name": "Local Business Zone 2",
        "subtype": "General Local Business",
        "category": "Business",
        "primary_uses": ["Business premises", "Office", "Shop", "Service trade", "Flats"],
        "consent_uses": ["Place of assembly", "Place of entertainment", "Hotel", "Informal trading", "Motor repair garage"],
        "floor_factor": 1.0,
        "coverage": "Refer to section 8.2.2(a)",
        "coverage_numeric": None,
        "height_wallplate": 9.0,
        "height_roof": 11.0,
        "street_setback": "0.0m",
        "common_boundary_setback": "0.0m",
        "notes": "General local business zone for neighbourhood commercial centres and local retail.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 8"
    },

    # ─────────────────────────────────────────────
    # GENERAL BUSINESS ZONES
    # ─────────────────────────────────────────────

    "GB1": {
        "name": "General Business Zone 1",
        "subtype": "General Business",
        "category": "Business",
        "primary_uses": ["Business premises", "Dwelling house", "Flats", "Place of assembly", "Hotel", "Service trade"],
        "consent_uses": ["Adult shop", "Motor repair garage", "Warehouse", "Transport use", "Service station"],
        "floor_factor": 1.5,
        "coverage": "100%",
        "coverage_numeric": 100.0,
        "height_wallplate": None,
        "height_roof": 15.0,
        "street_setback": "0.0m up to 10m height | 4.5m above 10m",
        "common_boundary_setback": "0.0m up to 10m height | 4.5m above 10m",
        "notes": "Low-intensity general business zone. 100% site coverage permitted. Used for low-rise commercial areas.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 9"
    },

    "GB2": {
        "name": "General Business Zone 2",
        "subtype": "General Business",
        "category": "Business",
        "primary_uses": ["Business premises", "Flats", "Place of assembly", "Hotel", "Service trade"],
        "consent_uses": ["Adult shop", "Motor repair garage", "Warehouse", "Transport use"],
        "floor_factor": 2.0,
        "coverage": "100%",
        "coverage_numeric": 100.0,
        "height_wallplate": None,
        "height_roof": 15.0,
        "street_setback": "0.0m up to 10m height | 4.5m above 10m",
        "common_boundary_setback": "0.0m up to 10m height | 4.5m above 10m",
        "notes": "Medium-intensity general business zone with higher floor factor than GB1.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 9"
    },

    "GB3": {
        "name": "General Business Zone 3",
        "subtype": "General Business",
        "category": "Business",
        "primary_uses": ["Business premises", "Flats", "Place of assembly", "Hotel", "Conference facility"],
        "consent_uses": ["Adult shop", "Motor repair garage", "Warehouse", "Transport use"],
        "floor_factor": 2.0,
        "coverage": "100%",
        "coverage_numeric": 100.0,
        "height_wallplate": None,
        "height_roof": 25.0,
        "street_setback": "0.0m up to 10m height | 4.5m above 10m",
        "common_boundary_setback": "0.0m up to 10m height | 4.5m above 10m",
        "notes": "General business zone allowing greater height than GB2. Suitable for mid-rise mixed-use commercial buildings.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 9"
    },

    "GB4": {
        "name": "General Business Zone 4",
        "subtype": "General Business",
        "category": "Business",
        "primary_uses": ["Business premises", "Flats", "Hotel", "Conference facility", "Place of entertainment"],
        "consent_uses": ["Adult shop", "Warehouse", "Transport use", "Helicopter landing pad"],
        "floor_factor": 3.0,
        "coverage": "100%",
        "coverage_numeric": 100.0,
        "height_wallplate": None,
        "height_roof": 25.0,
        "street_setback": "0.0m up to 10m height | 4.5m above 10m",
        "common_boundary_setback": "0.0m up to 10m height | 4.5m above 10m",
        "notes": "Higher intensity general business zone. Suitable for commercial towers and high-density mixed-use development.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 9"
    },

    "GB5": {
        "name": "General Business Zone 5",
        "subtype": "General Business",
        "category": "Business",
        "primary_uses": ["Business premises", "Flats", "Hotel", "Conference facility"],
        "consent_uses": ["Warehouse", "Transport use", "Helicopter landing pad"],
        "floor_factor": 4.0,
        "coverage": "100%",
        "coverage_numeric": 100.0,
        "height_wallplate": None,
        "height_roof": 25.0,
        "street_setback": "0.0m",
        "common_boundary_setback": "0.0m",
        "notes": "High intensity general business zone. No setback restrictions. Suitable for major commercial developments.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 9"
    },

    "GB6": {
        "name": "General Business Zone 6",
        "subtype": "General Business",
        "category": "Business",
        "primary_uses": ["Business premises", "Flats", "Hotel", "Conference facility"],
        "consent_uses": ["Warehouse", "Transport use", "Helicopter landing pad"],
        "floor_factor": 6.0,
        "coverage": "100%",
        "coverage_numeric": 100.0,
        "height_wallplate": None,
        "height_roof": 38.0,
        "street_setback": "0.0m up to 25m | half of (height - 25m) above 25m",
        "common_boundary_setback": "0.0m up to 25m | half of (height - 25m) above 25m",
        "notes": "Very high intensity general business zone for major commercial nodes and city centre development.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 9"
    },

    "GB7": {
        "name": "General Business Zone 7",
        "subtype": "General Business",
        "category": "Business",
        "primary_uses": ["Business premises", "Flats", "Hotel", "Conference facility"],
        "consent_uses": ["Warehouse", "Transport use", "Helicopter landing pad"],
        "floor_factor": 12.0,
        "coverage": "100%",
        "coverage_numeric": 100.0,
        "height_wallplate": None,
        "height_roof": 60.0,
        "street_setback": "0.0m up to 25m | half of (height - 25m) above 25m",
        "common_boundary_setback": "0.0m up to 25m | half of (height - 25m) above 25m",
        "notes": "Maximum intensity general business zone for Cape Town CBD high-rise development. Highest floor factor in the scheme.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 9"
    },

    # ─────────────────────────────────────────────
    # INDUSTRIAL ZONES
    # ─────────────────────────────────────────────

    "GI1": {
        "name": "General Industry Zone 1",
        "subtype": "General Industry",
        "category": "Industrial",
        "primary_uses": ["Industry", "Restaurant", "Service station", "Motor repair garage", "Warehouse", "Transport use"],
        "consent_uses": ["Abattoir", "Place of worship", "Shop", "Office", "Place of entertainment", "Container site"],
        "floor_factor": 1.5,
        "coverage": "75%",
        "coverage_numeric": 75.0,
        "height_wallplate": None,
        "height_roof": 18.0,
        "street_setback": "5.0m",
        "common_boundary_setback": "3.0m",
        "notes": "General industrial zone for manufacturing, warehousing and logistics. Environmental and hazardous substance controls apply.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 10"
    },

    "GI2": {
        "name": "General Industry Zone 2",
        "subtype": "High Intensity Industry",
        "category": "Industrial",
        "primary_uses": ["Industry", "Warehouse", "Transport use", "Agricultural industry"],
        "consent_uses": ["Abattoir", "Container site", "Aqua-culture", "Wind turbine infrastructure"],
        "floor_factor": 4.0,
        "coverage": "75%",
        "coverage_numeric": 75.0,
        "height_wallplate": None,
        "height_roof": 18.0,
        "street_setback": "5.0m",
        "common_boundary_setback": "3.0m",
        "notes": "High intensity industrial zone with no height restriction for manufacturing buildings.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 10"
    },

    # ─────────────────────────────────────────────
    # UTILITY AND TRANSPORT ZONES
    # ─────────────────────────────────────────────

    "UT": {
        "name": "Utility Zone",
        "subtype": "Utility Services",
        "category": "Utility",
        "primary_uses": ["Utility service", "Authority use", "Rooftop base telecommunication station"],
        "consent_uses": ["Cemetery", "Informal trading", "Funeral parlour", "Airport", "Wind turbine infrastructure"],
        "floor_factor": None,
        "coverage": "As determined by site development plan",
        "coverage_numeric": None,
        "height_wallplate": None,
        "height_roof": None,
        "street_setback": "As determined by site development plan",
        "common_boundary_setback": "As determined by site development plan",
        "notes": "Utility zone for infrastructure and municipal services. All development parameters determined by site development plan.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 11"
    },

    "TR1": {
        "name": "Transport Zone 1",
        "subtype": "Transport Use",
        "category": "Transport",
        "primary_uses": ["Transport use", "Multiple parking garage", "Utility service", "Warehouse", "Container site"],
        "consent_uses": ["Business premises", "Flats", "Place of assembly", "Hotel", "Service station", "Airport"],
        "floor_factor": 2.0,
        "coverage": "75%",
        "coverage_numeric": 75.0,
        "height_wallplate": None,
        "height_roof": 18.0,
        "street_setback": "0.0m",
        "common_boundary_setback": "3.0m",
        "notes": "Transport zone for roads, rail, airports and transport infrastructure.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 11"
    },

    # ─────────────────────────────────────────────
    # OPEN SPACE ZONES
    # ─────────────────────────────────────────────

    "OS1": {
        "name": "Open Space Zone 1",
        "subtype": "Environmental Conservation",
        "category": "Open Space",
        "primary_uses": ["Environmental conservation use"],
        "consent_uses": ["Harvesting of natural resources", "Environmental facilities", "Tourist accommodation", "Utility service"],
        "floor_factor": None,
        "coverage": "As determined by site development plan",
        "coverage_numeric": None,
        "height_wallplate": None,
        "height_roof": None,
        "street_setback": "As determined by site development plan",
        "common_boundary_setback": "As determined by site development plan",
        "notes": "Environmental conservation zone. Development is severely restricted. Only minor ancillary structures permitted.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 12"
    },

    "OS2": {
        "name": "Open Space Zone 2",
        "subtype": "Public Open Space",
        "category": "Open Space",
        "primary_uses": ["Public open space", "Environmental conservation use"],
        "consent_uses": ["Environmental facilities", "Tourist facilities", "Utility service", "Cemetery", "Urban agriculture"],
        "floor_factor": None,
        "coverage": "As determined by site development plan",
        "coverage_numeric": None,
        "height_wallplate": None,
        "height_roof": None,
        "street_setback": "As determined by site development plan",
        "common_boundary_setback": "As determined by site development plan",
        "notes": "Public open space zone for parks and public amenity. Development strictly limited to ancillary facilities.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 12"
    },

    "OS3": {
        "name": "Open Space Zone 3",
        "subtype": "Special Open Space",
        "category": "Open Space",
        "primary_uses": ["Open space", "Private road", "Environmental conservation use"],
        "consent_uses": ["Environmental facilities", "Tourist facilities", "Sport and recreation"],
        "floor_factor": None,
        "coverage": "As determined by site development plan",
        "coverage_numeric": None,
        "height_wallplate": None,
        "height_roof": None,
        "street_setback": "As determined by site development plan",
        "common_boundary_setback": "As determined by site development plan",
        "notes": "Special open space zone for private recreational facilities and sport grounds.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 12"
    },

    # ─────────────────────────────────────────────
    # AGRICULTURAL ZONE
    # ─────────────────────────────────────────────

    "AG": {
        "name": "Agricultural Zone",
        "subtype": "Agriculture",
        "category": "Agricultural",
        "primary_uses": ["Agriculture", "Intensive horticulture", "Dwelling house", "Riding stables", "Environmental conservation use"],
        "consent_uses": ["Additional dwelling units", "Guest house", "Hotel", "Tourist accommodation", "Mine", "Farm shop", "Agricultural industry"],
        "floor_factor": None,
        "max_floor_space": "1500m2 for all dwelling units | 100m2 for farm shop",
        "coverage": "Refer to section 13.1.2(a)",
        "coverage_numeric": None,
        "height_wallplate": 9.0,
        "height_roof": 11.0,
        "street_setback": ">20ha: 30.0m | <=20ha: 15.0m",
        "common_boundary_setback": ">20ha: 30.0m | <=20ha: 15.0m",
        "notes": "Agricultural zone for farming and related uses. Subdivision and development strictly controlled. Maximum 1500m2 floor space for all dwelling units. Rezoning required for non-agricultural use.",
        "source": "City of Cape Town Zoning Scheme Regulations, November 2012, Chapter 13"
    },
}


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def get_zone(zone_code):
    """Return zone data for a given zone code. Returns None if not found."""
    return CAPE_TOWN_ZONES.get(zone_code.upper())


def list_zones():
    """Return a list of all zone codes and names."""
    return [
        {"code": code, "name": data["name"], "category": data["category"]}
        for code, data in CAPE_TOWN_ZONES.items()
    ]


def get_zones_by_category(category):
    """Return all zones in a given category (e.g. 'Residential', 'Business')."""
    return {
        code: data
        for code, data in CAPE_TOWN_ZONES.items()
        if data["category"].lower() == category.lower()
    }


def calculate_max_floor_space(zone_code, erf_size_m2):
    """
    Calculate estimated maximum floor space given a zone code and erf size.
    Returns None if the zone does not have a floor factor.
    """
    zone = get_zone(zone_code)
    if not zone:
        return None, "Zone not found"
    if not zone.get("floor_factor"):
        return None, "This zone does not use a floor factor - refer to site development plan"
    max_floor_space = zone["floor_factor"] * erf_size_m2
    return max_floor_space, f"{erf_size_m2}m2 x {zone['floor_factor']} (floor factor) = {max_floor_space}m2"


# ─────────────────────────────────────────────
# QUICK TEST
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("CAPE TOWN ZONING DATA — Quick Test")
    print("Source: City of Cape Town Zoning Scheme, November 2012")
    print("=" * 60)

    print(f"\n{len(CAPE_TOWN_ZONES)} zones loaded:\n")
    for z in list_zones():
        print(f"  {z['code']:<6} | {z['category']:<15} | {z['name']}")

    print("\n" + "=" * 60)
    print("Zone Lookup: GB4")
    print("=" * 60)
    zone = get_zone("GB4")
    if zone:
        print(f"Name:           {zone['name']}")
        print(f"Floor Factor:   {zone['floor_factor']}")
        print(f"Coverage:       {zone['coverage']}")
        print(f"Max Height:     {zone['height_roof']}m")
        print(f"Street Setback: {zone['street_setback']}")

    print("\n" + "=" * 60)
    print("Floor Space Calculation: GB4, 1000m2 erf")
    print("=" * 60)
    result, formula = calculate_max_floor_space("GB4", 1000)
    print(f"Max Floor Space: {result}m2")
    print(f"Formula: {formula}")

    print("\n" + "=" * 60)
    print("Business Zones Only")
    print("=" * 60)
    business = get_zones_by_category("Business")
    for code, data in business.items():
        ff = data.get('floor_factor', 'N/A')
        h = data.get('height_roof', 'N/A')
        print(f"  {code:<6} | Floor Factor: {ff:<6} | Max Height: {h}m")