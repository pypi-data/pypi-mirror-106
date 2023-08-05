from typing import Optional

import base58

from metext.plugin_base import BaseDecoder, Decodable
from metext.utils import convert_to_bytes

CHARSETS = {
    "bitcoin": "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz",
    "ripple": "rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz",
    "flickr": "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ",
}


class Base58Decoder(BaseDecoder):
    PLUGIN_NAME = "base58"
    PLUGIN_ACTIVE = False

    @classmethod
    def run(cls, _input: Decodable, **kwargs) -> Optional[bytes]:
        """Decodes Base58 encoded bytes-like object or ASCII `data` string
        using the charset defined for Bitcoin addresses.

        Using https://rosettacode.org/wiki/Bitcoin/address_validation#Python

        :param _input: Base58 encoded (bytes) string
        :param kwargs: Arbitrary keyword arguments
        :keyword charset: Alphabet for base58 decoding. Use Bitcoin alphabet by default
        :return: Decode bytes string. Returns `None` if `data` couldn't be decoded.
        """
        charset = kwargs.get("charset", CHARSETS["bitcoin"])
        assert len(charset) == 58

        try:
            return base58.b58decode(_input, alphabet=convert_to_bytes(charset))
        except:
            return None


class Base58BitcoinDecoder(BaseDecoder):
    PLUGIN_NAME = "base58btc"

    @classmethod
    def run(cls, _input: Decodable, **kwargs) -> Optional[bytes]:
        """Decodes Base58 encoded bytes-like object or ASCII `data` string
        using the charset defined for Bitcoin addresses.

        Using https://rosettacode.org/wiki/Bitcoin/address_validation#Python

        :param _input: Base58 encoded (bytes) string
        :param kwargs: Arbitrary keyword arguments
        :return: Decode bytes string. Returns `None` if `data` couldn't be decoded.
        """
        return Base58Decoder.run(_input, charset=CHARSETS["bitcoin"])


class Base58RippleDecoder(BaseDecoder):
    PLUGIN_NAME = "base58ripple"

    @classmethod
    def run(cls, _input: Decodable, **kwargs) -> Optional[bytes]:
        """Decodes Base58 encoded bytes-like object or ASCII `data` string
        using the charset defined for Bitcoin addresses.

        Using https://rosettacode.org/wiki/Bitcoin/address_validation#Python

        :param _input: Base58 encoded (bytes) string
        :param kwargs: Arbitrary keyword arguments
        :return: Decode bytes string. Returns `None` if `data` couldn't be decoded.
        """
        return Base58Decoder.run(_input, charset=CHARSETS["ripple"])
