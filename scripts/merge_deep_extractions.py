#!/usr/bin/env python3
import re
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.resolve()
DESKTOP_DIR = Path("/Users/jiawei/Desktop")

# File paths
DIABETES_DRAFT = DESKTOP_DIR / "Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues. 2024.deep extract.md"
HCM_076_DRAFT = DESKTOP_DIR / "*Left Atrioventricular Coupling Index in Feline Hypertrophic   Cardiomyopathy: Association with Disease Severity and Arterial   Thromboembolism.* 2026.  deep extract.md"
HCM_205_DRAFT = DESKTOP_DIR / "Prevalence of Hypertrophic Cardiomyopathy and ALMS1 Variant in Sphynx Cats in New Zealand deep extract.md"

TARGET_DIABETES = VAULT_ROOT / "raw" / "deep-extractions" / "ext-src-diabetes-025.md"
TARGET_HCM_076 = VAULT_ROOT / "raw" / "deep-extractions" / "ext-src-hcm-076.md"
TARGET_HCM_205 = VAULT_ROOT / "raw" / "deep-extractions" / "ext-src-hcm-205.md"
TARGET_FIP_031 = VAULT_ROOT / "raw" / "deep-extractions" / "ext-src-fip-031.md"
TARGET_HCM_SPHINX = VAULT_ROOT / "raw" / "deep-extractions" / "ext-src-hcm-sphinx.md"

def clean_content(text: str) -> str:
    """Clean ResearchGate tracking parameters and adjust headers for regex matching."""
    # Remove ?utm_source=chatgpt.com and similar tracking params from URLs
    text = re.sub(r'\?utm_source=[a-zA-Z0-9.-]+', '', text)
    
    # Standardize Phase 2 & Phase 3 headers so they match the deep_extraction.py regex:
    # Phase 2 regex: r"#\s*Phase\s*2[：:]\s*论点-?论据提炼"
    text = re.sub(r'#\s*(?:[一二三四五六七八九十百]+、)?\s*Phase\s*2[：:]\s*论点[—－-]论据提炼', '# Phase 2：论点-论据提炼', text)
    # Phase 3 regex: r"#\s*Phase\s*3[：:]\s*自检发现"
    text = re.sub(r'#\s*(?:[一二三四五六七八九十百]+、)?\s*Phase\s*3[：:]\s*自检发现.*', '# Phase 3：自检发现', text)
    # One-line summary regex: r"#\s*一句话总结"
    text = re.sub(r'#\s*(?:[一二三四五六七八九十百]+、)?\s*一句话(?:准确复述这篇论文|总结)', '# 一句话总结', text)
    text = re.sub(r'#\s*最终压缩版结论', '# 一句话总结', text)
    
    return text

def merge_diabetes():
    print("Merging Diabetes-025...")
    content = DIABETES_DRAFT.read_text(encoding="utf-8")
    content = clean_content(content)
    
    # Build YAML frontmatter
    fm = """---
id: ext-src-diabetes-025
tier: deep
source_id: src-diabetes-025
title: "Feline Diabetes Is Associated with Deficits in Markers of Insulin Signaling in Peripheral Tissues"
title_zh: "猫糖尿病与外周组织胰岛素信号标志物缺失相关"
journal: "Int J Mol Sci"
year: 2024
doi: "10.3390/ijms252313195"
pmid: "39684832"
pmcid: "PMC11642086"
url: "https://doi.org/10.3390/ijms252313195"
diseases: [diabetes]
study_type: "观察性队列研究"
sample: "54只家猫（瘦猫15, 超重15, 糖尿病24）"
evidence_nodes: [insulin-resistance, incretin-signaling, ectopic-lipid, GLUT-4, GLP-1R]
tensions_with: []
supports: []
extraction_date: "2026-06-22"
---

"""
    # Remove original document title header if it exists
    content_lines = content.splitlines()
    if content_lines and "Feline Diabetes" in content_lines[0]:
        # skip title lines
        start_idx = 0
        while start_idx < len(content_lines) and (not content_lines[start_idx].strip() or "Feline Diabetes" in content_lines[start_idx] or "URL:" in content_lines[start_idx] or "深度提炼" in content_lines[start_idx]):
            start_idx += 1
        content = "\n".join(content_lines[start_idx:])

    TARGET_DIABETES.write_text(fm + content.strip() + "\n", encoding="utf-8")
    print("Diabetes-025 merged successfully.")

