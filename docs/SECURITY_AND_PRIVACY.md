# Security and Privacy

This document is implementation guidance, not evidence of a completed
formal security audit or legal compliance review.

## Credentials

-   Keep Gemini and Copernicus credentials on the server.
-   Use hosting secret management in production.
-   Never commit `.env`, tokens, passwords or API keys.
-   Use placeholders in examples.
-   Rotate exposed credentials.
-   Avoid logging secrets.

## Input and API protection

Validate geographic coordinates, bounding boxes, date/time ranges, depth
limits, variables, JSON structure and tutor input. Consider request-size
limits, timeouts, rate limiting, appropriate CORS restrictions and abuse
protection for AI calls based on the actual architecture.

Use HTTPS for public traffic and keep dependencies reviewed and updated.

## Learner privacy

Before a school pilot, determine whether accounts exist, what
prompts/progress/quiz responses are stored, why personal data is needed,
who can access it, retention periods, deletion handling and whether
school or guardian consent is required.

Collect only what is necessary. Prefer aggregate or anonymized analytics
where appropriate. Do not claim compliance without documented review.

## Responsible AI

Identify AI-assisted explanations, avoid treating output as
authoritative, review English/Hindi quality, avoid sending unnecessary
personal information to providers and label demo/fallback content
clearly.

## Scientific integrity

Keep observations, model outputs and fallback/demo values distinct.
Preserve provenance and avoid presenting illustrative data as live
measurements.

## Incident response

If a key is exposed, revoke or rotate it promptly, inspect relevant
logs/repository history, remove it from active code and document
remediation. Follow appropriate school and legal processes if learner
data may be involved.
