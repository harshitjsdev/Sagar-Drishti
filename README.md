# SagarDrishti

**SagarDrishti** is a browser-based, interactive 3D ocean visualization and learning platform. It helps users explore ocean conditions through Argo float observations and ocean-model data, inspect profiles and trajectories, compare observations with model values, and learn ocean science through guided lessons, quizzes, and an AI-powered Ocean Tutor.

## Current website features

### Interactive 3D ocean explorer
- Explore an interactive 3D representation of the ocean water column.
- View ocean variables such as **temperature** and **salinity**.
- Adjust the displayed depth and explore changes through the depth and time controls.
- Play or pause the time sequence and inspect the selected region.
- Toggle visual layers such as currents and grid overlays.
- Choose a predefined region, including the **Bay of Bengal**, **Arabian Sea**, and **Equatorial Indian Ocean**, or define a custom latitude/longitude box.
- Use the region map to select a point and reposition the current geographic bounds.

### Argo observations and ocean-model data
- Explore Argo float locations and observed vertical profiles.
- Inspect selected float details, including identifiers, cycle, position, and available metadata.
- View float trajectory information where available.
- Load available local data for the initial experience and request data for a selected region and date range through the backend.
- Request INCOIS Argo observations and, when enabled and available, corresponding Copernicus Marine model samples.
- View fallback or illustrative data when live data files or external data retrieval are unavailable. Such fallback data should not be interpreted as a live observation.

### Model–observation comparison
- Compare an Argo observation with a corresponding ocean-model value.
- Select the float/observation, variable, and depth for comparison.
- Review comparison context, data eligibility/availability, and the displayed difference or insight.
- Access data provenance from the comparison and float panels.

### Guided learning
- Follow interactive ocean-science lessons that connect explanations to the 3D explorer.
- Track lesson progress and revisit completed lessons.
- Take the built-in quiz to review concepts; answers include explanations.

### Ocean Tutor
- Ask questions about the ocean and the information shown in the explorer.
- Use the tutor's suggested questions as starting points.
- Switch between English and Hindi.
- Use voice input where supported by the browser and optionally have responses read aloud.
- The tutor can use the Gemini API through the Flask backend when configured. If the API is unavailable, the website may show built-in demo answers instead.

### Additional interface tools
- Rapid insights and contextual explanations.
- Glossary tooltips for ocean-science terms.
- Data provenance and metadata views.
- Responsive panels for smaller screens.

## Data sources

- **INCOIS / Argo:** in-situ ocean observations, including float positions and vertical profiles.
- **Copernicus Marine:** ocean-model data used for model comparison when configured and available.
- **Local JSON data:** optional/prepared data files used by the website for initial loading or fallback presentation.

Ocean data remains subject to the terms, licenses, and attribution requirements of its respective provider. Check the source metadata and provenance shown in the website before reusing data.

## Technology stack

### Frontend
- HTML5, CSS3, and JavaScript
- Three.js for browser-based 3D rendering
- Leaflet for the interactive geographic map
- CDN-hosted frontend libraries and fonts

### Backend and data processing
- Python
- Flask and Flask-CORS
- Xarray, NumPy, Pandas, Requests, and NetCDF support
- Copernicus Marine Python client
- Google Gen AI SDK for the Gemini-powered Ocean Tutor
- `python-dotenv` for loading local environment variables

## Application workflow

1. The user explores the 3D ocean view and chooses a region, date range, depth, and variable.
2. The frontend can load prepared local data and can send a live-data request to the Flask backend.
3. The backend retrieves Argo observations from the configured INCOIS/ERDDAP source.
4. If model fetching is enabled and configured, the backend obtains Copernicus Marine data corresponding to the requested region/time and available Argo cycles.
5. The frontend updates the explorer and comparison panels with the returned data. If retrieval is incomplete or unavailable, the interface may use fallback/illustrative values and display a status message.
6. The Ocean Tutor sends questions to the backend Gemini endpoint when configured; otherwise, the frontend can fall back to demo responses.

## Project structure

