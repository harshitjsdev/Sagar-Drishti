# Roadmap

## Guiding approach

Build on the existing SagarDrishti foundation rather than replacing it.
Keep the current explorer and data pipeline usable while improving
education features and reliability incrementally. The stages below are
proposed work based on the supplied implementation plan, not a claim
that all items are complete.

## Staged roadmap

  ---------------------------------------------------------------------------------
  Stage             Focus             Work                        Intended output
  ----------------- ----------------- --------------------------- -----------------
  1                 Stabilize         Test live-data flow, tutor, Stable baseline
                                      fallback, errors, browser   
                                      compatibility and           
                                      deployment                  

  2                 Classroom layer   Curriculum mapping, clearer Structured
                                      explanations, objectives,   classroom
                                      teacher notes and lesson    experience
                                      navigation                  

  3                 Guided explorer   "What am I looking at?",    Lower entry
                                      layer explanations, simpler barrier
                                      controls, seasonal slider,  
                                      data-quality language       

  4                 Contextual AI     Ground tutor in selected    More
                                      float/date/depth/variable   context-aware
                                      and relevant summaries;     tutoring
                                      curate modes                

  5                 Assessment        Concept quizzes/flashcards, Data-informed
                                      performance recording and   feedback
                                      weak-topic feedback         

  6                 Pilot and scale   Teacher/student pilot,      Evidence-based
                                      usability fixes,            deployment plan
                                      language/content expansion  
                                      and infrastructure review   
  ---------------------------------------------------------------------------------

## Near-term priorities

**Reliability:** clear external failures, partial results, timeouts,
request bounds, logging and deployment verification.\
**Learning clarity:** simple labels, units, source/time context and
educator-reviewed explanations.\
**AI quality:** verify configuration, improve contextual grounding where
implemented, review English/Hindi output and communicate limitations.

## Pilot before scaling

Begin with a small teacher-supported pilot. Select a lesson, region and
objectives; guide students through an exploration; collect feedback;
compare concept understanding before and after; and use findings to
improve controls and lesson pacing.

## Future options

Potential expansion includes NCERT/MP Board alignment, additional
regional languages, teacher resources, learning-level pathways, adaptive
quizzes, flashcards, weak-topic analytics and more datasets where
reliable access exists. Prioritize based on user feedback, feasibility,
privacy and educational review.
