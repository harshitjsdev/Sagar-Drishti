"""
Ocean-tutor endpoint for SagarDrishti, backed by the Gemini API (free tier).

The frontend (explorer.html) already POSTs to /api/tutor with
    { "question": str, "context": {...}, "lang": "en" | "hi" }
and expects JSON back as
    { "answer": str }
If this endpoint is missing or fails, the page silently falls back to its
built-in demo answers.

Hook it into your existing Flask app (server.py) with two lines:

    from tutor_api import tutor_bp
    app.register_blueprint(tutor_bp)

Environment variables (put them in .env; python-dotenv is already a dependency):
    GEMINI_API_KEY   required  -- get one free at https://aistudio.google.com/apikey
    GEMINI_MODEL     optional, defaults to gemini-2.0-flash (free-tier eligible)
"""
import os

from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from google import genai
from google.genai import types
from google.genai import errors as genai_errors

load_dotenv()

tutor_bp = Blueprint("tutor", __name__)

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
MAX_QUESTION_CHARS = 500

# Created lazily so the app still starts (and the frontend falls back to demo
# answers) when no API key is configured.
_client = None


def _get_client():
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    return _client


VARIABLES = {
    "en": ["temperature", "salinity"],
    "hi": ["तापमान", "लवणता"],
}

SYSTEM_PROMPT = """You are the ocean tutor inside SagarDrishti, an educational 3D explorer of \
Argo float data from INCOIS. Your students are school and college learners, many in Madhya \
Pradesh, far from the coast.

Rules:
- Answer in {language}. Keep answers short: 2 to 4 sentences, plain words, no jargon without a quick explanation.
- Ground answers in the "screen context" below when the question is about what the student is looking at.
- Topics you cover: Argo floats, temperature, salinity, the thermocline, ocean currents, \
the Indian monsoon, and comparing a computer model with real measurements.
- Never invent specific measurements. If the context does not contain a value, say you cannot see it on screen.
- If asked about something unrelated to the ocean or this tool, politely steer back to ocean science.

Screen context (JSON-derived):
{context}
"""


def _describe_context(ctx: dict, lang: str) -> str:
    ctx = ctx if isinstance(ctx, dict) else {}
    names = VARIABLES.get(lang, VARIABLES["en"])
    var_idx = ctx.get("variable")
    variable = names[var_idx] if isinstance(var_idx, int) and 0 <= var_idx < len(names) else "unknown"
    lines = [
        f"- Region: {ctx.get('region') or 'unknown'}",
        f"- Variable shown: {variable}",
        f"- Depth slice: {ctx.get('depthText') or 'unknown'}",
        f"- Selected float: {ctx.get('floatId') or 'none'}",
        f"- Current tab: {str(ctx.get('view') or '').replace('subview-', '') or 'unknown'}",
    ]
    return "\n".join(lines)


@tutor_bp.route("/api/tutor", methods=["POST"])
def tutor():
    data = request.get_json(silent=True) or {}
    question = str(data.get("question") or "").strip()[:MAX_QUESTION_CHARS]
    if not question:
        return jsonify({"error": "question is required"}), 400

    lang = "hi" if data.get("lang") == "hi" else "en"
    system = SYSTEM_PROMPT.format(
        language="Hindi (Devanagari script)" if lang == "hi" else "English",
        context=_describe_context(data.get("context"), lang),
    )

    try:
        resp = _get_client().models.generate_content(
            model=MODEL,
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=system,
                max_output_tokens=400,
            ),
        )
    except KeyError:
        # GEMINI_API_KEY not set.
        return jsonify({"error": "tutor unavailable: missing GEMINI_API_KEY"}), 502
    except (genai_errors.ClientError, genai_errors.ServerError) as exc:
        # The frontend treats any non-200 as "use demo answers".
        return jsonify({"error": f"tutor unavailable: {exc.__class__.__name__}"}), 502

    answer = (resp.text or "").strip()
    if not answer:
        return jsonify({"error": "empty answer"}), 502
    return jsonify({"answer": answer})