#!/usr/bin/env python

#  Copyright (c) 2020. Davi Pereira dos Santos
#  This file is part of the dupy project.
#  Please respect the license - more about this in the section (*) below.
#
#  dupy is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  dupy is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with dupy.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.

import heapq
import os
import sys

import xxhash


class Content:
    def __init__(self, size, path):
        self.size = size
        self.paths = [path]

    def add(self, path):
        self.paths.append(path)

    def __lt__(self, other):
        return self.size > other.size

    def __repr__(self):
        return f"{self.size}: {self.paths}"


class Dupy:
    def __init__(self, verbose=True):
        self.verbose = verbose
        self.heap = []
        self.m = {}

    def process(self, path, tab=""):
        name = os.path.basename(path)
        if os.path.isdir(path):
            if self.verbose:
                print(f"{tab}{name} {'{'}", flush=True)
            digest, size = 77777777777777777777777777777777777777, 0
            for entry in os.scandir(path):
                filepath = os.path.join(path, entry)
                subdigest, subsize = self.process(filepath, tab + "  ")
                digest += subdigest
                size += subsize
            digest %= 340282366920938463463374607431768211297
            if self.verbose:
                print(f"{tab}{'}'} ", flush=True, end="")
        else:
            if os.path.islink(path) or os.path.getsize(path) == 0:
                namedigest = xxhash.xxh3_128_intdigest(name)
                digest = namedigest
                size = 0
            else:
                digest = self._file_hash(path)
                size = os.path.getsize(path)
            if self.verbose:
                print(f"{tab + name:<70}", flush=True, end="")

        if self.verbose:
            print(f"{digest}\t\t{size}", flush=True)
        if digest in self.m:
            self.m[digest].add(path)
        else:
            content = Content(size, path)
            self.m[digest] = content
            heapq.heappush(self.heap, content)
        return digest, size

    @staticmethod
    def _file_hash(path, blocksize=65536):  # pragma: no cover
        f = open(path, 'rb')
        xx = xxhash.xxh3_128()
        buf = f.read(blocksize)
        while len(buf) > 0:
            xx.update(buf)
            buf = f.read(blocksize)
        f.close()
        return xx.intdigest()


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) > 1:
        print(sys.argv)
        if sys.argv[-1].startswith("max="):
            folders = sys.argv[1:-1]
            maxout = int(sys.argv[-1].split("=")[1])
        else:
            folders = sys.argv[1:]
            maxout = 100
        d = Dupy(verbose=False)
        for folder in folders:
            if os.path.exists(folder):
                print(folder, "...")
                d.process(folder)
            else:
                print(f"{folder} is not a valid path, please verify")
                sys.exit()
        print()
        print("===============================================================")
        print("===============================================================")
        print()
        print()
        print()
        for cont in reversed(heapq.nsmallest(maxout, d.heap)):
            if len(cont.paths) > 1:
                print(f"{cont.size / 1_000_000:.2f} MB     ({cont.size / 1_000:.3f} KB):")
                for p in cont.paths:
                    print(f"\t{p}")
                print()
    else:
        print('Usage:\n dupy folder [max=100]')
        print('Usage:\n dupy folder1 folder2 folder3 ... [max=100]')
