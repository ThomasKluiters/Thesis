import dataclasses
from typing import Union, Optional

from pgembed.model import SequenceSource


@dataclasses.dataclass
class GeneIdentifier:
    def identify_genes(self, source: SequenceSource):
        raise NotImplementedError

    def version(self) -> Optional[str]:
        raise NotImplementedError

    def verify(self):
        raise NotImplementedError
