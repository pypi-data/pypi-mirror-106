from django.conf import settings

GLOSSARY_DISCLOSURE_MODEL = getattr(settings, "GLOSSARY_DISCLOSURE_MODEL", "common.GlossaryDisclosure")
GLOSSARY_TERM_MODEL = getattr(settings, "GLOSSARY_TERM_MODEL", "common.GlossaryTerm")
