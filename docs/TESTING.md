# Testing and Quality Assurance

Testing must cover software behaviour and the educational experience. A
successful response is not enough if the learner receives confusing or
scientifically misleading information.

## Test matrix

  -----------------------------------------------------------------------
  Area                                Checks
  ----------------------------------- -----------------------------------
  API validation                      Invalid coordinates/dates, missing
                                      fields, depth limits, malformed
                                      JSON

  Argo pipeline                       Empty region, unavailable source,
                                      malformed rows, missing
                                      measurements, large response

  Model pipeline                      Missing credentials, no coverage,
                                      network failure, interpolation
                                      failure, successful sample

  Frontend states                     Loading, success, partial success,
                                      failure, fallback and stale-data
                                      messaging

  Explorer                            Depth, time, variable, region
                                      presets, custom bounds and map
                                      interaction

  Learning                            Lesson progress, quiz navigation,
                                      answer explanations and persistence
                                      if implemented

  Tutor                               English/Hindi, timeout, backend
                                      failure, fallback and context

  Browser/device                      Desktop, small screens, touch and
                                      supported speech features

  Scientific review                   Units, labels, provenance, depth
                                      ordering, QC interpretation and
                                      comparison context
  -----------------------------------------------------------------------

## Data quality checks

-   Validate coordinates, date/time range and depth.
-   Test areas with and without coverage.
-   Preserve missing-value semantics.
-   Verify units and timestamps.
-   Preserve source labels and metadata.
-   Ensure model values are not presented as direct observations.
-   Test partial success when a provider fails.
-   Bound processing time and response size.

## Tutor quality checks

Test configured Gemini, missing/invalid credentials, provider
timeout/quota errors, empty/oversized input, English/Hindi clarity,
fallback labels and secret redaction. Review answers for age
appropriateness and scientific accuracy.

## Usability checks

With suitable school/guardian consent, test whether learners can open a
lesson, identify the visualization, change supported controls, interpret
a simple profile, distinguish observation from model, ask a question and
complete a quiz.

## Pilot evaluation

The project materials do not report validated field-study outcomes. A
future pilot may compare pre/post concept questions, data
interpretation, engagement, teacher feedback and delayed recall. Report
sample size, context, duration, assessment method and limitations. Do
not infer broad causal impact from a small demonstration.

## Release criteria

Core flows work; secrets are protected; failure states are
understandable; source/unit labels are reviewed; and target
browsers/devices have been tested.
