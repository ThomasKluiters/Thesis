import dataclasses
import torch
from typing import List

from pathlib import Path

from allennlp.commands.elmo import ElmoEmbedder


@dataclasses.dataclass
class ElmoProteinEmbedder:
    elmo_embedder: ElmoEmbedder

    def perform_embedding(self, protein: str) -> torch.Tensor:
        return self.perform_batch_embedding([protein])[0]

    def perform_batch_embedding(self, amino_acids: List[str]) -> List[torch.Tensor]:
        amino_acids = [list(protein_sequence) for protein_sequence in amino_acids]
        amino_acids.sort(key=len)
        embeddings = self.elmo_embedder.embed_batch(amino_acids)
        return [torch.tensor(embedding).sum(dim=0).mean(dim=0) for embedding in embeddings]

    @classmethod
    def from_weights(cls, path: str) -> 'ElmoProteinEmbedder':
        model_dir = Path(path)
        weights = model_dir / 'weights.hdf5'
        options = model_dir / 'options.json'
        return ElmoProteinEmbedder(ElmoEmbedder(options, weights))
