from infra.ports.get_scope_keywords_port import GetScopeKeywordsPort

# Career/resume topic keywords (PT + EN) -- a message needs at least one of these (or be a short
# greeting) to be considered in scope. Known limitation: keyword matching, not semantic understanding.
SCOPE_KEYWORDS = [
    # Portuguese
    "currículo",
    "curriculo",
    "experiência",
    "experiencia",
    "habilidade",
    "habilidades",
    "carreira",
    "formação",
    "formacao",
    "projeto",
    "projetos",
    "tecnologia",
    "tecnologias",
    "trabalho",
    "emprego",
    "disponibilidade",
    "salário",
    "salario",
    "entrevista",
    "certificação",
    "certificacao",
    "curso",
    "cursos",
    "profissional",
    "cargo",
    # English
    "resume",
    "cv",
    "experience",
    "skill",
    "skills",
    "career",
    "education",
    "project",
    "projects",
    "technology",
    "technologies",
    "job",
    "work",
    "availability",
    "salary",
    "interview",
    "certification",
    "course",
    "courses",
    "professional",
    "position",
]


class GetScopeKeywordsAdapter(GetScopeKeywordsPort):
    def execute(self) -> list[str]:
        return SCOPE_KEYWORDS