The exact folder layout can vary. A typical flat layout is:

```text
SagarDrishti/
├── Server.py
├── tutor_api.py
├── Fetch_incois_argo.py
├── Capernicus_model.py
├── explorer.html
├── index.html
├── requirements.txt
├── .env                 # local secrets; do not commit
├── .gitignore
└── data/                # downloaded/prepared data
```

Keep the Python modules and frontend files in the locations expected by your `Server.py`. The backend's frontend-directory resolution supports a flat layout or a sibling `frontend/` directory when that directory contains `index.html`.

## Run locally

### 1. Prepare Python

Use a supported Python installation and create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 2. Install dependencies

If the project includes `requirements.txt`:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages used by the backend:

```bash
pip install flask flask-cors python-dotenv pandas requests xarray netCDF4 numpy copernicusmarine google-genai
```

### 3. Configure environment variables

Create a local `.env` file beside `Server.py` (or in the directory from which the backend loads its environment), and add only the credentials needed for the features you intend to use:

```env
GEMINI_API_KEY=replace_with_your_key
# Optional:
GEMINI_MODEL=gemini-2.0-flash

# Add Copernicus Marine credentials only if required by your data access setup:
COPERNICUSMARINE_SERVICE_USERNAME=your_username
COPERNICUSMARINE_SERVICE_PASSWORD=your_password
```

Do not commit `.env`, paste credentials into frontend JavaScript, or share API keys in screenshots, issue trackers, or chat. Configure production secrets through your hosting provider's environment/secrets settings. If a key has been exposed, revoke it and replace it.

The Gemini key is used server-side by the Ocean Tutor. The tutor endpoint is `/api/tutor`. If Gemini is not configured or the request fails, the interface may fall back to built-in demo answers.

### 4. Start the Flask server

From the project directory:

```bash
python Server.py
```

Open the local address printed by Flask. In the supplied backend configuration, the default port is `8000`, so the site is normally available at:

```text
http://localhost:8000/
```

Use the Flask-served site for testing API-backed features. Opening the HTML directly or using a separate static development server can send relative API requests to the wrong host.

## Backend API

### `POST /api/fetch-live-data`

Requests data for a selected geographic bounding box and date range. The frontend sends fields similar to:

```json
{
  "minLat": 5,
  "maxLat": 15,
  "minLon": 80,
  "maxLon": 90,
  "start": "2025-01-01",
  "end": "2025-01-07",
  "minDepth": 0.5,
  "maxDepth": 1000,
  "includeModel": true
}
```

The endpoint returns Argo data and model data/status in JSON. Model retrieval can depend on credentials, network availability, data coverage, and the request parameters. Refer to `Server.py` and the data-fetching modules for the exact response schema and current implementation.

### `POST /api/tutor`

Accepts a question, screen context, and language, then returns a JSON answer when the Gemini request succeeds. The API key must remain on the backend; never expose it in the browser.

## Troubleshooting

- **Tutor shows demo answers:** confirm `GEMINI_API_KEY` is configured in the backend environment, restart Flask after changing `.env`, and inspect the `/api/tutor` response and Flask terminal for details.
- **Tutor request is canceled:** the frontend currently applies a request timeout. A slow response may be aborted and trigger demo fallback; also check backend logs and Gemini errors.
- **`404` for JSON data files:** verify that the requested file exists in the frontend directory being served by Flask, or use the live-data fetch workflow to generate/update it where supported.
- **Argo fetch fails:** check the data source availability, request region/date range, and backend logs.
- **Copernicus model data is unavailable:** check Copernicus Marine access/configuration, model coverage for the selected time and region, and backend logs. Argo results may still be returned when model retrieval fails.
- **API calls fail while using a static server:** open the website through Flask so relative `/api/...` requests reach the backend.

## Security

- Keep `.env`, API keys, and data-provider credentials out of source control.
- Add the following to `.gitignore` if not already present:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
data/
```

Review whether any generated data should be committed before ignoring or publishing the `data/` directory.

Team MANTHAN 
