# Master's Research Proposal

## Explainable Fraud Detection for Digital Payments
### A Temporal Comparison of Tabular and Heterogeneous Graph Models

**Program:** Master's in Data Science / Engineering  
**Student:** [Student name]  
**Advisor:** [Advisor name]  
**Institution:** [Institution name]  
**Date:** October 2026  
**Status:** Draft for advisor review; not approved

<!-- PAGEBREAK -->

## Contents

1. Abstract  
2. Introduction and Background  
3. Problem Statement  
4. Aim, Objectives, and Research Questions  
5. Related Work  
6. Methodology  
7. Expected Outcomes and Significance  
8. Ethics, Data Governance, and Limitations  
9. Research Plan  
10. References

<!-- PAGEBREAK -->

## 1. Abstract

Digital payments are increasingly important to Cambodia's financial ecosystem. As use of mobile banking, QR payments, and interoperable services grows, payment providers must identify suspicious activity among a much larger volume of legitimate transactions. Rule-based monitoring is transparent but can miss evolving patterns or generate too many alerts. Machine-learning models can learn more complex patterns, but fraud labels are rare and high-performing models may be difficult for investigators to interpret.

This study proposes a reproducible comparison of conventional tabular classifiers and a relation-aware heterogeneous GraphSAGE model for transaction fraud detection. Logistic Regression, Random Forest, XGBoost, and LightGBM will provide tabular baselines. The graph model will represent transactions and available card/device entities and their relationships. Experiments will use the IEEE-CIS Fraud Detection dataset, subject to its competition terms. This is an anonymized benchmark dataset, not Cambodian payment data; Cambodia provides the application motivation, not the empirical source of the study.

The data will be evaluated chronologically. Preprocessing and feature construction will use past information only, and the final temporal test set will remain untouched during model selection. Average precision / PR-AUC and recall at a fixed review capacity will be primary metrics, with ROC-AUC, precision, calibration, and inference latency reported as secondary measures. SHAP will explain tabular predictions; graph explanations will be evaluated with a graph-appropriate method. The intended contribution is evidence about whether relational information improves fraud ranking and whether its explanations and runtime are useful for a prototype.

**Keywords:** payment fraud, temporal validation, class imbalance, heterogeneous graphs, GraphSAGE, explainable AI, SHAP

## 2. Introduction and Background

Digital payment systems can reduce friction in everyday commerce and improve access to financial services. Cambodia's payment ecosystem, including Bakong and KHQR, provides the local context for this research. Increased digital activity also creates opportunities for scams and suspicious transfers. A monitoring system must distinguish unusual behavior from legitimate variation while limiting the number of alerts requiring human review.

Many operational monitoring systems begin with fixed rules, such as an amount threshold or a maximum number of transactions in a time interval. Rules can be audited and explained, but each new behavior may require manual updates. Statistical and machine-learning methods can combine multiple transaction attributes and learn patterns from labeled examples. The evaluation problem is difficult: in fraud datasets, legitimate transactions greatly outnumber fraudulent ones, and transaction behavior can change over time.

Interpretability matters because a risk score is not necessarily an adequate reason to block or investigate a payment. Investigators need to understand which attributes or historical relationships influenced an alert. This proposal therefore treats model discrimination, alert workload, temporal reliability, and explanation quality as related evaluation concerns.

The empirical study will use the IEEE-CIS Fraud Detection competition data. It contains anonymized transaction fields and a separate identity table, with an `isFraud` label for the competition's training records. It is suitable for a reproducible benchmark comparison, but it does not establish performance on Cambodia's domestic payment channels. Any local deployment claim would require authorized, appropriately anonymized Cambodian data and separate validation.

## 3. Problem Statement

A fraud-detection system faces three connected challenges. First, suspicious examples are uncommon, so a classifier that predicts nearly every transaction as legitimate can appear accurate while missing most fraud. Second, temporal drift means that a model evaluated on randomly mixed records may benefit from patterns that would not have been available when scoring future transactions. Third, transaction-level tabular models may not fully represent links among repeated cards, devices, and transactions, while graph models can be harder to train, explain, and serve efficiently.

The proposed research will address these challenges with a controlled temporal comparison. Tabular baselines and a heterogeneous graph model will use the same labeled benchmark, temporal cutoff, and primary evaluation metrics. The study will examine whether relation-aware learning improves the prioritization of suspicious transactions, whether this result holds under a realistic alert budget, and what explanations can be provided to an investigator. It will not assume that a graph model is better; a result showing no improvement will also be reported.

