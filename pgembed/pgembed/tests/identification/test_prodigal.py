import subprocess
import pytest

from pgembed.identification import ProdigalIdentifier


def test_prodigal_installed():
    identifier = ProdigalIdentifier()
    assert identifier.verify()
