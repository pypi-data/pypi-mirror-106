import re
from collections import Counter
from typing import Iterable

from metext.plugin_base import BaseExtractor
from metext.plugins.extractors import _extract_with_regex
from metext.plugins.validators.baseenc import Base32Validator, Base64Validator
from metext.utils.regex import RE_BASE32, RE_BASE64


class Base32Extractor(BaseExtractor):
    PLUGIN_NAME = "base32"

    @classmethod
    def run(cls, _input: str, **kwargs) -> Iterable[dict]:
        """Extracts (standard) padded Base32 strings.

        See https://tools.ietf.org/html/rfc4648#section-4

        :param _input: String or a list of strings
        :param kwargs: Arbitrary keyword arguments
        :keyword min_len: Minimum length of base32 found strings,
        defaults to 25
        :return: Generator of Base32 strings
        """

        def validate(value):
            if len(value) < min_len:
                return False

            counter = Counter(value)
            thresh = len(value) * 0.6
            if any(x for x, c in counter.most_common() if c > thresh if x != "="):
                return False

            return Base32Validator.run(value)

        min_len = kwargs.get("min_len", 25)
        yield from _extract_with_regex(
            _input,
            RE_BASE32,
            validator=validate,
            per_line=True,
            preprocess=lambda val: val.replace(r"\r\n", "")
            .replace(r"\n", "")
            .replace(r"\r", ""),
            data_kind=Base32Extractor.PLUGIN_NAME,
        )


class Base64Extractor(BaseExtractor):
    PLUGIN_NAME = "base64"

    @classmethod
    def run(cls, _input: str, **kwargs) -> Iterable[dict]:
        """Extracts (standard) padded Base64 strings.

        See https://tools.ietf.org/html/rfc4648#section-4

        :param _input: String or a list of strings
        :param kwargs: Arbitrary keyword arguments
        :keyword min_len: Minimum length of base64 found string,
        defaults to 25
        :return: Generator of Base64 strings
        """

        def validate(value):
            if len(value) < min_len:
                return False
            parts = value.split("/")
            if any(
                x
                for x in parts
                if len(x) > 4 and x in (x.upper(), x.lower()) and "=" not in x
            ):
                return False

            return Base64Validator.run(value, strict=True)

        min_len = kwargs.get("min_len", 25)
        yield from _extract_with_regex(
            _input,
            RE_BASE64,
            validator=validate,
            per_line=False,
            postprocess=(
                lambda val: re.sub("\r\n|\n|\r", "", val)
                .replace(r"\r\n", "")
                .replace(r"\n", "")
                .replace(r"\r", "")
            ),
            data_kind=Base64Extractor.PLUGIN_NAME,
        )


class HexExtractor(BaseExtractor):
    PLUGIN_NAME = "hex"
    PLUGIN_ACTIVE = False

    @classmethod
    def run(cls, _input: str, **kwargs) -> Iterable[dict]:
        """Extracts sequences of hex strings, where each two hex chars are separated by
        a selected delimiter.

        :param _input: String or a list of strings
        :param kwargs: Arbitrary keyword arguments
        :keyword delim: Delimiter separating 2-digit hex representation of a byte,
        can be regex pattern string. Defaults to empty string ("")
        :return: Generator of hex-representation strings
        """
        delim = kwargs.get("delim", "")
        regex = re.compile(HEX_PATTERN_TEMPLATE.format(delim=delim), re.IGNORECASE)
        yield from _extract_with_regex(
            _input, regex, data_kind=HexExtractor.PLUGIN_NAME
        )


HEX_DELIMITERS = {
    "None": "",
    "Space": " ",
    "Comma": ",",
    "Semicolon": ";",
    "Colon": ":",
    "LF": r"\n",
    "CRLF": r"\r\n",
    "0x": "0x",
    "comma-0x": ",0x",
    r"\x": r"[\]x",
}
HEX_PATTERN_TEMPLATE = r"[\dA-F]{{2}}(?:{delim}[\dA-F]{{2}})*"
