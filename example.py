#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#     ॐ भूर्भुवः स्वः
#     तत्स॑वि॒तुर्वरे॑ण्यं॒
#    भर्गो॑ दे॒वस्य॑ धीमहि।
#   धियो॒ यो नः॑ प्रचो॒दया॑त्॥
#
#
# बोसजी के द्वारा रचित टिप्पी अधिलेखन प्रकृया।
# ================================
#
# एक सरल संचार सहायक और संलग्न तंत्र।
#
# ~~~~~~~~~~~~~~~~~~~~~~~
# एक रचनात्मक भारतीय उत्पाद।
# ~~~~~~~~~~~~~~~~~~~~~~~
#
# Sources
# --------
#
# https://github.com/boseji/pytppi
#
# License
# ----------
#
#   `tppi` stands for Tilde Pipe Plus Interface
#
#   Copyright (C) 2024 Abhijit Bose (aka. Boseji). All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   <http://www.apache.org/licenses/LICENSE-2.0>
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   SPDX short identifier: Apache-2.0
#

from datetime import datetime
from src.tppi import assemble_func, specify, disassemble, discover


@assemble_func
def build(timestamp: int, value: float):
    return [
        specify(f"{timestamp}", "TS"),
        specify(f"{value}", "F"),
    ]


if __name__ == "__main__":
    print("Transmit Packet")
    print(build(datetime.now().timestamp(), 12.4))
    parts = disassemble("~|TS~1725869454.327236|F~12.4|~")
    parts = [discover(p) for p in parts]
    print("Found:", parts)
    for p in parts:
        if p[1] == "TS":
            print("Time Stamp:", datetime.fromtimestamp(float(p[0])))
        elif p[1] == "F":
            print("Value:", float(p[0]))
