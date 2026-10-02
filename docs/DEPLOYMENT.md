# Deployment

## Overview

The supplied implementation plan describes a Flask web service that
reads the hosting `PORT`, binds to `0.0.0.0` and disables debug mode by
default. The team-provided hosted application URL is:

https://sagar-drishti-production-4cd6.up.railway.app

The current Railway project settings and logs were not available for
this documentation; verify them in the repository and hosting dashboard.

## Deployment layers

  -----------------------------------------------------------------------
  Layer                               Consideration
  ----------------------------------- -----------------------------------
  Flask app                           Run behind a production WSGI server

  Frontend                            Serve HTML, JS, CSS and required
                                      assets through configured
                                      static/application layer

  Secrets                             Store Gemini/Copernicus credentials
                                      in host secrets

  Port/host                           Respect platform port and bind
                                      interface

  Logs                                Keep diagnostic server logs without
                                      secrets

  Cache                               Cache repeated bounded requests
                                      where appropriate and permitted

  Monitoring                          Track latency, API errors, model
                                      failures and tutor failures
  -----------------------------------------------------------------------

## Pre-deployment checklist

-   [ ] Confirm application entry point and start command.
-   [ ] Confirm Python runtime and dependency file.
-   [ ] Use a production WSGI server.
-   [ ] Disable debug mode.
-   [ ] Respect platform port and host binding.
-   [ ] Configure credentials in hosting secrets.
-   [ ] Verify frontend/static asset paths.
-   [ ] Set timeouts, input bounds and response limits.
-   [ ] Test external provider failure states.
-   [ ] Test tutor behaviour without Gemini.
-   [ ] Check logs for secrets and personal data.
-   [ ] Test on desktop and smaller screens.
-   [ ] Record release commit and rollback process.

## External dependencies

Live observations, Copernicus sampling and Gemini responses depend on
external providers. Distinguish application availability from optional
provider availability. An external service failure should be surfaced
clearly rather than represented as a successful live retrieval.

## Monitoring

Where available, track startup/restarts, request latency, validation
errors, observation failures, Copernicus failures, tutor timeouts and
partial/fallback states. Avoid retaining unnecessary learner prompts or
personal information.

## Recovery

Keep code under version control and deployment configuration separate
from secrets. For a failed release, redeploy a previously tested commit
using the host's supported recovery process, then verify core user
flows.

[Open the hosted
application](https://sagar-drishti-production-4cd6.up.railway.app)
