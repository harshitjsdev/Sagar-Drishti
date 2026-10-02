# System Architecture

## Overview

SagarDrishti uses a browser-client and Python web-backend design. The
frontend presents the explorer and learning interface. Flask serves the
application and coordinates requests to data services and tutor
functionality.

``` mermaid
flowchart TD
    A[Student or Teacher Browser] --> B[HTML, CSS, JavaScript UI]
    B --> C[Three.js 3D Explorer]
    B --> D[Leaflet Map]
    B --> E[Flask Backend]
    E --> F[INCOIS ERDDAP / Argo]
    E --> G[Copernicus Marine]
    E --> H[Ocean Tutor Endpoint]
    H --> I[Gemini when configured]
    F --> J[Prepared observation data]
    G --> K[Model samples when available]
    J --> L[Backend response]
    K --> L
    I --> M[Tutor response]
    L --> B
    M --> B
    B --> N[Guided Lessons and Quizzes]
```

This is a conceptual diagram based on supplied project materials, not an
automatically extracted code dependency graph.

## Frontend

Project materials identify HTML, CSS and JavaScript, with Three.js for
3D visualization and Leaflet for maps. The UI includes explorer
controls, lesson and quiz experiences, and Ocean Tutor interaction.
Frontend code should not contain provider secrets.

## Backend

The documented backend uses Python Flask and Flask-CORS. It serves the
frontend and exposes endpoints used for data retrieval and tutoring. The
supplied implementation plan describes reading the hosting `PORT`,
binding to `0.0.0.0` and disabling debug mode by default.

Exact route names, modules, validation and response schemas must be
checked in the current repository.

## Data services

**INCOIS/Argo:** observation retrieval, cleaning and compact response
preparation.\
**Copernicus Marine:** model sampling at observation positions/times
when enabled and available.\
**Gemini:** tutor generation through backend integration when
configured.

## Typical request lifecycle

1.  User opens the web application.
2.  Browser loads frontend assets.
3.  User selects a region, time, depth or variable.
4.  Frontend sends a request to the backend.
5.  Backend validates inputs and retrieves observation data.
6.  Model sampling may run where applicable.
7.  Backend returns available results and relevant status.
8.  Frontend updates the visualization and communicates partial or
    failed states.
9.  User continues with lessons, quizzes or tutor questions.

The exact ordering and response contract should be verified against
active source.

## Design considerations

-   Keep UI, data retrieval, processing and tutor concerns separable.
-   Preserve valid observation results when optional model access fails,
    where supported.
-   Clearly identify observations, model values and fallback/demo
    content.
-   Keep credentials server-side.
-   Use bounded queries, timeouts and caching.
-   Test accessibility and performance on common school devices.

## Keep architecture current

Document actual API routes, request/response schemas, provider
identifiers, processing rules, cache strategy, tutor context
construction, error codes and production start command as code evolves.
