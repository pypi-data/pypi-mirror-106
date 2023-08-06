from django.forms import inlineformset_factory

from scarlet.cms import forms, bundles, views
from scarlet.disclosures import get_glossary_term_model, get_glossary_disclosure_model


class DisclosureInlineFormset(forms.LazyFormSetFactory):
    def __init__(self):
        super().__init__(
            inlineformset_factory,
            get_glossary_term_model(),
            get_glossary_disclosure_model(),
            can_order=False,
            can_delete=True,
        )


class GlossaryBundle(bundles.Bundle):
    dashboard = (("main",),)

    edit = views.FormView(formsets={"Disclosures": DisclosureInlineFormset()})
    add = edit

    class Meta:
        model = get_glossary_term_model()
