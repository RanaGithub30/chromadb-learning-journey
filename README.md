# Chroma Cloud getting started

This example stores a few documents in a Chroma Cloud collection and runs a
semantic query. It uses Python 3.13 and a project-local virtual environment.

## Set up

From this directory, in PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If you do not already have an active Chroma Cloud profile, authenticate:

```powershell
chroma login
```

Create and connect to the Cloud database:

```powershell
chroma db create chroma-getting-started
chroma db connect chroma-getting-started --env-file
```

The connect command writes the Cloud credentials to `.env`. Keep this file
private; it is excluded from version control.

## Run

```powershell
python main.py
```

The script upserts three example documents into the `getting-started`
collection, queries for semantically similar text, and prints the ingested
documents, query, and matches. It does not delete collection data. Re-running
the script updates the same document IDs instead of adding duplicates.
