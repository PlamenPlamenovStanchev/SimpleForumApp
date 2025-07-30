from django.db import models


class LanguageChoice(models.TextChoices):
    PYTHON = "py", "Python"
    JAVASCRIPT = "js", 'JavaScript'
    C = "c", "C"
    C_PLUS_PLUS = "cpp", "C++"
    C_SHARP = "csharp", "C#"
    RUBY = "rb", "Ruby"
    PHP = "php", "PHP"
    JAVA = "java", "Java"
    OTHER = "other", "Other"