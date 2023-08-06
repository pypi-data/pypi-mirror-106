from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SourceStageSpecifier


class ADAMSODInputFormatSpecifier(SourceStageSpecifier):
    """
    Specifier of the components for reading the ADAMS report-based
    object detection format.
    """
    @classmethod
    def description(cls) -> str:
        return "Reads image object-detection annotations in the ADAMS report-format"

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from ...base.component import ADAMSFilenameSource, ADAMSBaseReader
        from ..component import FromADAMSReport
        return ADAMSFilenameSource, ADAMSBaseReader, FromADAMSReport

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.object_detection import ImageObjectDetectionDomainSpecifier
        return ImageObjectDetectionDomainSpecifier
