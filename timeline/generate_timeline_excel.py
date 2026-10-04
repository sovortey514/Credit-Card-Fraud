import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# -------------------------------------------------------------
# 1. Timeline Data Definition
# -------------------------------------------------------------
timeline_data = [
    # Phase 1: Setup & Data Exploration
    {
        "Phase": "Phase 1: Setup & EDA",
        "Month": "October 2026",
        "Week": "Week 1",
        "Task Name": "Download IEEE-CIS Dataset & Setup Env",
        "Track": "Data Science",
        "Deliverable": "Raw CSVs loaded, Jupyter EDA Notebook working",
        "Target Date": "2026-10-10",
        "Status": "In Progress"
    },
    {
        "Phase": "Phase 1: Setup & EDA",
        "Month": "October 2026",
        "Week": "Week 2",
        "Task Name": "Dockerized Stack & Database Initialization",
        "Track": "Software Eng",
        "Deliverable": "PostgreSQL & Redis running in Docker Compose",
        "Target Date": "2026-10-17",
        "Status": "Pending"
    },
    {
        "Phase": "Phase 1: Setup & EDA",
        "Month": "October 2026",
        "Week": "Week 3",
        "Task Name": "Data Cleaning & Temporal 80/20 Train-Test Split",
        "Track": "Data Science",
        "Deliverable": "clean_train.parquet & clean_test.parquet exported",
        "Target Date": "2026-10-24",
        "Status": "Pending"
    },
    {
        "Phase": "Phase 1: Setup & EDA",
        "Month": "October 2026",
        "Week": "Week 4",
        "Task Name": "Formal Proposal Sign-off with Advisor",
        "Track": "Academic",
        "Deliverable": "Approved 1-page Master's Proposal Document",
        "Target Date": "2026-10-31",
        "Status": "Pending"
    },

    # Phase 2: Model Training & Benchmarking
    {
        "Phase": "Phase 2: ML Engine",
        "Month": "November 2026",
        "Week": "Week 5-6",
        "Task Name": "Train Tabular Baselines (XGBoost & LightGBM)",
        "Track": "Data Science",
        "Deliverable": "Baseline PR-AUC & Recall@Top-1% results",
        "Target Date": "2026-11-14",
        "Status": "Pending"
    },
    {
        "Phase": "Phase 2: ML Engine",
        "Month": "November 2026",
        "Week": "Week 7-8",
        "Task Name": "Build & Train Heterogeneous GraphSAGE",
        "Track": "Data Science",
        "Deliverable": "PyG HeteroData trained with Focal Loss; beats baseline",
        "Target Date": "2026-11-28",
        "Status": "Pending"
    },

    # Phase 3: Real-Time Pipeline & Web Dashboard
    {
        "Phase": "Phase 3: Web App",
        "Month": "December 2026",
        "Week": "Week 9-10",
        "Task Name": "Export GNN to ONNX & Build Redis Subgraph Pipeline",
        "Track": "Software Eng",
        "Deliverable": "FastAPI endpoint with sub-30ms scoring latency",
        "Target Date": "2026-12-12",
        "Status": "Pending"
    },
    {
        "Phase": "Phase 3: Web App",
        "Month": "December 2026",
        "Week": "Week 11-12",
        "Task Name": "Build React Triage Dashboard & Live WebSocket Feed",
        "Track": "Frontend / UI",
        "Deliverable": "Interactive D3/Force-graph canvas & live alert triage",
        "Target Date": "2026-12-26",
        "Status": "Pending"
    },

    # Phase 4: Academic Paper Submission
    {
        "Phase": "Phase 4: Journal Submission",
        "Month": "January 2027",
        "Week": "Week 13-15",
        "Task Name": "Stress Testing & Paper Drafting (IEEE / ACM Format)",
        "Track": "Academic",
        "Deliverable": "8-10 page complete paper manuscript draft",
        "Target Date": "2027-01-23",
        "Status": "Pending"
    },
    {
        "Phase": "Phase 4: Journal Submission",
        "Month": "February 2027",
        "Week": "Week 16-17",
        "Task Name": "SUBMIT RESEARCH PAPER TO TARGET JOURNAL",
        "Track": "MILESTONE",
        "Deliverable": "Journal submission confirmation receipt",
        "Target Date": "2027-02-15",
        "Status": "CRITICAL"
    },

    # Phase 5: Thesis Book Writing
    {
        "Phase": "Phase 5: Thesis Writing",
        "Month": "March 2027",
        "Week": "Week 18-21",
        "Task Name": "Author Thesis Chapters 1 to 3 (Intro, Lit Review, Arch)",
        "Track": "Academic",
        "Deliverable": "First 40 pages of thesis draft submitted to advisor",
        "Target Date": "2027-03-31",
        "Status": "Pending"
    },
    {
        "Phase": "Phase 5: Thesis Writing",
        "Month": "April 2027",
        "Week": "Week 22-25",
        "Task Name": "Author Thesis Chapters 4 to 6 (Experiments, Discussion)",
        "Track": "Academic",
        "Deliverable": "Complete 70+ page thesis document compiled",
        "Target Date": "2027-04-30",
        "Status": "Pending"
    },
    {
        "Phase": "Phase 5: Thesis Writing",
        "Month": "May 2027",
        "Week": "Week 26-29",
        "Task Name": "Advisor Review Revisions & Journal Feedback Incorporation",
        "Track": "Academic",
        "Deliverable": "Revised pre-defense thesis manuscript",
        "Target Date": "2027-05-31",
        "Status": "Pending"
    },

    # Phase 6: Defense Preparation & Final Release
    {
        "Phase": "Phase 6: Final Defense",
        "Month": "June 2027",
        "Week": "Week 30-33",
        "Task Name": "Pre-Defense Submission & Presentation Slide Deck",
        "Track": "Academic",
        "Deliverable": "Formal thesis submission & 25-slide defense deck",
        "Target Date": "2027-06-25",
        "Status": "Pending"
    },
    {
        "Phase": "Phase 6: Final Defense",
        "Month": "July 2027",
        "Week": "Week 34-35",
        "Task Name": "ORAL MASTER'S THESIS DEFENSE",
        "Track": "MILESTONE",
        "Deliverable": "Oral presentation, live software demo, final degree signoff",
        "Target Date": "2027-07-15",
        "Status": "CRITICAL"
    }
]

