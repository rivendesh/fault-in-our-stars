# 567 Machine Learning Project - Spring 2026

- [567 Machine Learning Project - Spring 2026](#567-machine-learning-project---spring-2026)
  - [Introduction](#introduction)
  - [Proposed Project Flowchart](#proposed-project-flowchart)
- [Links \& References](#links--references)


## Introduction 

Project for CSCI 567 Machine Learning in Spring 2026 on light curve analysis of distant stars to detect exoplanets.

## Proposed Project Flowchart

```mermaid

flowchart TD

A["Raw Light Curve Data\n(Kepler / TESS)"]
--> B["Preprocessing\nCleaning, detrending, normalization"]

%% -------- Traditional Pipeline --------
B --> C

subgraph S1["Traditional + Feature-Based Pipeline"]
C["BLS\nDetect dips & extract features"]
--> D["XGBoost / Random Forest\nClassify transit vs non-transit"]
end

%% -------- Deep Learning Pipeline --------
B --> E

subgraph S2["Time-Series ML Pipeline"]
E["Raw Light Curve Input"]
--> F["CNN / LSTM / TCN\nDetect transit patterns"]
end

%% -------- Merge --------
D --> G["Candidate Transit Events"]
F --> G

%% -------- Optional Localization --------
G --> H

subgraph S3["Transit Localization (Optional)"]
H["U-Net / TCN\nLabel transit start & end"]
end

%% -------- Parameter Estimation --------
H --> I

subgraph S4["Parameter Estimation"]

I["Physical Model\nMandel & Agol\nFit & estimate parameters"]

I --> J["ML Regression (Optional)\nPredict planet properties"]

end

%% -------- Evaluation --------
J --> K

subgraph S5["Evaluation & Analysis"]
K["Metrics:\nPrecision, Recall, ROC\nRMSE, MAE\nFeature importance\nInjection tests"]
end

%% -------- Final Output --------
K --> L["Final Results\nDetected planets\nEstimated properties"]

```

# Links & References

> [!NOTE]
> 1. [NASA EXP Archives](https://exoplanetarchive.ipac.caltech.edu/index.html)
> 2. [MAST Landing Page](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html)
> 3. [MAST Notebook Repo](https://spacetelescope.github.io/mast_notebooks/notebooks/GALEX/mis_mosaic/mis_mosaic.html#about-this-notebook)
> 4. [Beginner Introductory Notebooks for `Lightkurve`](https://spacetelescope.github.io/mast_notebooks/notebooks/Kepler/beginner.html)
> 5. [Getting and Processing `Lightkurve` data](https://spacetelescope.github.io/mast_notebooks/notebooks/Kepler/lightkurve_analyzing_lc_products/lightkurve_analyzing_lc_products.html)
> 6. [Kaggle Notebook on Exoplanet Detection with CNNs](https://www.kaggle.com/code/huyghens/ai-model-for-the-detection-of-exoplanets/notebook#Future-work)
