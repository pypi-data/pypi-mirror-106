from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.component.util import LocalFilenameSource
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SourceStageSpecifier


class COCOInputFormatSpecifier(SourceStageSpecifier):
    """
    Specifier of the components for reading the MS-COCO JSON-based
    object detection format.
    """
    @classmethod
    def description(cls) -> str:
        return "Reads image object-detection annotations in the MS-COCO JSON-format"

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from ..component import FromCOCO
        return LocalFilenameSource, FromCOCO

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.object_detection import ImageObjectDetectionDomainSpecifier
        return ImageObjectDetectionDomainSpecifier
