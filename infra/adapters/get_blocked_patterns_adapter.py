from infra.ports.get_blocked_patterns_port import GetBlockedPatternsPort

# Deliberately a plain substring blocklist, not an AI-based classifier -- no LLM/moderation provider
# is configured anywhere in this project yet (see tasks/guard-rails-validators). Known limitation:
# easy to bypass with paraphrasing; this is a first line of defense, not a complete solution.
BLOCKED_PATTERNS = [
    # Malicious code / hacking
    "malicious code",
    "malware",
    "ransomware",
    "keylogger",
    "hack into",
    "exploit a vulnerability",
    "sql injection",
    "ddos attack",
    "phishing",
    "código malicioso",
    "vírus de computador",
    "invadir um sistema",
    # Illegal activity / weapons
    "how to make a bomb",
    "buy illegal drugs",
    "counterfeit money",
    "como fazer uma bomba",
    "comprar drogas ilegais",
    # Hate / violence
    "hate speech",
    "how to hurt someone",
    "discurso de ódio",
]


class GetBlockedPatternsAdapter(GetBlockedPatternsPort):
    def execute(self) -> list[str]:
        return BLOCKED_PATTERNS
