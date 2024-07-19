#!/usr/bin/env python3
#
# MIT License
#
# Copyright (c) 2024 Tony Walker
# Copyright (c) 2024 Megan Oelgoetz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from itertools import product

# number of questions to generate
# edit as needed
total = 2000

# synonyms for HPC cluster
# edit as needed
location = ['center', 'cluster', 'computer', 'resource', 'resource provider', 'provider', 'RP']

# software available
# edit as needed
resource = ['blast', 'boost', 'gcc', 'go', 'matlab', 'python', 'spss']

# variations on how a user might phrase their search
# edit as needed
question = ['Does any {0} have {1}',
            'Which {0} has {1}',
            'What {0} has {1}',
            'Where is {1}']


if __name__ == '__main__':
    count = 1
    print("\"Question\",")
    for q, l, r in product(question, location, resource):
        print("\"" + q.format(l, r) + "\",")
        if count >= total:
            break
        else:
            count += 1
    # print(count)