## 4. Aim, Objectives, and Research Questions

### Aim

To evaluate whether heterogeneous transaction relationships improve explainable, time-aware fraud detection compared with strong tabular baselines, using a public benchmark and a prototype architecture motivated by Cambodia's digital-payment context.

### Objectives

1. Prepare the IEEE-CIS transaction and identity records with documented validation, missingness, and a chronological train/test split.
2. Establish Logistic Regression, Random Forest, XGBoost, and LightGBM baselines with leakage-safe preprocessing.
3. Construct a heterogeneous graph from transaction, card, and device entities that are actually available and sufficiently reliable in the dataset.
4. Evaluate class-weighted training and, where appropriate, resampling within training data only.
5. Compare tabular and graph models using ranking, alert-capacity, calibration, and latency measures.
6. Produce global and local explanations using SHAP for tabular models and a graph-appropriate explanation approach for the graph model.
7. Demonstrate the selected model in a prototype using the repository's FastAPI, PostgreSQL, Redis, and Vue stack, without presenting the prototype as a production payment service.

### Research Questions

- **RQ1:** Does relation-aware heterogeneous GraphSAGE improve PR-AUC or recall at a fixed review capacity over tabular baselines on a later-time holdout?
- **RQ2:** Which transaction attributes and entity relationships contribute most to the models' suspicious-transaction scores?
- **RQ3:** How do class-weighting and suitable resampling strategies affect PR-AUC, precision, and recall under temporal evaluation?
- **RQ4:** What are the trade-offs among detection performance, explanation usefulness, and inference latency?

### Working Hypotheses

- **H1:** Historical transaction-to-card/device relationships may improve ranking over tabular features alone, but the improvement may be small or absent.
- **H2:** Class-imbalance handling will change the precision/recall trade-off; its value will be assessed at fixed alert budgets rather than accuracy alone.
- **H3:** Explanation methods can identify useful model drivers, but explanation quality and stability must be evaluated rather than assumed.

## 5. Related Work

### 5.1 Tabular fraud models

Logistic Regression provides an interpretable linear baseline. Random Forests model nonlinear interactions using ensembles of decision trees [1]. Gradient boosting methods such as XGBoost and LightGBM are effective for structured data and will serve as stronger tabular comparators [2, 3]. A fair comparison requires identical time splits and train-only preprocessing, not a random split selected separately for each model.

### 5.2 Class imbalance and evaluation

When positive cases are rare, accuracy can conceal poor fraud recall. Precision-recall analysis is informative for rare-event detection because it directly relates the fraction of alerts that are correct to the fraction of fraud cases found. The study will report PR-AUC / average precision and recall at a specified review capacity, alongside ROC-AUC for comparison. SMOTE is a widely used minority oversampling technique [4], but synthetic samples can distort mixed categorical and temporal data. It will therefore be treated as a controlled training-only experiment, with class weighting as a simpler baseline.

### 5.3 Graph learning and explanations

GraphSAGE learns node representations by aggregating information from sampled neighborhoods, supporting inductive inference on newly observed nodes [5]. A heterogeneous transaction graph adds distinct node and relation types, such as transactions linked to card or device entities. The implementation must preserve relation meaning and must not let future transactions or labels leak into historical neighborhoods. GNNExplainer provides a method for identifying influential subgraphs and features for graph predictions [6]. For tabular models, SHAP assigns feature contributions to predictions using a unified additive explanation framework [7]. Explanations will be treated as model diagnostics, not causal evidence.

## 6. Methodology

### 6.1 Research design

This is a quantitative, comparative machine-learning study using an anonymized benchmark. All candidate models will use a common temporal evaluation protocol. Hyperparameters and thresholds will be selected using only training-period validation data. The final later-period test set will be used once for the principal comparison.

### 6.2 Dataset and permissions

The study will use the IEEE-CIS Fraud Detection competition's transaction and identity training files. In the current workspace, the transaction table contains 590,540 rows and the identity table contains 144,233 rows. The tables are joined on `TransactionID`; identity data is absent for many transactions and that absence will be retained as a feature. The competition rules permit non-commercial academic research and education while restricting redistribution of the competition data. Raw CSVs will remain private, and publications will present methods and aggregate results rather than redistribute records.

This benchmark is not a sample of Cambodia's Bakong, KHQR, or mobile-banking transactions. The study can be motivated by Cambodia's needs, but its findings will be described as benchmark results. Local validity requires future access to authorized local data and an appropriate ethics/data-governance review.

