# API Documentation

## Accuracy note

The supplied project materials confirm a Flask backend and API endpoints
for data retrieval and Ocean Tutor, but do not provide a complete
verified route inventory or exact schemas. This page intentionally
avoids inventing route names or payload fields. Complete it by
inspecting current Flask route decorators and frontend API calls.

## Backend responsibilities

-   Retrieve INCOIS/Argo observations.
-   Sample Copernicus model information at relevant observation
    positions/times where available.
-   Prepare compact data for the frontend.
-   Handle Ocean Tutor requests, with Gemini when configured and a demo
    fallback described.
-   Serve the frontend application.

## Route inventory template

  ------------------------------------------------------------------------------------
  Method         Actual route   Purpose               Dependency        Verified
  -------------- -------------- --------------------- ----------------- --------------
  To inspect     Extract from   Argo/observation      INCOIS/ERDDAP     No
                 Flask source   retrieval             availability      

  To inspect     Extract from   Model                 Copernicus        No
                 Flask source   sampling/comparison   access/coverage   

  To inspect     Extract from   Ocean Tutor           Gemini            No
                 Flask source                         configuration     

  To inspect     Extract from   Health/status, if     Deployment        No
                 source         present                                 
  ------------------------------------------------------------------------------------

## For every route, document

-   HTTP method and exact path
-   Purpose
-   Required/optional query and body fields
-   Types, bounds and defaults
-   Actual response schema and synthetic example
-   Status codes and error format
-   External services called
-   Timeout, request-size and rate limits
-   Partial success and fallback behaviour
-   Data source and timestamp meaning

## Validation

Implementation guidance identifies invalid coordinates, dates, missing
fields, depth limits, malformed JSON, empty provider responses, missing
measurements and large responses as cases that should return clear
errors.

Do not return stack traces, provider secrets or internal configuration
to the browser.

## How to verify API contracts

1.  Inspect Flask route decorators in `Server.py` or the current entry
    point.
2.  Search frontend source for `fetch`, `XMLHttpRequest` and API base
    URLs.
3.  Match each frontend call to its backend route.
4.  Test valid and invalid requests locally.
5.  Record actual status codes and response bodies.
6.  Update this file whenever the API changes.
