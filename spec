{
    "$schema": "https://spec.openapis.org/oas/3.1/dialect/base",
    "openapi": "3.1.1",
    "info": {
        "title": "Transparency Exchange API",
        "summary": "Transparency Exchange API specification for consumers and publishers",
        "description": "TBC",
        "contact": {
            "name": "TEA Working Group",
            "email": "TBC",
            "url": "https://github.com/CycloneDX/transparency-exchange-api"
        },
        "license": {
            "identifier": "Apache-2.0",
            "url": "https://github.com/CycloneDX/transparency-exchange-api/blob/main/LICENSE"
        },
        "version": "0.0.1"
    },
    "servers": [
        {
            "url": "http://localhost/tea/v1",
            "description": "Local development"
        }
    ],
    "paths": {
        "/index/{product-identifier}": {
            "get": {
                "description": "Access the TEA Index for the supplied product identifier",
                "operationId": "getTeaIndex",
                "parameters": [
                    {
                        "$ref": "#/components/parameters/product-identifier"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Requested TEA Index found and returned",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/tea-index"
                                }
                            }
                        }
                    },
                
                    "404": {
                        "$ref": "#/components/responses/404-object-by-id-not-found"
                    }
                
                },
                "tags": [
                    "TEA Index"
                ]
            }
        },
        "/leaf/{product-identifier}/{product-version}": {
            "get": {
                "description": "Get the TEA Leaf that describes the Version of a Product",
                "operationId": "getTeaLeaf",
                "parameters": [
                    {
                        "$ref": "#/components/parameters/product-identifier"
                    },
                    {
                        "$ref": "#/components/parameters/product-version"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Requested TEA Leaf found and returned",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/tea-leaf"
                                }
                            }
                        }
                    },
                    "404": {
                        "$ref": "#/components/responses/404-object-by-id-not-found"
                    }
                },
                "tags": [
                    "TEA Leaf"
                ]
            }
        },
        "/collection/{tea-collection-identifier}": {
            "get": {
                "description": "Get a TEA Collection by it's Identifier",
                "operationId": "getTeaCollection",
                "parameters": [
                    {
                        "$ref": "#/components/parameters/tea-collection-identifier"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Requested TEA Collection found and returned",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/tea-collection"
                                }
                            }
                        }
                    },
                    "404": {
                        "$ref": "#/components/responses/404-object-by-id-not-found"
                    }
                },
                "tags": [
                    "TEA Leaf"
                ]
            }
        }
    },
    "webhooks": {},
    "components": {
        "schemas": {
            "tea-index": {
                "type": "object",
                "properties": {
                    "uuid": {
                        "$ref": "#/components/schemas/type-uuid"
                    },
                    "product-name": {
                        "type": "string"
                    },
                    "product-version": {
                        "type": "string"
                    }
                },
                "reqiured": [
                    "uuid",
                    "product-name",
                    "product-version"
                ]
            },
            "tea-leaf": {
                "type": "object",
                "properties": {
                    "uuid": {
                        "$ref": "#/components/schemas/type-uuid"
                    },
                    "product-name": {
                        "type": "string"
                    },
                    "product-version": {
                        "type": "string"
                    },
                    "release-date": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "prerelease": {
                        "type": "boolean"
                    },
                    "tea-collection-uuid": {
                        "$ref": "#/components/schemas/type-uuid"
                    }
                },
                "reqiured": [
                    "uuid",
                    "product-name",
                    "product-version",
                    "release-date",
                    "prerelease",
                    "tea-collection-uuid"
                ]
            },
            "tea-collection": {
                "type": "object",
                "properties": {
                    "uuid": {
                        "$ref": "#/components/schemas/type-uuid"
                    },
                    "product-name": {
                        "type": "string"
                    },
                    "product-version": {
                        "type": "string"
                    },
                    "release-date": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "author": {
                        "$ref": "#/components/schemas/type-author"
                    },
                    "reason": {
                        "$ref": "#/components/schemas/type-collection-reason"
                    }
                },
                "reqiured": [
                    "uuid",
                    "product-name",
                    "product-version",
                    "release-date",
                    "author",
                    "reason"
                ]
            },
            "tea-collection-artifact": {
                "type": "object",
                "properties": {
                    "uuid": {
                        "$ref": "#/components/schemas/type-uuid"
                    },
                    "name": {
                        "type": "string"
                    },
                    "type": {
                        "$ref": "#/components/schemas/type-tea-collection-artifact-type"
                    },
                    "author": {
                        "$ref": "#/components/schemas/type-author"
                    }
                },
                "reqiured": [
                    "uuid",
                    "name",
                    "author"
                ]
            },
            "type-author": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "email": {
                        "type": "string",
                        "format": "email"
                    },
                    "organization": {
                        "type": "string"
                    }
                },
                "required": [
                    "name",
                    "email",
                    "organization"
                ]
            },
            "type-collection-reason": {
                "type": "string",
                "description": "Event requiring this TEA Collection was published",
                "enum": [
                    "NEW_PRODUCT_RELEASE",
                    "BOM_UPDATED",
                    "ATTESTATION_ADDED",
                    "ATTESTATION_UPDATED"
                ]
            },
            "type-tea-collection-artifact-type": {
                "type": "string",
                "title": "Type",
                "description": "Specifies the type of external reference.",
                "enum": [
                    "vcs",
                    "issue-tracker",
                    "website",
                    "advisories",
                    "bom",
                    "mailing-list",
                    "social",
                    "chat",
                    "documentation",
                    "support",
                    "source-distribution",
                    "distribution",
                    "distribution-intake",
                    "license",
                    "build-meta",
                    "build-system",
                    "release-notes",
                    "security-contact",
                    "model-card",
                    "log",
                    "configuration",
                    "evidence",
                    "formulation",
                    "attestation",
                    "threat-model",
                    "adversary-model",
                    "risk-assessment",
                    "vulnerability-assertion",
                    "exploitability-statement",
                    "pentest-report",
                    "static-analysis-report",
                    "dynamic-analysis-report",
                    "runtime-analysis-report",
                    "component-analysis-report",
                    "maturity-report",
                    "certification-report",
                    "codified-infrastructure",
                    "quality-metrics",
                    "poam",
                    "electronic-signature",
                    "digital-signature",
                    "rfc-9116",
                    "other"
                ],
                "meta:enum": {
                    "vcs": "Version Control System",
                    "issue-tracker": "Issue or defect tracking system, or an Application Lifecycle Management (ALM) system",
                    "website": "Website",
                    "advisories": "Security advisories",
                    "bom": "Bill of Materials (SBOM, OBOM, HBOM, SaaSBOM, etc)",
                    "mailing-list": "Mailing list or discussion group",
                    "social": "Social media account",
                    "chat": "Real-time chat platform",
                    "documentation": "Documentation, guides, or how-to instructions",
                    "support": "Community or commercial support",
                    "source-distribution": "The location where the source code distributable can be obtained. This is often an archive format such as zip or tgz. The source-distribution type complements use of the version control (vcs) type.",
                    "distribution": "Direct or repository download location",
                    "distribution-intake": "The location where a component was published to. This is often the same as \"distribution\" but may also include specialized publishing processes that act as an intermediary.",
                    "license": "The reference to the license file. If a license URL has been defined in the license node, it should also be defined as an external reference for completeness.",
                    "build-meta": "Build-system specific meta file (i.e. pom.xml, package.json, .nuspec, etc)",
                    "build-system": "Reference to an automated build system",
                    "release-notes": "Reference to release notes",
                    "security-contact": "Specifies a way to contact the maintainer, supplier, or provider in the event of a security incident. Common URIs include links to a disclosure procedure, a mailto (RFC-2368) that specifies an email address, a tel (RFC-3966) that specifies a phone number, or dns (RFC-4501) that specifies the records containing DNS Security TXT.",
                    "model-card": "A model card describes the intended uses of a machine learning model, potential limitations, biases, ethical considerations, training parameters, datasets used to train the model, performance metrics, and other relevant data useful for ML transparency.",
                    "log": "A record of events that occurred in a computer system or application, such as problems, errors, or information on current operations.",
                    "configuration": "Parameters or settings that may be used by other components or services.",
                    "evidence": "Information used to substantiate a claim.",
                    "formulation": "Describes how a component or service was manufactured or deployed.",
                    "attestation": "Human or machine-readable statements containing facts, evidence, or testimony.",
                    "threat-model": "An enumeration of identified weaknesses, threats, and countermeasures, dataflow diagram (DFD), attack tree, and other supporting documentation in human-readable or machine-readable format.",
                    "adversary-model": "The defined assumptions, goals, and capabilities of an adversary.",
                    "risk-assessment": "Identifies and analyzes the potential of future events that may negatively impact individuals, assets, and/or the environment. Risk assessments may also include judgments on the tolerability of each risk.",
                    "vulnerability-assertion": "A Vulnerability Disclosure Report (VDR) which asserts the known and previously unknown vulnerabilities that affect a component, service, or product including the analysis and findings describing the impact (or lack of impact) that the reported vulnerability has on a component, service, or product.",
                    "exploitability-statement": "A Vulnerability Exploitability eXchange (VEX) which asserts the known vulnerabilities that do not affect a product, product family, or organization, and optionally the ones that do. The VEX should include the analysis and findings describing the impact (or lack of impact) that the reported vulnerability has on the product, product family, or organization.",
                    "pentest-report": "Results from an authorized simulated cyberattack on a component or service, otherwise known as a penetration test.",
                    "static-analysis-report": "SARIF or proprietary machine or human-readable report for which static analysis has identified code quality, security, and other potential issues with the source code.",
                    "dynamic-analysis-report": "Dynamic analysis report that has identified issues such as vulnerabilities and misconfigurations.",
                    "runtime-analysis-report": "Report generated by analyzing the call stack of a running application.",
                    "component-analysis-report": "Report generated by Software Composition Analysis (SCA), container analysis, or other forms of component analysis.",
                    "maturity-report": "Report containing a formal assessment of an organization, business unit, or team against a maturity model.",
                    "certification-report": "Industry, regulatory, or other certification from an accredited (if applicable) certification body.",
                    "codified-infrastructure": "Code or configuration that defines and provisions virtualized infrastructure, commonly referred to as Infrastructure as Code (IaC).",
                    "quality-metrics": "Report or system in which quality metrics can be obtained.",
                    "poam": "Plans of Action and Milestones (POAM) complement an \"attestation\" external reference. POAM is defined by NIST as a \"document that identifies tasks needing to be accomplished. It details resources required to accomplish the elements of the plan, any milestones in meeting the tasks and scheduled completion dates for the milestones\".",
                    "electronic-signature": "An e-signature is commonly a scanned representation of a written signature or a stylized script of the person's name.",
                    "digital-signature": "A signature that leverages cryptography, typically public/private key pairs, which provides strong authenticity verification.",
                    "rfc-9116": "Document that complies with RFC-9116 (A File Format to Aid in Security Vulnerability Disclosure)",
                    "other": "Use this if no other types accurately describe the purpose of the external reference."
                }
            },
            "type-uuid": {
                "type": "string",
                "format": "uuid",
                "required": true
            }
        },
        "responses": {
            "404-object-by-id-not-found": {
                "description": "Object requested by identifier not found",
                "content": {
                    "application/json": {}
                }
            }
        },
        "parameters": {
            "product-identifier": {
                "name": "product-identifier",
                "description": "Product Identifier part of a TEI",
                "in": "path",
                "required": true,
                "schema": {
                    "type": "string"
                }
            },
            "product-version": {
                "name": "product-version",
                "description": "Product Version string",
                "in": "path",
                "reqiured": true,
                "schema": {
                    "type": "string"
                }
            },
            "tea-collection-identifier": {
                "name": "tea-collection-identifier",
                "description": "TEA Collection Identifier",
                "in": "path",
                "required": true,
                "schema": {
                    "type": "string"
                }
            }
        }
    },
    "security": [],
    "tags": [
        "TEA Index",
        "TEA Leaf"
    ],
    "externalDocs": {
        "description": "Transparency Exchange API specification",
        "url": "https://github.com/CycloneDX/transparency-exchange-api"
    }
}