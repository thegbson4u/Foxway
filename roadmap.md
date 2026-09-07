# FOXWAY --- 2-Month Weekly Roadmap

**Project:** FOXWAY: AI-Powered Threat Intelligence Framework\
**Team:** Prince Kumar Maurya & Prakhar Lal\
**Timeline:** 8 weeks\
**Goal:** Complete a working end-to-end prototype within two months,
covering CTI report processing, IOC/entity extraction, behavior
analysis, MITRE ATT&CK mapping, evidence verification,
storage/retrieval, analyst interface, evaluation, and final
demonstration.

> **Note:** The roadmap defines shared weekly targets for Prince and
> Prakhar. It does **not** assign individual tasks. Both members are
> expected to work toward the same weekly milestone.

------------------------------------------------------------------------

## Week 1 --- Foundation & Project Setup

**Target:** Establish the technical foundation and freeze the initial
project scope.

-   Finalize the end-to-end FOXWAY workflow and component boundaries.
-   Set up the development environment and project structure.
-   Establish the initial CTI report dataset and define the expected
    output schema.
-   Set up the basic FastAPI, Streamlit, PostgreSQL and project
    configuration structure.
-   Define provenance requirements so extracted information can retain
    report/page/chunk/evidence references.

**Week-end milestone:** A runnable project skeleton with a small set of
CTI reports ready for processing and a clearly defined data/output
structure.

------------------------------------------------------------------------

## Week 2 --- Document Processing & IOC Extraction

**Target:** Build a reliable first stage that converts CTI PDFs into
structured text and indicators.

-   Implement PDF ingestion and validation using PyMuPDF.
-   Preserve report and page-level provenance during extraction and
    chunking.
-   Implement deterministic extraction for IPs, domains, URLs, hashes,
    CVEs and emails.
-   Add normalization and validation of extracted indicators.
-   Produce a structured intermediate output for each processed report.

**Week-end milestone:** FOXWAY can take a CTI PDF and produce page-aware
text/chunks plus validated IOC results.

------------------------------------------------------------------------

## Week 3 --- Entity & Behavior Extraction

**Target:** Move from structured indicators to security entities and
attacker behaviors.

-   Implement NLP-based extraction for entities such as threat actors,
    malware, tools, campaigns and vulnerabilities.
-   Establish the behavior schema: Action, Mechanism, Object, Source,
    Page, Evidence, Method and Confidence.
-   Add rule-based and NLP-supported behavior identification.
-   Integrate constrained LLM-assisted interpretation for context-heavy
    behavior descriptions.
-   Preserve source evidence for every important extracted result.

**Week-end milestone:** A CTI report produces IOCs, entities and
structured attacker behaviors with supporting evidence.

------------------------------------------------------------------------

## Week 4 --- Semantic Representation & MITRE ATT&CK Retrieval

**Target:** Build the core intelligence-mapping layer.

-   Generate embeddings for behavior descriptions and relevant text
    chunks.
-   Integrate machine-readable MITRE ATT&CK data as the reference
    knowledge base.
-   Implement semantic retrieval of candidate ATT&CK
    techniques/sub-techniques.
-   Generate Top-K candidates for extracted behaviors.
-   Ensure mappings are based on retrieved ATT&CK knowledge rather than
    arbitrary LLM-generated technique IDs.

**Week-end milestone:** Extracted behaviors can be converted into
semantic representations and matched against relevant MITRE ATT&CK
candidates.

------------------------------------------------------------------------

## Week 5 --- Evidence Verification, Confidence & Storage

**Target:** Make the intelligence traceable, verifiable and persistently
stored.

-   Implement evidence verification for extracted behaviors and ATT&CK
    mappings.
-   Establish confidence estimation using available signals such as
    semantic similarity, entities, keywords and review information.
-   Set up PostgreSQL as the primary structured storage layer.
-   Integrate pgvector for embeddings and similarity search.
-   Store intelligence, evidence, mappings, confidence and provenance in
    a consistent schema.

