# VIB-CCB-BioIT & AI Catalog of Tools & Pipelines

Everything developed or used in the center, in one place. Found something you need? Open the repository (if public) or **contact the person in charge** listed in the last column.

- Missing or wrong entry? See [CONTRIBUTING.md](CONTRIBUTING.md); it is a one-line edit of [`tools.yaml`](tools.yaml).
- Want it as a spreadsheet? Download [`catalog.csv`](catalog.csv).
- Want to hear about new releases? Join the Teams channel (link on the [organization page](https://github.com/VIB-CCB-BioIT)).

<!-- CATALOG:START -->
### Single-cell transcriptomics

| Name | What it does | Data / topic | Language | Status | Contact |
|---|---|---|---|---|---|
| Bartab | SPLINTR barcode processing, QC, annotation and clone identification. | SPLINTR barcodes · Any | Nextflow | Public | Ariel Pulido Vicuña (Pozniak) |
| [Pan-cancer downstream analysis (Lodi et al.)](https://github.com/lambrechtslab/Pan-cancer_Lodietal) | Downstream analysis, visualization and reporting for the pan-cancer scRNA-seq study. | scRNA-seq / snRNA-seq · Pan-cancer | R | Public | Tom Venken (Lambrechts) |
| Archetype analysis (name TBD) | Archetype analysis; description of continuous phenotypes. | scRNA-seq / snRNA-seq · Melanoma | Python (scanpy, squidpy) | In development | Axel Rodriguez Perez (Pozniak) |
| Colorectal cancer scRNA/snRNA pipeline (name TBD) | Preprocessing, QC, clustering, annotation and pathway analysis. | scRNA-seq / snRNA-seq · Colorectal cancer | bash, R | Internal – ask contact | Tom Venken (Lambrechts) |
| Drug repurposing from transcriptional changes (name TBD) | Prioritises drugs that induce transcriptional changes. | scRNA-seq / snRNA-seq · Melanoma | Python | In development | Axel Rodriguez Perez (Pozniak) |
| HCC / urogenital scRNA/snRNA pipeline (name TBD) | Preprocessing, QC, clustering, annotation, pathway analysis, CNV inference, single-cell SNP/mutation calling. | scRNA-seq / snRNA-seq · HCC / urogenital carcinoma | bash, R | Internal – ask contact | Gino Philips (Lambrechts) |
| Improved SoupX wrapper (name TBD) | Improved implementation of the SoupX method, packaged as a function. | scRNA-seq / snRNA-seq · Any (except one-cell-type datasets) | R (Seurat, SoupX) | Internal – ask contact | Juan Fernandez Garcia (Fendt) |
| Melanoma scRNA/snRNA pipeline (name TBD) | Preprocessing, QC and malignant-cell annotation. | scRNA-seq / snRNA-seq · Melanoma | Snakemake, R, Python | In development | Ariel Pulido Vicuña (Pozniak) |
| scRNA trajectory & cell-cell communication (name TBD) | QC, report and visualization for scRNA-seq with cell trajectories and cell-cell communication. | scRNA-seq / cell trajectory / cell-cell communication |  | Internal – ask contact | Fateme Safaeifard (CoSc) |

### Spatial omics

| Name | What it does | Data / topic | Language | Status | Contact |
|---|---|---|---|---|---|
| HCC / urogenital spatial transcriptomics pipeline (name TBD) | Preprocessing, QC, clustering, annotation, scRNA-seq integration. | Spatial transcriptomics · HCC / urogenital carcinoma | bash, R | Internal – ask contact | Gino Philips (Lambrechts) |
| Melanoma spatial transcriptomics pipeline (name TBD) | Preprocessing, QC, clustering and annotation. | Spatial transcriptomics · Melanoma | Python | Internal – ask contact | Georg Demaerel (Pozniak) |
| Spatial metabolomics / lipidomics pipeline (name TBD) | Aggregation over pre-defined spatial regions, normalization, statistics and ranking of altered metabolites (input exported from e.g. SCiLS). | Spatial metabolomics / lipidomics · Any | R | Internal – ask contact | Juan Fernandez Garcia (Fendt) |
| Spatial proteomics / multiplex imaging pipeline (name TBD) | Preprocessing, cell segmentation, background correction, QC, clustering and annotation. | Spatial proteomics / multiplex imaging · Urogenital carcinoma | bash, R | Internal – ask contact | Gino Philips (Lambrechts) |

### Long-read & DNA sequencing

| Name | What it does | Data / topic | Language | Status | Contact |
|---|---|---|---|---|---|
| [ASCAT.sc](https://github.com/ljwharbers/ASCAT.sc) | Copy number calling of (long-read) single-cell DNA sequencing. | Single-cell DNA · Not disease-specific (method) | R | Public | Luuk Harbers (Demeulemeester) |
| ASCAT.sc-explorer | Visualization and QC tool for single-cell copy number data. | Single-cell DNA · Not disease-specific (method) | JavaScript | Public | Harry (Charalampos Anagnost) (Demeulemeester) |
| [ggmethylation](https://github.com/ljwharbers/ggmethylation) | Visualization package for methylation plotting. | Long-read WGS · Not disease-specific (method) | R | Public | Luuk Harbers (Demeulemeester) |
| [Lrsomatic](https://github.com/IntGenomicsLab/lrsomatic) | Preprocessing, variant calling and QC of long-read WGS. | Long-read WGS · Pan-cancer | Nextflow | Public | Luuk Harbers (Demeulemeester) |
| nanoWGS | Preprocessing pipeline for nanopore WGS data. | Long-read WGS · Non-cancer disease | Nextflow | Public | Alexandra Pančíková (Demeulemeester) |
| [scnanoseq (fork)](https://github.com/ljwharbers/scnanoseq) | Preprocessing and QC of long-read single-cell DNA/RNA (forked nf-core pipeline). | Long-read single-cell DNA/RNA · Not disease-specific (method) | Nextflow | Public | Luuk Harbers (Demeulemeester) |
| ASCAT.sc rewrite (Rust/Python) | Speed-optimised rewrite of ASCAT.sc in Rust/Python. | Single-cell DNA · Not disease-specific (method) | Rust, Python | In development | Harry (Charalampos Anagnost) (Demeulemeester) |
| cfDNA fragmentomics pipeline (name TBD) | Fragmentomics analysis of cell-free DNA. | Cell-free DNA · Ovarian / gynaecological | Nextflow, bash, R | In development | Pieter Busschaert (Lambrechts) |
| Fibertron | Sequence-to-function model for downstream variant interpretation. | Long-read WGS | Python | Internal – ask contact | Marios Eftychiou (Demeulemeester) |

### Bulk RNA-seq & proteomics

| Name | What it does | Data / topic | Language | Status | Contact |
|---|---|---|---|---|---|
| Bulk RNA-seq end-to-end (name TBD) | End-to-end bulk RNA-seq analysis. | Bulk RNA-seq · Various |  | Internal – ask contact | Gino Philips (Lambrechts) |
| Bulk RNA-seq QC & report (name TBD) | QC, report and visualization for bulk RNA-seq. | Bulk RNA-seq |  | Internal – ask contact | Fateme Safaeifard (CoSc) |
| Longitudinal bulk RNA-seq (name TBD) | QC, analysis and visualization of longitudinal bulk RNA-seq. | Longitudinal bulk RNA-seq | R | Internal – ask contact | Fateme Safaeifard (CoSc) |
| Longitudinal proteomics (name TBD) | QC, analysis and visualization of longitudinal proteomics. | Longitudinal proteomics | R | Internal – ask contact | Fateme Safaeifard (CoSc) |
| Proteomics QC & analysis (name TBD) | QC, analysis and visualization of proteomics data. | Proteomics |  | Internal – ask contact | Fateme Safaeifard (CoSc) |

### Imaging & microscopy

| Name | What it does | Data / topic | Language | Status | Contact |
|---|---|---|---|---|---|
| [napari-fast4dreg](https://github.com/COSC-Lab/napari-fast4dreg) | Fast rigid registration for large volumetric time-lapse series. | Microscope volumetric time-series · Any | Python (dask, opencl, napari) | Public | Marcel Issler (CoSc) |
| 3D epithelial morphology reconstruction (name TBD) | Reconstructs 3D epithelial morphology from sequential H&E slides with variable spacing (here 20 µm); supports intermediate slices. | H&E (primary), multimodal (secondary) · Healthy breast and breast cancer | Python (dask, pytorch, napari) | In development | Marcel Issler (CoSc) |
| 5D-KTR-pipeline | Quantifies spatio-temporal kinase translocation dynamics (nuclear vs cytosolic signal), including segmentation and morphological features. | Kinase-translocation-sensor volumetric time-lapse · Various | Python (dask, napari) | In development | Marcel Issler (CoSc) |
| napari-nd-registration | Elastic nd-registration with dimension awareness; mainly breathing correction of 5D intravital measurements. | Intravital nd-stack · Any | Python (dask, opencl) | Internal – ask contact | Marcel Issler (CoSc) |

<!-- CATALOG:END -->