### 6.3 Cleaning and preprocessing

The current pipeline normalizes column names, removes exact duplicate rows, validates required identifiers and labels, checks transaction-ID uniqueness, and performs a left join from transactions to identity records. It derives log transaction amount, a relative hour bin, a relative elapsed day, and an identity-match flag. `TransactionDT` is an elapsed-time field with an arbitrary reference origin; derived values will not be described as local clock time or calendar date.

Missingness will be profiled before treatment. Missing numeric and categorical values will be handled inside each model pipeline, with imputers fit on training data only. Categorical encoders will tolerate unseen values in validation/test. Identifiers used to build graph edges will be handled separately from model features to avoid accidental target leakage. Target label `isFraud` will never be used as an input feature or to build future graph context.

### 6.4 Temporal split and leakage controls

The dataset will be sorted by `TransactionDT`. The earliest approximately 80 percent of the time-ordered records will be used for model development and the latest approximately 20 percent will be held out for final testing. Records tied at the cutoff timestamp will remain on the same side, so the realized row ratio may differ slightly from exactly 80/20. The current export contains 472,432 training rows and 118,108 test rows, with the maximum train timestamp earlier than the minimum test timestamp.

A further chronological validation slice will be taken from the training period for model and threshold selection. Imputation, encoding, resampling, behavioral aggregates, and graph neighborhoods will be fitted or constructed using only information available before the relevant prediction time. This prevents the test set from influencing feature preparation or model selection.

### 6.5 Behavioral and relational feature engineering

Candidate tabular predictors include transaction amount and its logarithm, relative time features, available product/card/device categories, and identity availability. Behavioral aggregates such as prior transaction count, prior mean amount, amount deviation, or time since prior activity will be added only when they can be computed using strictly earlier records for each entity. The feature list will be documented, and high-cardinality or sparsely observed identifiers will be assessed before inclusion.

The graph will represent transaction nodes and, where reliable, anonymized card and device entity nodes. Edges will encode observed relations such as transaction-to-card and transaction-to-device. Entity keys, node counts, edge coverage, and missing-identifier behavior will be reported. A temporal graph for a transaction will include only historical context available at its scoring time; the label and future interactions will not be exposed to message passing.

### 6.6 Models and imbalance handling

The tabular comparison will include Logistic Regression, Random Forest, XGBoost, and LightGBM. Preprocessing and model hyperparameters will be tuned on the training-period validation slice. Class weighting will be tested as the primary imbalance treatment. Resampling such as SMOTE or SMOTENC may be evaluated only inside training folds and only where its assumptions are appropriate for the selected feature types.

The graph experiment will use a relation-aware heterogeneous GraphSAGE model, implemented with a suitable graph-learning library. It will combine transaction attributes with sampled historical neighborhoods. The architecture, relation definitions, sampling depth, training objective, and parameter count will be recorded. If a reliable graph cannot be built from the available identifiers, that limitation will be reported and the graph objective revised with advisor input rather than forcing unsupported edges.

### 6.7 Explainability

SHAP explanations will be generated for selected tabular models to summarize global feature contributions and explain individual high-scoring cases. For the graph model, a graph-specific explainer such as GNNExplainer will be tested to identify influential neighboring nodes, edges, and features. Explanations will be checked for stability across representative examples and clearly labeled as explanations of model behavior, not reasons that a transaction is objectively fraudulent.

### 6.8 Evaluation

PR-AUC / average precision will be the primary ranking metric because precision-recall analysis is informative for rare positive classes [8]. Operationally relevant measures will include recall@top-1% and precision@top-1%, where the highest-scored one percent represents a fixed analyst review budget. ROC-AUC, F1 at a validation-selected threshold, class-specific confusion counts, and calibration will be secondary measures. Metrics will be reported on the same temporal test set for all models, with repeated seeds or uncertainty intervals where computationally feasible.

Inference latency will be measured separately for model-only and end-to-end prototype scoring, with hardware and batch size documented. The planned sub-30 ms target is an engineering target, not a guaranteed outcome. Performance, explanation cost, and alert workload will be considered together when selecting a prototype model.

### 6.9 Prototype

The repository provides a FastAPI backend, PostgreSQL schema, Redis service, and Vue dashboard scaffold. After model evaluation, the selected model may be integrated behind an API endpoint. PostgreSQL will support transaction and prediction records; Redis may cache short-lived context or support low-latency access. The prototype will use synthetic or authorized demonstration transactions only. It will not connect to live payment rails or make automatic blocking decisions.

