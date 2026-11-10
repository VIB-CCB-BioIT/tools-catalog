# Adding or updating an entry

1. Edit [`tools.yaml`](tools.yaml) (GitHub's pencil icon works) and copy an existing entry:

   ```yaml
   - id: my-pipeline            # unique, lowercase, dashes
     name: My Pipeline
     category: Single-cell transcriptomics   # see the list in scripts/build_catalog.py
     summary: One line — input -> output.
     data: scRNA-seq
     step: End-to-end
     topic: Melanoma
     language: Nextflow
     status: internal           # public | internal | building
     repo: ""                   # GitHub URL once public
     contact: Your full name
     lab: Your lab
     share: yes
   ```

2. Open a pull request. A check validates the file; the tables in `README.md` and `catalog.csv` are rebuilt automatically on your pull request.

**Status meanings**

| Status | Use when |
|---|---|
| `public` | There is an open repository anyone can use. Please fill `repo`. |
| `internal` | It exists in the center but is not public (or the repo is private). Others can contact you. |
| `building` | In development. Listing it helps avoid duplicate work. |

**Local preview** (optional)

```bash
pip install pyyaml
python scripts/build_catalog.py
```

**Contact:** list the person in charge by full name, plus their lab or group. Do not add emails or phone numbers.
