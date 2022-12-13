import dataclasses
import re
import subprocess
from typing import List, Union, Optional

from pgembed.identification.base import GeneIdentifier
from pgembed.model import SequenceSource

PRODIGAL_VERSION_REGEX = r"Prodigal V([0-9.]+): ([a-zA-Z]+), ([0-9]+)"


@dataclasses.dataclass
class ProdigalIdentifier(GeneIdentifier):
    executable_location: str = 'prodigal'

    def run_prodigal_with_commands(self, commands: List[str]) -> str:
        return subprocess.check_output([self.executable_location] + commands, stderr=subprocess.STDOUT).decode('utf-8').strip()

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

    def identify_genes(self, source: SequenceSource):
        pass
