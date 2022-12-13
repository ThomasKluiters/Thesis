import dataclasses
import os
from typing import List, Optional
from pathlib import Path

DATASETS_FOLDER = os.path.join(os.path.dirname(__file__), "..", "datasets")


@dataclasses.dataclass
class Sample:
    path: str

    def name(self) -> str:
        return Path(self.path).stem

    def relative_file(self, name) -> str:
        return os.path.join(self.path, name)

    def find_fasta_file(self) -> Optional[str]:
        for file in os.listdir(self.path):
            if file.endswith("fna"):
                return os.path.join(self.path, file)
        return None

    @classmethod
    def from_path(cls, path: str):
        return Sample(path)


@dataclasses.dataclass
class DatasetCollection:
    species: str
    samples: List[Sample]

    @classmethod
    def from_species(cls, species: str) -> 'DatasetCollection':
        path = os.path.join(DATASETS_FOLDER, species)
        files = [os.path.normpath(os.path.join(path, file)) for file in os.listdir(path)]
        samples = [Sample.from_path(file) for file in files if os.path.isdir(file)]
        return DatasetCollection(species, samples)
