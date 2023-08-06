from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SinkStageSpecifier


class FestVoxOutputFormatSpecifier(SinkStageSpecifier):
    """
    Specifier of the components for writing Festival FestVox
    speech annotations.
    """
    @classmethod
    def description(cls) -> str:
        return "Writes speech transcriptions in the Festival FestVox format"

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from ..component import FestVoxWriter
        return FestVoxWriter,

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.audio.speech import SpeechDomainSpecifier
        return SpeechDomainSpecifier
