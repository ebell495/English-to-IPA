#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    import eng_to_ipa as ipa

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    ipa.convert(fdp.ConsumeUnicode(len(data)))


atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()