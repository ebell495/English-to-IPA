FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /english-to-ipa
WORKDIR /english-to-ipa
RUN python3 -m pip install . && chmod +x fuzz/ipa_convert_fuzz.py

ENTRYPOINT [ ]
CMD ["/english-to-ipa/fuzz/ipa_convert_fuzz.py"]