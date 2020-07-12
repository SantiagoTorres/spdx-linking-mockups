#!/usr/bin/env python
import os
import os.path
import shutil

TEST_FILENAME = os.getenv("SPLIT_FILENAME", "nginx-spdx-tern.txt")
VERBOSE = os.getenv("SPLIT_VERBOSE", False)

if os.path.exists("spdx_docs"):
    print("Removing old documents...")
    shutil.rmtree("spdx_docs")

os.mkdir("spdx_docs")

def serialize_document(data):
    basename = data[data.index("SPDXRef"):].split()[0]
    filename = os.path.join("spdx_docs", basename)

    with open(filename, 'wt') as fp:
        fp.write(data)

    return basename

with open(TEST_FILENAME) as fp:
    data = fp.read()

# we merge the two first chunks to create a toplevel nginx document with a
# bunch of relationships
chunks = data.split("PackageName")
toplevel = chunks.pop(0)
toplevel += "PackageName" + chunks.pop(0)
toplevel_name = serialize_document(toplevel)

print("Toplevel is saved at spdx_docs/" + toplevel_name)

for chunk in chunks:
    # we are instantiating a string here for each chunk, we could be smarter
    # if we did something else rather than split (like tokenization)
    name = serialize_document("PackageName" + chunk)

    if VERBOSE:
        print(chunk.split("\n")[0][2:] + "saved to spdx_docs/" + name)


# p = Parser(Builder(), StandardLogger())
# p.build()
# document, error = p.parse(data)