# -------------------------------------------------------------
# 2. Build Formatted Excel Workbook via OpenPyXL
# -------------------------------------------------------------
wb = Workbook()

# Sheet 1: Master Timeline
ws = wb.active
ws.title = "Master Timeline"
ws.views.sheetView[0].showGridLines = True

# Title Block
ws.merge_cells("A1:H1")
title_cell = ws["A1"]
title_cell.value = "MASTER'S RESEARCH & ENGINEERING PROJECT TIMELINE (2026 - 2027)"
title_cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
title_cell.fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
title_cell.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[1].height = 40

# Column Headers
headers = ["Phase", "Month", "Week", "Task Name", "Track", "Deliverable", "Target Date", "Status"]
ws.append([])  # Blank row 2
ws.append(headers)  # Row 3
ws.row_dimensions[3].height = 26

header_fill = PatternFill(start_color="334155", end_color="334155", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
header_border = Border(bottom=Side(style="medium", color="0F172A"))

for col_idx in range(1, len(headers) + 1):
    cell = ws.cell(row=3, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = header_border

# Populate Data Rows
thin_border = Border(
    left=Side(style="thin", color="E2E8F0"),
    right=Side(style="thin", color="E2E8F0"),
    top=Side(style="thin", color="E2E8F0"),
    bottom=Side(style="thin", color="E2E8F0")
)

for row_idx, item in enumerate(timeline_data, start=4):
    row_values = [
        item["Phase"], item["Month"], item["Week"],
        item["Task Name"], item["Track"], item["Deliverable"],
        item["Target Date"], item["Status"]
    ]
    ws.append(row_values)
    ws.row_dimensions[row_idx].height = 22

    # Formatting per row
    is_milestone = item["Status"] == "CRITICAL"
    
    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=row_idx, column=col_idx)
        cell.font = Font(name="Calibri", size=10, bold=is_milestone)
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center")

        # Specific column alignments
        if col_idx in [2, 3, 5, 7, 8]:
            cell.alignment = Alignment(horizontal="center", vertical="center")

        # Milestone row styling
        if is_milestone:
            cell.fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
            if col_idx == 8:
                cell.font = Font(name="Calibri", size=10, bold=True, color="991B1B")
        elif item["Status"] == "In Progress" and col_idx == 8:
            cell.fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
            cell.font = Font(name="Calibri", size=10, bold=True, color="92400E")

# Auto-fit Column Widths cleanly
for col in ws.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

# Sheet 2: Quick Status Summary Card
ws_summary = wb.create_sheet(title="Milestone Summary")
ws_summary.views.sheetView[0].showGridLines = True

ws_summary.append(["Key Degree Milestones", "Target Deadline", "Deliverable Type"])
ws_summary.row_dimensions[1].height = 24
for col_idx in range(1, 4):
    cell = ws_summary.cell(row=1, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

summary_rows = [
    ["Proposal Sign-off", "October 31, 2026", "Approved Proposal Document"],
    ["Baseline ML Performance Verified", "November 28, 2026", "PR-AUC Benchmark Table"],
    ["System Architecture Prototype Ready", "December 26, 2026", "Sub-30ms API + React Dashboard"],
    ["Journal Paper Submission", "February 15, 2027", "8-10 Page Academic Manuscript"],
    ["Full Thesis Book Draft", "April 30, 2027", "Chapters 1-6 Master's Dissertation"],
    ["Master's Oral Defense", "July 15, 2027", "Oral Examination & Live System Demo"]
]

for r_idx, row in enumerate(summary_rows, start=2):
    ws_summary.append(row)
    ws_summary.row_dimensions[r_idx].height = 22
    for c_idx in range(1, 4):
        c = ws_summary.cell(row=r_idx, column=c_idx)
        c.font = Font(name="Calibri", size=10)
        c.border = thin_border
        if c_idx == 2:
            c.alignment = Alignment(horizontal="center", vertical="center")

for col in ws_summary.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws_summary.column_dimensions[col_letter].width = max_len + 5

# Save the workbook to disk
output_file = "Master_Thesis_Timeline_2026_2027.xlsx"
wb.save(output_file)
print(f"Excel file created: {output_file}")