import json

from identification import ProdigalIdentifier
from pgembed.model import UriSequenceSource
from pgembed.embedder import ElmoProteinEmbedder
from pgembed.model.graph import PangenomeEmbeddingNode
from util import DatasetCollection
import os

current_location = os.path.dirname(__file__)

if __name__ == '__main__':
    experiment_directory = os.path.join(current_location, "..", "experiments", "e_coli")

    os.makedirs(experiment_directory, exist_ok=True)

    species = DatasetCollection.from_species('e_coli')
    identifier = ProdigalIdentifier()

    embedder = ElmoProteinEmbedder.from_weights(
        os.path.join(current_location, "..", "embeddings", "uniref50_v2"))

    for sample in species.samples:
        proteins = identifier.identify_genes(UriSequenceSource(sample.find_fasta_file()))
        bio_seq = proteins.as_bio_seq()
        nodes = []
        for record in bio_seq:
            nodes.append(
                PangenomeEmbeddingNode(record.id, record.name, record.seq, embedder.perform_embedding(record.seq)))
        with open(os.path.join([experiment_directory, f"{sample.name()}.json"]), "w+") as fp:
            fp.write(json.dumps({"sample": sample.name(), "nodes": nodes}))
