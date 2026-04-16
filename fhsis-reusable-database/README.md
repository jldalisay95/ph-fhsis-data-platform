# fhsis-reusable-database

Scaffold for source registration, extraction, normalization, canonical modeling, and marts.

Layer boundary rule:
- `raw` -> `extract` -> `models/bronze` -> `models/silver` -> `models/gold`
