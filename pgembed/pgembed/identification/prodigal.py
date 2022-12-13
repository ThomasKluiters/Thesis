import dataclasses
import os.path
import re
import subprocess
from typing import List, Union, Optional

from .base import GeneIdentifier
from pgembed.model import SequenceSource, UriSequenceSource

PRODIGAL_VERSION_REGEX = r"Prodigal V([0-9.]+): ([a-zA-Z]+), ([0-9]+)"
PRODIGAL_CACHE_LOCATION = os.path.join("~", ".pgembed", "cache")


def create_cache_directory():
    os.makedirs(PRODIGAL_CACHE_LOCATION, exist_ok=True)


@dataclasses.dataclass
class ProdigalIdentifier(GeneIdentifier):
    executable_location: str = 'prodigal'

    def run_prodigal_with_commands(self, commands: List[str]) -> str:
        return subprocess.check_output([self.executable_location] + commands, stderr=subprocess.STDOUT).decode(
            'utf-8').strip()

    def version(self) -> Optional[str]:
        version_output = self.run_prodigal_with_commands(['-v'])

        match = re.search(PRODIGAL_VERSION_REGEX, version_output)
        if not match:
            return None

        (version, month, year) = match.groups()
        return version

    def verify(self):
        version_output = self.run_prodigal_with_commands(['-v'])
        return version_output is not None

    def identify_genes(self, source: SequenceSource) -> SequenceSource:
        create_cache_directory()
        if isinstance(source, UriSequenceSource):
            input_file = source.as_uri()
            output_file = f"{input_file}.proteins"
            print(output_file)
            if not os.path.exists(output_file):
                subprocess.run([self.executable_location, "-i", input_file, "-a", output_file])
            return UriSequenceSource(output_file)
