import email
import re
from email import policy
from typing import Optional

from metext.plugin_base import BaseDecoder, Decodable


class MimeDecoder(BaseDecoder):
    PLUGIN_NAME = "mime"

    @classmethod
    def run(cls, _input: Decodable, **kwargs) -> Optional[bytes]:
        """Decodes e-mail MIME document body. Tries to decode the body
        part content.

        At the moment only MIME main types "text" and "application" are
        considered as a text-like content is assumed. Decoded content
        is concatenated and returned as utf-8 encoded bytes.

        :param _input: MIME (e-mail) document
        :param kwargs:
        :return: Bytes string if decoded successfully, else None
        """
        try:
            if isinstance(_input, str):
                _input = bytes(_input, "utf8")

            if not re.search(rb"MIME-Version:\s\d+\.\d+", _input):
                return None

            msg = email.message_from_bytes(
                _input, policy=policy.default.clone(raise_on_defect=True)
            )
            res = []
            if msg.preamble:
                res.append(msg.preamble)
            if msg.is_multipart():
                for part in msg.walk():
                    res.append(part.get_payload(decode=True))
            else:
                res.append(msg.get_payload(decode=True))
            if msg.epilogue:
                res.append(msg.epilogue)
            return b"\n\n".join(
                bytes(part, "utf8") if isinstance(part, str) else part
                for part in res
                if part
            )
        except:
            return None
