# Configuration and Secrets

## Documented configuration

Project materials describe the following: - `PORT` is read from the
hosting environment. - Server binds to `0.0.0.0`. - Debug mode is
disabled by default. - Gemini credentials enable full tutor integration
when configured. - Copernicus Marine credentials may be supplied through
CLI configuration or environment, depending on the script.

Exact current variable names beyond `PORT` are not confirmed by the
supplied materials; inspect source before setting them.

## Configuration inventory

  -----------------------------------------------------------------------
  Setting                 Purpose                 Status
  ----------------------- ----------------------- -----------------------
  `PORT`                  Hosting platform port   Explicitly described

  Gemini credential       AI tutor access         Credential described;
                                                  exact variable name to
                                                  verify

  Copernicus              Model-data access       CLI/environment method
  authentication                                  described; exact setup
                                                  to verify

  Debug setting           Development diagnostics Debug off by default
                                                  described

  Host binding            Deployment network      `0.0.0.0` described
                          interface               
  -----------------------------------------------------------------------

## Secret management

-   Keep credentials server-side.
-   Store production keys in hosting secrets.
-   Do not hardcode keys in Python, HTML, CSS or JavaScript.
-   Ignore local secret files in Git.
-   Use placeholders in examples.
-   Rotate exposed keys.
-   Separate development and production credentials.
-   Avoid logging secrets or unnecessary learner information.

## `.env.example`

Only create this after confirming actual variable names in code. A
generic placeholder is not a working application configuration:

``` dotenv
# Replace with exact names verified from source
PORT=5000
# GEMINI_KEY=<set-locally>
# COPERNICUS_CREDENTIAL=<set-locally>
```

## Production

Use a production WSGI server, keep debug off, configure secrets in the
host dashboard, set request timeouts and bounds, and confirm logs do not
expose private information.
