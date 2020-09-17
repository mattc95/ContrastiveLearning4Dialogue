#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
Glove vectors.
"""

import os
import torchtext.vocab as vocab



def download(datapath):
    return vocab.GloVe(
        name='840B', dim=300, cache=os.path.join(datapath, 'models', 'glove_vectors'),
    )
