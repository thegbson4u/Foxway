# FOXWAY

## AI-Powered Threat Intelligence Framework

FOXWAY is an AI-powered Cyber Threat Intelligence (CTI) framework designed to transform unstructured CTI reports into structured, searchable, and evidence-backed intelligence.

## Project Status

🚧 Under Development

## Proposed Pipeline

CTI Report  
→ Document Processing  
→ IOC & Entity Extraction  
→ Behavior Analysis  
→ MITRE ATT&CK Mapping  
→ Evidence Verification  
→ Structured Intelligence  
→ Analyst Interface  
→ Retrieval-Based Querying

## Technology Stack

- Python
- FastAPI
- Streamlit
- PyMuPDF
- spaCy
- Hugging Face Transformers
- Sentence Transformers
- MITRE ATT&CK
- STIX
- PostgreSQL
- pgvector
- Pydantic
- Plotly
- Docker

## Project Structure

```text
backend/       Backend and API
frontend/      Streamlit analyst interface
data/          CTI data and processed documents
models/        ML/NLP models
mitre_attack/  MITRE ATT&CK resources
notebooks/     Experiments and analysis
scripts/       Utility scripts
tests/         Unit, integration and API tests
docs/          Project documentation
