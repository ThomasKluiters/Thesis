import dataclasses
from typing import Iterable

import Bio.SeqRecord
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


@dataclasses.dataclass(frozen=True, unsafe_hash=True)
class SequenceSource:
    def as_uri(self):
        raise NotImplementedError

    def as_string(self):
        raise NotImplementedError

    def as_stream(self):
        raise NotImplementedError

    def as_bio_seq(self) -> 'SeqIOSequenceSource':
        raise NotImplementedError


@dataclasses.dataclass(frozen=True, unsafe_hash=True)
class StringSequenceSource(SequenceSource):
    sequence: str

    def as_uri(self):
        pass

    def as_string(self):
        return self.sequence

    def as_stream(self):
        pass


@dataclasses.dataclass(frozen=True, unsafe_hash=True)
class UriSequenceSource(SequenceSource):
    uri: str

    def as_uri(self):
        return self.uri

    def as_string(self):
        pass

    def as_stream(self):
        pass

    def as_bio_seq(self):
        return SeqIOSequenceSource(SeqIO.parse(self.uri, 'fasta'))


@dataclasses.dataclass(frozen=True, unsafe_hash=True)
class StreamSequenceSource(SequenceSource):
    stream: str

    def as_uri(self):
        pass

    def as_string(self):
        pass

    def as_stream(self):
        pass


@dataclasses.dataclass(frozen=True, unsafe_hash=True)
class SeqIOSequenceSource(SequenceSource):
    seq: SeqIO.FastaIO.FastaIterator

    def as_string(self):
        pass

    def as_stream(self):
        pass

    def as_uri(self):
        pass

    def __iter__(self) -> Iterable[Bio.SeqRecord.SeqRecord]:
        return self.seq.__iter__()