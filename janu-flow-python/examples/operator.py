##
## Copyright (c) 2017, 2021 TAWHEED
##
## This program and the accompanying materials are made available under the
## terms of the Eclipse Public License 2.0 which is available at
## http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
## which is available at https://www.apache.org/licenses/LICENSE-2.0.
##
## SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
##
## Contributors:
##   TAWHEED janu team, <janu@tawedge.com>
##

from janu_flow import Inputs, Outputs, Operator


class MyOp(Operator):
    def initialize(self, configuration):
        return None

    def finalize(self, state):
        return None

    def run(self, _ctx, _state, inputs):
        # print(type(inputs))
        data = inputs.get('Data').data
        # print(f'data {data}')
        int_data = int_from_bytes(data)
        int_data = int_data * 2
        # print(f'updated data {int_data}')
        # outputs = {'Data' : int_to_bytes(int_data)}
        # print(type(output))
        outputs = Outputs()
        outputs.put('Data', int_to_bytes(int_data))

        return outputs



def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')

def register():
    return MyOp