def merge_hcm_076():
    print("Merging HCM-076...")
    content = HCM_076_DRAFT.read_text(encoding="utf-8")
    content = clean_content(content)
    
    # Fix the OR = 6.8 facts to OR = 4.65
    content = content.replace("OR = 6.8", "OR = 4.65 (95% CI: 1.405–29.215, p = 0.020)")
    content = content.replace("OR=6.8", "OR = 4.65 (95% CI: 1.405–29.215, p = 0.020)")
    content = content.replace("OR：6.8", "OR = 4.65 (95% CI: 1.405–29.215, p = 0.020)")
    content = content.replace("OR: 6.8", "OR = 4.65 (95% CI: 1.405–29.215, p = 0.020)")
    content = content.replace("OR是6.8", "OR是4.65")
    
    # Build YAML frontmatter
    fm = """---
id: ext-src-hcm-076
tier: deep
source_id: src-hcm-076
title: "Left Atrioventricular Coupling Index in Feline Hypertrophic Cardiomyopathy: Association with Disease Severity and Arterial Thromboembolism"
title_zh: "猫肥厚型心肌病中的左房室耦合指数：与疾病严重程度和动脉血栓栓塞的关系"
journal: "Vet Sci"
year: 2026
doi: "10.3390/vetsci13050491"
pmid: "42188963"
pmcid: ""
url: "https://doi.org/10.3390/vetsci13050491"
diseases: [hcm]
study_type: "回顾性横断面研究"
sample: "91只猫"
evidence_nodes: [LACI-ED, FATE, cardiac-remodeling, severity-marker]
tensions_with: []
supports: []
extraction_date: "2026-06-22"
---

"""
    # Remove original document title header if it exists
    content_lines = content.splitlines()
    if content_lines and "Left Atrioventricular" in content_lines[0] or "vetsci" in content_lines[0] or "vetsci" in content_lines[1] or "vetsci" in content_lines[2]:
        start_idx = 0
        while start_idx < len(content_lines) and (not content_lines[start_idx].strip() or "Left Atrioventricular" in content_lines[start_idx] or "Cardiomyopathy:" in content_lines[start_idx] or "Thromboembolism.*" in content_lines[start_idx] or "URL:" in content_lines[start_idx] or "处理" in content_lines[start_idx]):
            start_idx += 1
        content = "\n".join(content_lines[start_idx:])

    TARGET_HCM_076.write_text(fm + content.strip() + "\n", encoding="utf-8")
    print("HCM-076 merged successfully.")

def merge_hcm_205():
    print("Merging HCM-205...")
    content = HCM_205_DRAFT.read_text(encoding="utf-8")
    content = clean_content(content)
    
    # Ensure correct prevalence is supported
    content = content.replace("20/55", "22/55")
    content = content.replace("20 out of 55", "22 out of 55")
    
    # Build YAML frontmatter
    fm = """---
id: ext-src-hcm-205
tier: deep
source_id: src-hcm-205
title: "Prevalence of Hypertrophic Cardiomyopathy and ALMS1 Variant in Sphynx Cats in New Zealand"
title_zh: "新西兰斯芬克斯猫肥厚型心肌病患病情况及 ALMS1 变异分布"
journal: "Animals"
year: 2024
doi: "10.3390/ani14182629"
pmid: "39335607"
pmcid: "PMC11426466"
url: "https://doi.org/10.3390/ani14182629"
diseases: [hcm]
study_type: "前瞻性、单队列、重复超声心动图筛查研究"
sample: "55只斯芬克斯猫"
evidence_nodes: [prevalence, ALMS1, myocardial-ischemia, Sphynx]
tensions_with: []
supports: []
extraction_date: "2026-06-22"
---

"""
    # Remove original document title header if it exists
    content_lines = content.splitlines()
    if content_lines and "Prevalence of" in content_lines[0]:
        start_idx = 0
        while start_idx < len(content_lines) and (not content_lines[start_idx].strip() or "Prevalence of" in content_lines[start_idx] or "ALMS1" in content_lines[start_idx] or "mdpi.com" in content_lines[start_idx] or "论文深度提炼" in content_lines[start_idx]):
            start_idx += 1
        content = "\n".join(content_lines[start_idx:])

    TARGET_HCM_205.write_text(fm + content.strip() + "\n", encoding="utf-8")
    print("HCM-205 merged successfully.")

def update_fip_031():
    print("Updating FIP-031...")
    if TARGET_FIP_031.exists():
        content = TARGET_FIP_031.read_text(encoding="utf-8")
        # Ensure it has tier: deep
        if "tier:" not in content:
            # Insert tier: deep into frontmatter
            content = content.replace("source_id: src-fip-031", "id: ext-src-fip-031\ntier: deep\nsource_id: src-fip-031")
        
        # Clean tracking params
        content = clean_content(content)
        TARGET_FIP_031.write_text(content, encoding="utf-8")
        print("FIP-031 updated successfully.")

def update_hcm_sphinx():
    print("Updating HCM-Sphinx...")
    if TARGET_HCM_SPHINX.exists():
        content = TARGET_HCM_SPHINX.read_text(encoding="utf-8")
        # Build YAML frontmatter if missing
        if not content.startswith("---"):
            fm = """---
id: ext-src-hcm-sphinx
tier: lite
source_id: src-hcm-205
title: "Prevalence of Hypertrophic Cardiomyopathy and ALMS1 Variant in Sphynx Cats in New Zealand"
title_zh: "新西兰斯芬克斯猫肥厚型心肌病患病情况及 ALMS1 变异分布"
journal: "Animals"
year: 2024
doi: "10.3390/ani14182629"
pmid: "39335607"
pmcid: "PMC11426466"
url: "https://doi.org/10.3390/ani14182629"
diseases: [hcm]
study_type: "前瞻性、单队列、重复超声心动图筛查研究"
sample: "55只斯芬克斯猫"
evidence_nodes: [prevalence, ALMS1, Sphynx]
tensions_with: []
supports: []
extraction_date: "2026-06-22"
---

"""
            content = fm + content
        content = clean_content(content)
        TARGET_HCM_SPHINX.write_text(content, encoding="utf-8")
        print("HCM-Sphinx updated successfully.")

if __name__ == "__main__":
    merge_diabetes()
    merge_hcm_076()
    merge_hcm_205()
    update_fip_031()
    update_hcm_sphinx()
    print("All tasks completed.")
