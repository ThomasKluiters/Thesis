import numpy as np
import dataclasses
from typing import Optional


@dataclasses.dataclass(frozen=True)
class PangenomeEmbeddingNode:
    id: str
    sample: str
    sequence: str
    embedding: np.ndarray


@dataclasses.dataclass
class PangenomeEmbeddingGraph:
    pass