## 7. Expected Outcomes and Significance

The study is expected to produce a cleaned, time-split benchmark; reproducible tabular and graph baselines; comparative performance and alert-capacity results; and model explanations suitable for investigation. The graph model may improve, match, or underperform tabular models. Each outcome is useful if evaluation is fair and the limitations are stated.

Academic value comes from assessing relational learning under temporal evaluation rather than relying only on random splits. Practical value comes from relating model scores to a fixed review capacity and explaining the factors behind alerts. Cambodian relevance is motivational and contextual: the work can inform later locally grounded research, but it cannot establish performance for Cambodian payment providers without representative authorized data.

## 8. Ethics, Data Governance, and Limitations

The IEEE-CIS data is anonymized competition data, but it remains governed by its competition terms. It will be used for non-commercial academic research; raw records will not be committed to source control, included in public appendices, or redistributed. The repository's data-handling rules will be followed. If Cambodian institutional or provider data is considered later, collection and use will require prior authorization, appropriate anonymization, security controls, and institutional ethics approval.

Principal limitations include the age and domain of the benchmark, anonymized features, potential distribution shift, incomplete identity records, uncertainty in entity relationships, and the gap between an offline prototype and production payment systems. Class imbalance and concept drift may affect measured performance. Graph explanations may not be stable or readily actionable. The study will not claim a reduction in real-world losses based only on offline metrics.

## 9. Research Plan

| Period | Activities | Deliverable |
|---|---|---|
| October 2026 | Finalize proposal; dataset setup, EDA, Docker/database environment, cleaning and temporal exports | Approved proposal; reproducible data pipeline |
| November 2026 | Train and tune Logistic Regression, Random Forest, XGBoost, and LightGBM; define graph schema | Tabular baseline report and graph design |
| December 2026 | Implement temporal heterogeneous GraphSAGE and imbalance experiments | Trained graph model and experiment logs |
| January 2027 | SHAP/GNN explanations, error analysis, latency tests, manuscript drafting | Comparative results and paper draft |
| February 2027 | Advisor revisions and submission preparation | Research paper submitted, subject to advisor approval |
| March-April 2027 | Write thesis chapters and integrate system prototype | Complete thesis draft |
| May 2027 | Incorporate advisor and reviewer feedback | Revised thesis and manuscript |
| June-July 2027 | Final submission, presentation, and defense preparation | Thesis defense and final project demonstration |

## 10. References

[1] L. Breiman, “Random Forests,” *Machine Learning*, vol. 45, pp. 5-32, 2001. https://doi.org/10.1023/A:1010933404324.

[2] T. Chen and C. Guestrin, “XGBoost: A Scalable Tree Boosting System,” in *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 2016, pp. 785-794. https://doi.org/10.1145/2939672.2939785.

[3] G. Ke et al., “LightGBM: A Highly Efficient Gradient Boosting Decision Tree,” in *Advances in Neural Information Processing Systems 30*, 2017.

[4] N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, “SMOTE: Synthetic Minority Over-sampling Technique,” *Journal of Artificial Intelligence Research*, vol. 16, pp. 321-357, 2002. https://doi.org/10.1613/jair.953.

[5] W. L. Hamilton, R. Ying, and J. Leskovec, “Inductive Representation Learning on Large Graphs,” in *Advances in Neural Information Processing Systems 30*, 2017.

[6] R. Ying et al., “GNNExplainer: Generating Explanations for Graph Neural Networks,” in *Advances in Neural Information Processing Systems 32*, 2019.

[7] S. M. Lundberg and S.-I. Lee, “A Unified Approach to Interpreting Model Predictions,” in *Advances in Neural Information Processing Systems 30*, 2017.

[8] J. Davis and M. Goadrich, “The Relationship Between Precision-Recall and ROC Curves,” in *Proceedings of the 23rd International Conference on Machine Learning*, 2006, pp. 233-240. https://doi.org/10.1145/1143844.1143874.

[9] Kaggle, “IEEE-CIS Fraud Detection Competition: Rules and Data,” 2019. https://www.kaggle.com/competitions/ieee-fraud-detection/rules. Accessed October 2026.

[10] National Bank of Cambodia, official materials on Bakong and KHQR. Exact report/page and publication date to be confirmed during the literature review.
