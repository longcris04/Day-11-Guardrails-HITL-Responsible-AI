"""
Lab 11 — Configuration & API Key Setup
"""
import os

# Model used across all agents. Override via OPENROUTER_MODEL env var.
# Browse available models at https://openrouter.ai/models
OPENROUTER_MODEL = os.environ.get(
    "OPENROUTER_MODEL", "openrouter/google/gemini-2.0-flash"
)


def setup_api_key():
    """Load OpenRouter API key from environment or prompt."""
    if "OPENROUTER_API_KEY" not in os.environ:
        os.environ["OPENROUTER_API_KEY"] = input("Enter OpenRouter API Key: ")
    # NeMo Guardrails & LangChain use these env vars for OpenAI-compatible calls
    os.environ["OPENAI_API_KEY"] = os.environ["OPENROUTER_API_KEY"]
    os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
    print("API key loaded.")


# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
