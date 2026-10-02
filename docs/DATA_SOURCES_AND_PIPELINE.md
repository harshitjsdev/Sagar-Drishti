# Data Sources and Processing Pipeline

## Purpose

SagarDrishti uses ocean observations and model information to support
interactive learning. Provider availability, dataset coverage, access
rules and network conditions can affect results.

## INCOIS / Argo observations

Project materials describe an INCOIS ERDDAP-based Argo retrieval
workflow. Argo profiling floats collect ocean measurements, and the
platform uses available profiles as real observations for exploration.

The documented workflow includes requesting data for a selected region
and time window, retrieving records, cleaning/preparing the result and
producing compact JSON for frontend use. Coverage is not uniform; some
requests may return no matching records or incomplete measurements.

## Copernicus Marine model information

The project includes Copernicus Marine sampling at relevant Argo
locations/times to support comparison. This is conditional on provider
access, data coverage, connectivity and processing success.

-   **Observation:** measurement collected by an observing system.
-   **Model output:** value produced by a numerical model.
-   **Comparison:** examining how model information corresponds to
    observations; the two are not interchangeable.

## Conceptual pipeline

``` mermaid
flowchart LR
    A[User region and time] --> B[Validate request]
    B --> C[Retrieve Argo observations]
    C --> D[Clean and structure records]
    D --> E{Model sampling enabled?}
    E -- Yes --> F[Sample Copernicus]
    E -- No --> G[Observation-only result]
    F --> H[Build available comparison context]
    G --> I[Prepare response]
    H --> I
    I --> J[JSON to browser]
    J --> K[Visualization]
```

This diagram is conceptual. Confirm actual functions and ordering in the
current source.

## Bounded Copernicus preparation example

A supplied script description references a local temperature subset
with: - Dataset ID: `cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i` -
Variable: `thetao` - Longitude: 45 to 105 - Latitude: -5 to 22 - Depth:
0 to 1000 m - Required start and end dates - Default output:
`data/copernicus/temperature.nc`

This is a local-demo preparation example, not a guarantee that every
deployed request uses those exact settings. The described script writes
outside the web app static tree. Credentials are supplied through
Copernicus Marine CLI configuration or environment as configured.

## Data handling principles

-   Validate coordinates, date ranges, depth limits and requested
    variables.
-   Handle empty results and provider failures clearly.
-   Preserve units, timestamps, coordinates and metadata where
    available.
-   Distinguish missing values from valid zero measurements.
-   Label observations, model values, cached data and fallback/demo
    content.
-   Do not silently substitute illustrative values for live
    measurements.
-   Bound request size and processing time.

## Failure scenarios

External timeout/outage, missing credentials, coverage gaps, empty
observations, malformed records, missing measurements, interpolation
failure and oversized responses may affect a request. Where possible,
return valid observation data independently and show a clear model
warning if optional sampling fails.

## Source files

Supplied materials refer to `Fetch_incois_argo.py`,
`Capernicus_model.py` (spelling as supplied), `Server.py`,
`explorer.html` and `index.html`. Confirm exact paths and capitalization
in the repository.