**Week-end milestone:** FOXWAY has a persistent, evidence-backed
intelligence pipeline from CTI report to stored ATT&CK-mapped results.

------------------------------------------------------------------------

## Week 6 --- Analyst Interface & Retrieval

**Target:** Turn the backend pipeline into a usable analyst-facing
prototype.

-   Build the Streamlit analyst interface.
-   Support CTI report upload and processing.
-   Display extracted IOCs, entities, behaviors and ATT&CK mappings.
-   Display source evidence, confidence and provenance for results.
-   Add analyst review/validation states such as accept/reject.
-   Implement the basic retrieval layer for querying processed
    intelligence.

**Week-end milestone:** An analyst can upload a report, inspect the
generated intelligence, verify results and retrieve stored information
through the interface.

------------------------------------------------------------------------

## Week 7 --- RAG, Integration & Evaluation

**Target:** Complete the end-to-end system and validate its quality.

-   Integrate the retrieval-based analyst Q&A flow.
-   Ensure analyst questions retrieve relevant stored intelligence and
    supporting evidence.
-   Connect all major components into one stable end-to-end workflow.
-   Test the complete pipeline across representative CTI reports.
-   Evaluate IOC extraction and ATT&CK mapping using appropriate
    accuracy/reliability metrics.
-   Identify and fix the most important integration and quality issues.

**Week-end milestone:** A stable end-to-end FOXWAY prototype is working
across representative CTI reports with evidence-grounded analyst
responses.

------------------------------------------------------------------------

## Week 8 --- Stabilization, Documentation & Final Demo

**Target:** Make the project presentation-ready and complete the
two-month delivery.

-   Resolve remaining critical bugs and integration issues.
-   Improve output consistency, error handling and interface usability.
-   Finalize evaluation results and representative examples.
-   Prepare the final system architecture and workflow documentation.
-   Complete project documentation and demonstration material.
-   Run a complete final demonstration from CTI PDF ingestion to
    evidence-backed analyst output.

**Week-end milestone:** FOXWAY is a complete, demonstrable prototype
with documented architecture, evaluation results and an end-to-end
working workflow.

------------------------------------------------------------------------

## 8-Week Delivery Summary

  -----------------------------------------------------------------------
  Week                    Primary Milestone       Expected State
  ----------------------- ----------------------- -----------------------
  1                       Foundation              Project structure,
                                                  scope, dataset and
                                                  schemas ready

  2                       Document + IOC Pipeline PDF → text/chunks →
                                                  validated IOCs

  3                       Entities + Behaviors    IOCs + entities +
                                                  structured behaviors +
                                                  evidence

  4                       ATT&CK Retrieval        Behaviors → embeddings
                                                  → ATT&CK candidates

  5                       Verification + Storage  Evidence-backed
                                                  intelligence stored in
                                                  PostgreSQL/pgvector

  6                       Analyst Interface       Upload, inspect, review
                                                  and retrieve
                                                  intelligence

  7                       RAG + Evaluation        End-to-end workflow
                                                  validated and evaluated

  8                       Finalization            Stable prototype,
                                                  documentation and final
                                                  demonstration
  -----------------------------------------------------------------------

## Final 2-Month Outcome

By the end of Week 8, the project should demonstrate the complete
intended FOXWAY pipeline:

**CTI Report → File Validation → PDF Processing → Normalization &
Chunking → IOC/Entity Extraction → Hybrid Behavior Extraction → Semantic
Embeddings → MITRE ATT&CK Candidate Retrieval → Evidence Verification →
Confidence Estimation → Structured Storage → Analyst Interface →
Retrieval-Based Querying**

The primary focus throughout the eight weeks is to maintain a **working
end-to-end system**, rather than over-expanding individual components.
Features that are not essential to the core pipeline should remain
secondary until the main workflow is stable.
