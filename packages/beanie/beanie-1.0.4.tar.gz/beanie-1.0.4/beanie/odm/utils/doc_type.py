from typing import TYPE_CHECKING
from typing import TypeVar

if TYPE_CHECKING:
    from beanie.odm.documents import Document


DocType = TypeVar("DocType", bound="Document")
