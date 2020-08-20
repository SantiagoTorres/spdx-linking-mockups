# SBoM placement in container images

This is a mock-up of how an nginx container would look like if it included a Software Bill of Materials. The SBoM format used is SPDX 2.2.

## index.json

The OCI image layout allows for an `index.json` wherein a list of manifests may be included. The image index was downloaded from https://index.docker.io/v2/library/nginx/manifests/1.19.0. One can download an index based on digest but there is no way to find the digest without attempting to download an `index.json` based on tag.

## blobs

`index.json` will reference a number of manifests and their digests. These artifacts are stored as blobs on the registry. The manifest for the amd64 nginx container image was downloaded from https://index.docker.io/v2/library/nginx/blobs/<digest>. The digest is aquired from `index.json`.  

## Considerations for SBoM content

- Content addressable artifacts are identified based on digests. an SBoM document cannot refer to itself in this case because changing the content of the SBoM changes the digest and hence the name of the document. An SBoM document can refer to other SBoM documents only after it has been generated and its digest is calculated. 
- The download location is the same for the image and the artifacts. How do we say "this SBoM describes this blob which was downloaded from the same endpoint as the SBoM"?
