# Installation and Local Setup

> This guide is a setup checklist based on the supplied project
> description. Verify actual filenames, Python version, dependencies and
> start command from the current repository before use.

## Prerequisites

-   Python version supported by the repository
-   Git
-   Modern browser
-   Project source code
-   Network access for external services
-   Optional Gemini and Copernicus credentials for full integrations

## Clone

``` bash
git clone <repository-url>
cd <repository-folder>
```

Replace placeholders with the real repository URL and folder.

## Virtual environment

``` bash
python -m venv .venv
```

Windows PowerShell:

``` powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

``` bash
source .venv/bin/activate
```

## Dependencies

If the repository includes `requirements.txt`:

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If the project uses another dependency manager, follow its checked-in
configuration. Do not guess production package versions.

## Configuration

Read `CONFIGURATION.md` and inspect the backend for exact
environment-variable names. Create a local `.env` only if the code
supports it. Never commit secrets.

## Run

Use the actual entry point in the repository. Project materials describe
a Flask application; if `Server.py` is the current entry point, a local
development command may be:

``` bash
python Server.py
```

Use only after confirming the filename and startup logic. Do not enable
debug mode in public deployment.

## Verify

-   Open the local URL printed by the server.
-   Confirm frontend assets load.
-   Check browser console and server logs.
-   Test a supported region/time selection.
-   Test lessons and quizzes.
-   Test the tutor with valid configuration.
-   Verify clear external-service failure states.
-   Confirm no credentials appear in browser files or responses.

## Troubleshooting

**Server fails to start:** verify Python runtime, dependencies, entry
point and port.\
**Tutor unavailable:** check backend configuration, credential, quota,
network and server logs.\
**Model unavailable:** check Copernicus access, coverage, requested
range and connectivity.\
**No observations:** test a region/time with known coverage and inspect
provider response.\
**Slow 3D view:** test a supported browser/device and reduce data volume
if controls allow.
