# Copyright (c) 2020 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Specifications:
# https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki

# Imports
from typing import List, Tuple
from bip_utils.bech32.bech32_base import Bech32DecoderBase, Bech32EncoderBase, Bech32BaseUtils
from bip_utils.bech32.bech32_ex import Bech32FormatError
from bip_utils.utils import ConvUtils


class SegwitBech32Const:
    """ Class container for Segwit Bech32 constants. """

    # Separator
    SEPARATOR: str = "1"
    # Checkum length
    CHECKSUM_LEN: int = 6
    # Witness version maximum value
    WITNESS_VER_MAX_VAL: int = 16
    # Minimum data length
    DATA_MIN_LEN: int = 2
    # Maximum data length
    DATA_MAX_LEN: int = 40
    # Accepted data lengths when witness version is zero
    WITNESS_VER_ZERO_DATA_LEN: Tuple[int, int] = (20, 32)


class SegwitBech32Utils:
    """ Class container for Segwit utility functions. """

    @staticmethod
    def PolyMod(values: List[int]) -> int:
        """ Computes the polynomial modulus.

        Args:
            values (list): List of polynomial coefficients

        Returns:
            int: Computed modulus
        """

        # Generator polynomial
        generator = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3]

        # Compute modulus
        chk = 1
        for value in values:
            top = chk >> 25
            chk = (chk & 0x1ffffff) << 5 ^ value
            for i in range(5):
                chk ^= generator[i] if ((top >> i) & 1) else 0
        return chk

    @staticmethod
    def HrpExpand(hrp: str) -> List[int]:
        """ Expand the HRP into values for checksum computation.

        Args:
            hrp (str): HRP

        Returns:
            list: Expanded HRP values
        """
        # [upper 3 bits of each character] + [0] + [lower 5 bits of each character]
        return [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 0x1f for x in hrp]

    @staticmethod
    def ComputeChecksum(hrp: str,
                        data: List[int]) -> List[int]:
        """ Compute the checksum from the specified HRP and data.

        Args:
            hrp (str)  : HRP
            data (list): Data part

        Returns:
            list: Computed checksum
        """

        values = SegwitBech32Utils.HrpExpand(hrp) + data
        polymod = SegwitBech32Utils.PolyMod(values + [0, 0, 0, 0, 0, 0]) ^ 1
        return [(polymod >> 5 * (5 - i)) & 0x1f for i in range(SegwitBech32Const.CHECKSUM_LEN)]

    @staticmethod
    def VerifyChecksum(hrp: str,
                       data: List[int]) -> bool:
        """ Verify the checksum from the specified HRP and converted data characters.

        Args:
            hrp  (str) : HRP
            data (list): Data part

        Returns:
            bool: True if valid, false otherwise
        """
        return SegwitBech32Utils.PolyMod(SegwitBech32Utils.HrpExpand(hrp) + data) == 1


class SegwitBech32Encoder(Bech32EncoderBase):
    """ Segwit Bech32 encoder class. It provides methods for encoding to Segwit Bech32 format. """

    @staticmethod
    def Encode(hrp: str,
               wit_ver: int,
               wit_prog: bytes) -> str:
        """ Encode to Segwit Bech32.

        Args:
            hrp (str)       : HRP
            wit_ver (int)   : Witness version
            wit_prog (bytes): Witness program

        Returns:
            str: Encoded address

        Raises:
            Bech32FormatError: If the data is not valid
        """

        return SegwitBech32Encoder._EncodeBech32(hrp,
                                                 [wit_ver] + Bech32BaseUtils.ConvertToBase32(wit_prog),
                                                 SegwitBech32Const.SEPARATOR)

    @staticmethod
    def _ComputeChecksum(hrp: str,
                         data: List[int]) -> List[int]:
        """ Compute the checksum from the specified HRP and data.

        Args:
            hrp (str)  : HRP
            data (list): Data part

        Returns:
            list: Computed checksum
        """
        return SegwitBech32Utils.ComputeChecksum(hrp, data)


class SegwitBech32Decoder(Bech32DecoderBase):
    """ Segwit Bech32 decoder class. It provides methods for decoding Segwit Bech32 format. """

    @staticmethod
    def Decode(hrp: str,
               addr: str) -> Tuple[int, bytes]:
        """ Decode from Segwit Bech32.

        Args:
            hrp (str) : Human readable part
            addr (str): Address

        Returns:
            tuple: Witness version (index 0) and witness program (index 1)

        Raises:
            Bech32FormatError: If the bech32 string is not valid
            Bech32ChecksumError: If the checksum is not valid
        """

        # Decode string
        hrpgot, data = SegwitBech32Decoder._DecodeBech32(addr,
                                                         SegwitBech32Const.SEPARATOR,
                                                         SegwitBech32Const.CHECKSUM_LEN)
        # Check HRP
        if hrpgot != hrp:
            raise Bech32FormatError("Invalid format (HRP not valid, expected %s, got %s)" % (hrp, hrpgot))

        # Convert back from base32
        conv_data = Bech32BaseUtils.ConvertFromBase32(data[1:])

        # Check converted data
        if len(conv_data) < SegwitBech32Const.DATA_MIN_LEN or len(conv_data) > SegwitBech32Const.DATA_MAX_LEN:
            raise Bech32FormatError("Invalid format (length not valid)")
        elif data[0] > SegwitBech32Const.WITNESS_VER_MAX_VAL:
            raise Bech32FormatError("Invalid format (witness version not valid)")
        elif data[0] == 0 and not len(conv_data) in SegwitBech32Const.WITNESS_VER_ZERO_DATA_LEN:
            raise Bech32FormatError("Invalid format (length not valid)")

        return data[0], ConvUtils.ListToBytes(conv_data)

    @staticmethod
    def _VerifyChecksum(hrp: str,
                        data: List[int]) -> bool:
        """ Verify the checksum from the specified HRP and converted data characters.

        Args:
            hrp  (str) : HRP
            data (list): Data part

        Returns:
            bool: True if valid, false otherwise
        """
        return SegwitBech32Utils.VerifyChecksum(hrp, data)
