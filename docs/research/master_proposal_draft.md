# Master's Research Proposal

**Status:** Draft for advisor review  
**Working title:** Temporal Credit-Card Fraud Detection with Heterogeneous Graph Neural Networks  
**Student:** [Student name]  **Advisor:** [Advisor name]  **Date:** October 2026

## Problem and Rationale

Credit-card fraud detection is difficult because fraudulent transactions are rare, behavior changes over time, and an individual transaction may be hard to assess without its relationships to cards, devices, and other transactions. Tabular classifiers provide a strong and practical baseline, while graph models may capture relational patterns that ordinary feature-based models do not. This research will test whether those relationships improve detection on future transactions, under a time-ordered evaluation that better reflects deployment than a random split.

## Research Question

Under a temporal holdout, does a heterogeneous GraphSAGE model using transaction, card, and device relationships improve fraud-ranking performance over tuned XGBoost and LightGBM baselines, while remaining practical for low-latency scoring?

## Objectives and Method

1. Clean and join the IEEE-CIS transaction and identity records; document missingness and create a chronological 80/20 train-test split.
2. Train and tune XGBoost and LightGBM baselines using training data only.
3. Construct a heterogeneous graph from available transaction, card, and device attributes, with entity and edge definitions documented and checked for temporal leakage.
4. Train GraphSAGE with an imbalance-aware objective and compare it with the tabular baselines on the same untouched temporal test set.
5. Report PR-AUC, recall among the highest-scored 1% of transactions, precision at that review capacity, and inference latency. Analyze errors and limitations; do not select a model from test results and then report those results as unbiased.

## Expected Contribution and Scope

The intended contribution is a reproducible, time-aware comparison showing whether relational graph information adds measurable value for fraud triage on this dataset. A graph-model advantage is a hypothesis, not an assumed result. A FastAPI/Redis prototype and dashboard may demonstrate the selected model after evaluation, but operational readiness and sub-30 ms latency are targets to measure, not guarantees.

## Data Use and Approval

The IEEE-CIS Fraud Detection competition rules permit non-commercial academic research and education, while restricting redistribution of competition data. Raw CSVs will remain private; publications will report methods and aggregate results. The study will follow university requirements for data handling and advisor guidance.

**Advisor decision:** ☐ Approved  ☐ Revise  
**Comments:** ____________________________________________________________  
**Advisor signature:** ______________________________  **Date:** __________

**Dataset source:** [Kaggle IEEE-CIS Fraud Detection competition](https://www.kaggle.com/competitions/ieee-fraud-detection); competition rules reviewed October 2026.