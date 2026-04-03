# 567 Machine Learning Project - Spring 2026

- [567 Machine Learning Project - Spring 2026](#567-machine-learning-project---spring-2026)
  - [Introduction](#introduction)
  - [Combined Project Flowchart](#combined-project-flowchart)
  - [Links \& References](#links--references)

## Introduction

Project for CSCI 567 Machine Learning in Spring 2026 on light curve analysis of distant stars to detect exoplanets.

## Combined Project Flowchart

```mermaid
flowchart TD

%% LEFT SIDE

subgraph A["Multi-source ingestion"]
    style A stroke-dasharray: 5 5, stroke:#888
    A1["KOI / Villanova / MAST
Exoplanet, EB & variable catalogs"]
    A2["Combine datasets
Confirmed exoplanet / binary / variable / FP"]
    A1 --> A2
end

A2 --> B1["Raw light curve data
Kepler / TESS"]
B1 --> B2["Preprocessing
Clean, normalize"]

subgraph P1["Traditional"]
    style P1 stroke-dasharray: 5 5, stroke:#888
    C1["BLS
Detect dips"]
    C2["XGBoost / RF
Classify"]
    C1 --> C2
end

subgraph P2["Image-based"]
    style P2 stroke-dasharray: 5 5, stroke:#888
    D1["Fold & convert"]
    D2["Train CNN
Classifier"]
    D3["4-class out"]
    D1 --> D2 --> D3
end

subgraph P3["Time-series ML"]
    style P3 stroke-dasharray: 5 5, stroke:#888
    E1["Light curve
input"]
    E2["CNN / LSTM / TCN
Patterns"]
    E1 --> E2
end

B2 --> C1
B2 --> D1
B2 --> E1

C2 --> F1
D3 --> F1
E2 --> F1

F1["Candidate transit events
Merged from all pipelines"]

%% RIGHT SIDE

F1 --> G1

subgraph B["Parameter estimation"]
    style B stroke-dasharray: 5 5, stroke:#888
    G1["Physical model
Mandel & Agol transit fit"]
    G2["ML regression
Predict planet properties"]
    G1 --> G2
end

subgraph C["Evaluation & analysis"]
    style C stroke-dasharray: 5 5, stroke:#888
    H1["Detection metrics"]
    H2["Classification metrics"]
end

G2 --> H1
G2 --> H2

H1 --> I1
H2 --> I1

I1["Final results"]
I1 --> J1["Detected planets & objects
Classified types, estimated properties"]

%% COLOR STYLING

style A1 fill:#7a2e1c,color:#fff,stroke:#7a2e1c
style A2 fill:#7a2e1c,color:#fff,stroke:#7a2e1c

style B1 fill:#555,color:#fff,stroke:#555

style B2 fill:#0f5c4a,color:#fff,stroke:#0f5c4a

style C1 fill:#4b3f99,color:#fff,stroke:#4b3f99
style C2 fill:#4b3f99,color:#fff,stroke:#4b3f99

style D1 fill:#7a2e1c,color:#fff,stroke:#7a2e1c
style D2 fill:#7a2e1c,color:#fff,stroke:#7a2e1c
style D3 fill:#4b3f99,color:#fff,stroke:#4b3f99

style E1 fill:#1f4e79,color:#fff,stroke:#1f4e79
style E2 fill:#1f4e79,color:#fff,stroke:#1f4e79

style F1 fill:#0f5c4a,color:#fff,stroke:#0f5c4a

style G1 fill:#3b3486,color:#fff,stroke:#3b3486
style G2 fill:#3b3486,color:#fff,stroke:#3b3486

style H1 fill:#0f5c4a,color:#fff,stroke:#0f5c4a
style H2 fill:#7a2e1c,color:#fff,stroke:#7a2e1c

style I1 fill:#555,color:#fff,stroke:#555
style J1 fill:#555,color:#fff,stroke:#555
```

---

## Links & References

> [!NOTE]
>
> 1. [NASA EXP Archives](https://exoplanetarchive.ipac.caltech.edu/index.html)
> 2. [MAST Landing Page](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html)
> 3. [MAST Notebook Repo](https://spacetelescope.github.io/mast_notebooks/notebooks/GALEX/mis_mosaic/mis_mosaic.html#about-this-notebook)
> 4. [Beginner Introductory Notebooks for `Lightkurve`](https://spacetelescope.github.io/mast_notebooks/notebooks/Kepler/beginner.html)
> 5. [Getting and Processing `Lightkurve` data](https://spacetelescope.github.io/mast_notebooks/notebooks/Kepler/lightkurve_analyzing_lc_products/lightkurve_analyzing_lc_products.html)
> 6. [Kaggle Notebook on Exoplanet Detection with CNNs](https://www.kaggle.com/code/huyghens/ai-model-for-the-detection-of-exoplanets/notebook#Future-work)
> 7. [Kaggle Notebook AI Model for the Detection of Exoplanets](https://www.kaggle.com/code/jaimetrickz/exoplanet-classification/notebook#KNN-Classifier)
> 8. [Kepler Eclipsing Binary Catalog](https://keplerebs.villanova.edu/)
