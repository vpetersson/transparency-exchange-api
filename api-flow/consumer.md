# Transparency Exchange API: Consumer access

The consumer access starts with a TEI, A transparency Exchange Identifier. This
is used to find the API server as described in the
[discovery document](/discovery/readme.md).

## API usage

The standard TEI points to a product.

- **List of TEA leafs**: Leafs are components of something sold. Each leaf has
  it's own versioning and it's own set of artefacts. Note that a single artefact
  can belong to multiple versions of a leaf and multiple leafs.
- **List of TEA collections**: For each leaf, there is a list of TEA collections
  as indicated by release date and a version string. The TEA API has no
  requirements of type of version string (semantic or any other scheme) - it's
  just an identifier set by the manufacturer. It's sorted by release date as a
  default.
- **List of TEA artefacts**: The collection is unique for a version and contains
  a list of artefacts. This can be SBOM files, VEX, SCITT, IN-TOTO or other
  documents.
- **List of artefact formats**: An artefact can be published in multiple
  formats.

The user has to know product TEI and version of each component (TEA LEAF) to
find the list of artefacts for the used version.

## API flow

```mermaid
sequenceDiagram
    autonumber
    actor user
    participant discovery as TEA Discovery
    participant tea_product as TEA Product
    participant tea_leaf as TEA Leaf
    participant tea_collection as TEA Collection
    participant tea_artifact as TEA Artefact

    Note over user,discovery: DNS-based discovery
    user ->> discovery: DNS lookup using TEI
    discovery -->> user: API server endpoints returned

    Note over user,tea_product: List all products
    user ->> tea_product: GET to /v1/product
    tea_product -->> user: List of products returned (paginated)

    Note over user,tea_product: Get specific product information
    user ->> tea_product: GET to /v1/product/{tea_product_identifier}
    tea_product -->> user: Product details with leaf references returned

    Note over user,tea_leaf: Get version information
    user ->> tea_leaf: GET to /v1/leaf?tea_product_identifier={product_id}
    tea_leaf -->> user: List of available versions returned (paginated)

    Note over user,tea_collection: Get artifacts for specific version
    user ->> tea_collection: GET to /v1/collection/{tea_collection_identifier}
    tea_collection -->> user: Collection with available artifacts returned

    Note over user,tea_artifact: Download specific artifact
    user ->> tea_artifact: GET to artifact URL
    tea_artifact -->> user: Artifact content returned
```

## Simplified workflow: Retrieving the latest SBOM using a TEI (EAN barcode)

For many consumer use cases, the goal is simply to retrieve the latest SBOM for a product identified by a TEI (such as an EAN barcode). Here's a simplified workflow for this common scenario:

```mermaid
sequenceDiagram
    autonumber
    actor user
    participant tea_product as TEA Product
    participant tea_leaf as TEA Leaf
    participant tea_collection as TEA Collection
    participant tea_artifact as TEA Artefact

    Note over user,tea_product: Lookup product by barcode
    user ->> tea_product: GET to /v1/product?barcode={barcode}
    tea_product -->> user: Product details with identifier returned

    Note over user,tea_leaf: Get leaf for product
    user ->> tea_leaf: GET to /v1/leaf?tea_product_identifier={product_id}
    tea_leaf -->> user: Leaf details with collection references returned

    Note over user,tea_collection: Get collection with artifacts
    user ->> tea_collection: GET to /v1/collection/{tea_collection_identifier}
    tea_collection -->> user: Collection with artifacts returned

    Note over user,tea_artifact: Download SBOM
    user ->> tea_artifact: GET to artifact URL (for artifact with type="bom")
    tea_artifact -->> user: SBOM content returned
```

This simplified workflow focuses on the most common consumer use case: retrieving the latest SBOM for a product using its TEI (such as an EAN barcode). The process involves:

1. Querying the product API with the TEI (barcode) to get the product identifier
2. Retrieving the latest leaf version by sorting by release date
3. Getting the collection for that leaf version
4. Downloading the SBOM artifact from the collection

This approach minimizes the number of API calls needed while ensuring the consumer gets the most up-to-date SBOM information available for the product.
