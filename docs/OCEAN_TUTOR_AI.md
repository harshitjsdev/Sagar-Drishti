# Ocean Tutor and AI Integration

## Overview

SagarDrishti includes an Ocean Tutor intended to help learners ask
questions about ocean-science concepts. Project materials describe a
backend tutor endpoint with Gemini integration when configured and a
demo fallback. English/Hindi interaction is described in the impact
material.

The tutor is a learning support feature, not a replacement for teachers,
scientific references, official forecasts or expert judgement.

## Conceptual flow

1.  Learner submits a question in the browser.
2.  Frontend sends the request to the tutor backend.
3.  Backend validates input and checks configuration.
4.  If configured, backend calls Gemini.
5.  Backend handles the provider response or error.
6.  Response is returned to the browser.
7.  If a demo fallback is used, it should be visibly labelled.

## Context grounding

The implementation plan proposes stronger grounding in selected float,
date, depth, variable and relevant data summaries. Treat this as planned
unless verified in the current code. Any context supplied to the tutor
should be relevant, bounded, accurately labelled as observation/model
and checked for stale or missing data.

## Reliability and errors

Possible failures include missing/invalid credentials, quota limits,
provider outage, timeout, empty input and malformed responses. Use clear
non-sensitive errors, server-side diagnostics and reasonable timeouts.
Never return stack traces or secrets to the client. Do not claim AI
success if the provider call failed.

## Educational quality

-   Use age-appropriate plain language.
-   Explain scientific terms.
-   Distinguish facts, model values and uncertainty.
-   Do not fabricate measurements or citations.
-   Encourage teacher/scientific-source verification.
-   Review English and Hindi responses.
-   Avoid using the tutor for high-stakes weather, safety or
    agricultural decisions.

## Configuration

Supplied materials mention Gemini credentials but do not establish the
exact current environment-variable name. Verify the backend source and
hosting configuration. Never commit real keys.

## Test checklist

-   [ ] Valid prompt with Gemini configured
-   [ ] Missing or invalid credential
-   [ ] Provider timeout/quota/error
-   [ ] Empty and oversized prompt
-   [ ] English and Hindi response quality
-   [ ] Demo fallback is clearly labelled
-   [ ] No secrets in client responses or logs
-   [ ] Context, if used, matches current selection
