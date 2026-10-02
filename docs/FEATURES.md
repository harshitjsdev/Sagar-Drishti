# Features and Implementation Status

This page distinguishes the capabilities described in project materials
from features that need verification or further work.

## Interactive ocean explorer

The browser-based explorer is the primary visual learning interface.
Project materials identify Three.js for 3D visualization and Leaflet for
map interaction. Described controls include region selection, depth,
time and variable controls, as well as Argo float profiles.

Available variables, geographic ranges and time periods depend on the
connected dataset and current implementation.

## Ocean observations

The backend includes an INCOIS ERDDAP / Argo retrieval workflow. The
project documents retrieval, cleaning and compact JSON output for the
frontend. Data may be unavailable for some region/time selections or
contain missing measurements.

## Model information

Copernicus Marine sampling is integrated at relevant Argo
locations/times to support model-observation comparison. Availability
depends on credentials where required, provider coverage, connectivity
and successful processing.

Model output is not a direct observation and should be labelled
accordingly.

## Guided learning

The described existing education layer includes guided lessons, lesson
navigation/progress, quizzes and explanations. Confirm the precise
lesson inventory and persistence behaviour from the current source.

## Ocean Tutor

The backend tutor endpoint can use Gemini when configured; project
materials also describe a demo fallback. English/Hindi interaction is
described. AI quality and availability depend on configuration and
provider conditions. The tutor supports learning and does not replace
teachers or authoritative science sources.

## Browser-based access

The frontend is served through the Flask application in the documented
implementation. Browser and device capabilities may affect 3D
performance and speech-related features.

## Reliability

The implementation plan recommends bounded requests, timeouts, caching,
clear failure states, explicit fallback labels and returning available
observation data if optional model sampling fails. Verify each behaviour
against current code before describing it as fully implemented.

## Planned or requiring verification

The project documents identify curriculum mapping, teacher activity
packs, adaptive difficulty, AI-generated assessments, weak-topic
analytics, additional languages, large-scale analytics and wider school
deployment as future work or further-development areas.

## Release verification checklist

-   [ ] Explorer loads in supported browsers.
-   [ ] Map, region, depth, time and variable controls work.
-   [ ] Argo retrieval works for supported requests.
-   [ ] Copernicus sampling works where access and coverage exist.
-   [ ] Partial/failure/fallback states are clear.
-   [ ] Lessons and quizzes navigate correctly.
-   [ ] Tutor works with valid configuration and handles failure safely.
-   [ ] English/Hindi interactions are reviewed.
-   [ ] Observation, model and fallback content are distinguishable.
