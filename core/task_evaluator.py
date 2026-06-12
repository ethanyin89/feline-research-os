"""
Task Evaluator for research queries.

Based on II-Researcher query evaluation principles:
- Freshness: Does this need latest literature?
- Plurality: Does this need multiple sources?
- Completeness: Does this need full protocol structure?
- Species-specificity: Must be cat-only?

Assigns search depth and task type to guide the research pipeline.
"""

import re
from dataclasses import dataclass
from typing import List, Optional, Tuple

from .schemas import ResearchRecord, SearchDepth, TaskType


@dataclass
class TaskEvaluation:
    """Result of evaluating a research query."""
    task_type: TaskType
    search_depth: SearchDepth
    disease: str
    requires_freshness: bool
    requires_plurality: bool
    requires_completeness: bool
    species_strict: bool
    suggested_sources: List[str]
    subqueries: List[str]
    reasoning: str


class TaskEvaluator:
    """
    Evaluates research queries to determine task type and search depth.

    This is the first step in the research pipeline, ensuring
    that complex tasks get appropriate depth and simple queries
    don't waste resources.
    """

    # Disease keywords (bilingual)
    DISEASE_PATTERNS = {
        "fip": ["fip", "传染性腹膜炎", "feline infectious peritonitis", "猫传腹"],
        "ckd": ["ckd", "慢性肾病", "chronic kidney disease", "肾病", "renal"],
        "hcm": ["hcm", "肥厚型心肌病", "hypertrophic cardiomyopathy", "心肌病"],
        "fcgs": ["fcgs", "口炎", "feline chronic gingivostomatitis", "gingivostomatitis"],
        "diabetes": ["diabetes", "糖尿病", "dm", "diabetic"],
        "obesity": ["obesity", "肥胖", "overweight", "体重"],
        "fcv": ["fcv", "杯状病毒", "calicivirus", "feline calicivirus"],
        "ibd": ["ibd", "炎症性肠病", "inflammatory bowel disease"],
        "cancer": ["cancer", "肿瘤", "tumor", "neoplasia", "carcinoma", "lymphoma", "sarcoma"],
    }

    # Task type patterns
    PROTOCOL_PATTERNS = [
        r"方案", r"protocol", r"设计", r"design",
        r"how to design", r"怎么设计", r"研究方案",
        r"评分体系", r"如何构建", r"如何设定",
        r"约束", r"constraints",
    ]

    ENDPOINT_PATTERNS = [
        r"终点", r"endpoint", r"指标", r"biomarker",
        r"哪些指标", r"选择.*指标", r"评价指标",
        r"用途", r"应用", r"药效评价", r"角色",
        r"核心指标", r"读数指标", r"efficacy",
        r"在.*中的", r"ratio",
    ]

    LITERATURE_PATTERNS = [
        r"文献", r"literature", r"review", r"综述",
        r"找.*文献", r"查.*文献", r"研究进展",
    ]

    EXPLANATION_PATTERNS = [
        r"是什么", r"what is", r"解释", r"explain",
        r"什么是", r"定义", r"definition",
    ]

    MODEL_PATTERNS = [
        r"模型", r"model", r"造模", r"动物模型",
        r"animal model", r"disease model",
    ]

    PK_PATTERNS = [
        r"pk", r"pd", r"药代", r"药动",
        r"pharmacokinetic", r"采血", r"blood sampling",
        r"采样时间点", r"采样", r"时间点",
    ]

    def evaluate(self, query: str) -> TaskEvaluation:
        """
        Evaluate a research query.

        Args:
            query: User's research question

        Returns:
            TaskEvaluation with type, depth, and guidance
        """
        query_lower = query.lower()

        # Detect disease
        disease = self._detect_disease(query_lower)

        # Detect task type
        task_type = self._detect_task_type(query_lower)

        # Determine search depth based on task type
        search_depth = self._determine_search_depth(task_type, query_lower)

        # Evaluate dimensions
        requires_freshness = self._requires_freshness(query_lower, task_type)
        requires_plurality = self._requires_plurality(task_type)
        requires_completeness = self._requires_completeness(task_type)
        species_strict = self._is_species_strict(query_lower)

        # Suggest sources
        suggested_sources = self._suggest_sources(task_type, disease)

        # Generate subqueries
        subqueries = self._generate_subqueries(query, task_type, disease)

        # Build reasoning
        reasoning = self._build_reasoning(
            task_type, search_depth, requires_freshness,
            requires_plurality, requires_completeness, species_strict
        )

        return TaskEvaluation(
            task_type=task_type,
            search_depth=search_depth,
            disease=disease,
            requires_freshness=requires_freshness,
            requires_plurality=requires_plurality,
            requires_completeness=requires_completeness,
            species_strict=species_strict,
            suggested_sources=suggested_sources,
            subqueries=subqueries,
            reasoning=reasoning,
        )

    def _detect_disease(self, query_lower: str) -> str:
        """Detect disease from query."""
        for disease, patterns in self.DISEASE_PATTERNS.items():
            for pattern in patterns:
                if pattern in query_lower:
                    return disease
        return ""

    def _detect_task_type(self, query_lower: str) -> TaskType:
        """Detect task type from query patterns."""
        # Check patterns in order of specificity (most specific first)

        # Explicit audit language overrides the subject being audited.
        if any(
            kw in query_lower
            for kw in ["证据审查", "审查", "evidence audit", "验证", "verify"]
        ):
            return TaskType.EVIDENCE_CHECK

        # PK patterns first - "PK 采血设计" should match PK, not "设计"
        for pattern in self.PK_PATTERNS:
            if re.search(pattern, query_lower):
                return TaskType.PK_DESIGN

        # Model patterns before endpoint - "模型中指标" is model, not endpoint
        for pattern in self.MODEL_PATTERNS:
            if re.search(pattern, query_lower):
                return TaskType.MODEL_EVALUATION

        for pattern in self.PROTOCOL_PATTERNS:
            if re.search(pattern, query_lower):
                return TaskType.PROTOCOL_DESIGN

        for pattern in self.ENDPOINT_PATTERNS:
            if re.search(pattern, query_lower):
                return TaskType.ENDPOINT_SELECTION

        for pattern in self.LITERATURE_PATTERNS:
            if re.search(pattern, query_lower):
                return TaskType.LITERATURE_REVIEW

        for pattern in self.EXPLANATION_PATTERNS:
            if re.search(pattern, query_lower):
                return TaskType.QUICK_EXPLANATION

        # General evidence questions that did not match a more specific task.
        if any(kw in query_lower for kw in ["证据", "evidence"]):
            return TaskType.EVIDENCE_CHECK

        if any(kw in query_lower for kw in ["biomarker", "标志物"]):
            return TaskType.BIOMARKER_MAPPING

        return TaskType.OTHER

    def _determine_search_depth(self, task_type: TaskType, query_lower: str) -> SearchDepth:
        """Determine appropriate search depth based on task type."""
        # Simple explanations need minimal search
        if task_type == TaskType.QUICK_EXPLANATION:
            return SearchDepth.QUICK

        # Protocol design and endpoint selection need deep research
        if task_type in [TaskType.PROTOCOL_DESIGN, TaskType.ENDPOINT_SELECTION]:
            return SearchDepth.DEEP

        # Evidence checks need audit-level depth
        if task_type == TaskType.EVIDENCE_CHECK:
            return SearchDepth.EVIDENCE_AUDIT

        # PK design needs deep research
        if task_type == TaskType.PK_DESIGN:
            return SearchDepth.DEEP

        # Model evaluation needs standard depth
        if task_type == TaskType.MODEL_EVALUATION:
            return SearchDepth.STANDARD

        # Literature review depends on scope
        if task_type == TaskType.LITERATURE_REVIEW:
            # Check for comprehensive indicators
            if any(kw in query_lower for kw in ["系统", "systematic", "全面", "comprehensive"]):
                return SearchDepth.DEEP
            return SearchDepth.STANDARD

        return SearchDepth.STANDARD

    def _requires_freshness(self, query_lower: str, task_type: TaskType) -> bool:
        """Check if query requires latest literature."""
        # Explicit freshness indicators
        freshness_keywords = [
            "最新", "latest", "recent", "2024", "2025", "2026",
            "新药", "new drug", "进展", "advances", "更新",
        ]

        if any(kw in query_lower for kw in freshness_keywords):
            return True

        # Some task types inherently need fresh data
        if task_type in [TaskType.ENDPOINT_SELECTION, TaskType.BIOMARKER_MAPPING]:
            return True

        return False

    def _requires_plurality(self, task_type: TaskType) -> bool:
        """Check if task requires multiple sources."""
        # Most research tasks need multiple sources
        plurality_tasks = [
            TaskType.PROTOCOL_DESIGN,
            TaskType.ENDPOINT_SELECTION,
            TaskType.LITERATURE_REVIEW,
            TaskType.EVIDENCE_CHECK,
            TaskType.MODEL_EVALUATION,
            TaskType.PK_DESIGN,
        ]

        return task_type in plurality_tasks

    def _requires_completeness(self, task_type: TaskType) -> bool:
        """Check if task requires complete structured output."""
        completeness_tasks = [
            TaskType.PROTOCOL_DESIGN,
            TaskType.PK_DESIGN,
        ]

        return task_type in completeness_tasks

    def _is_species_strict(self, query_lower: str) -> bool:
        """Check if query must be restricted to cat evidence."""
        # By default, feline research is species-strict
        # Only relax if explicitly cross-species
        cross_species_keywords = [
            "跨物种", "cross-species", "犬猫", "dog and cat",
            "比较", "compare", "人类", "human",
        ]

        for kw in cross_species_keywords:
            if kw in query_lower:
                return False

        return True

    def _suggest_sources(self, task_type: TaskType, disease: str) -> List[str]:
        """Suggest appropriate sources for the task."""
        sources = []

        # Base sources for all research tasks
        if task_type != TaskType.QUICK_EXPLANATION:
            sources.append("internal_knowledge_base")

        # Literature tasks need external sources
        if task_type in [TaskType.LITERATURE_REVIEW, TaskType.EVIDENCE_CHECK]:
            sources.extend(["pubmed", "pmc"])

        # Protocol tasks need guidelines
        if task_type in [TaskType.PROTOCOL_DESIGN, TaskType.PK_DESIGN]:
            sources.extend(["guideline", "internal_protocol"])

        # Endpoint tasks need comprehensive sources
        if task_type == TaskType.ENDPOINT_SELECTION:
            sources.extend(["pubmed", "guideline", "internal_protocol"])

        # Add disease-specific sources
        if disease in ["fip", "ckd", "hcm"]:
            sources.append(f"internal_{disease}_models")

        return list(dict.fromkeys(sources))  # Remove duplicates, preserve order

    def _generate_subqueries(
        self, query: str, task_type: TaskType, disease: str
    ) -> List[str]:
        """Generate subqueries for comprehensive research."""
        subqueries = []

        if not disease:
            return subqueries

        # Task-specific subqueries
        if task_type == TaskType.PROTOCOL_DESIGN:
            subqueries = [
                f"feline {disease} disease definition and diagnostic criteria",
                f"feline {disease} animal model or natural case enrollment",
                f"feline {disease} efficacy endpoints",
                f"feline {disease} safety monitoring parameters",
                f"feline {disease} study design and statistical considerations",
            ]

        elif task_type == TaskType.ENDPOINT_SELECTION:
            subqueries = [
                f"feline {disease} diagnosis biomarkers",
                f"feline {disease} disease progression markers",
                f"feline {disease} treatment response indicators",
                f"feline {disease} safety monitoring parameters",
            ]

        elif task_type == TaskType.LITERATURE_REVIEW:
            subqueries = [
                f"feline {disease} pathophysiology mechanism",
                f"feline {disease} clinical presentation",
                f"feline {disease} treatment options",
                f"feline {disease} prognosis factors",
            ]

        elif task_type == TaskType.MODEL_EVALUATION:
            subqueries = [
                f"feline {disease} natural disease model",
                f"feline {disease} induced model methods",
                f"feline {disease} model validation criteria",
                f"feline {disease} model limitations",
            ]

        elif task_type == TaskType.PK_DESIGN:
            subqueries = [
                f"feline pharmacokinetic study blood sampling design",
                f"feline {disease} drug metabolism considerations",
                f"feline PK study sample size calculation",
                f"feline blood volume and sampling constraints",
            ]

        return subqueries

    def _build_reasoning(
        self,
        task_type: TaskType,
        search_depth: SearchDepth,
        requires_freshness: bool,
        requires_plurality: bool,
        requires_completeness: bool,
        species_strict: bool,
    ) -> str:
        """Build reasoning explanation for the evaluation."""
        parts = [
            f"Task type: {task_type.value}",
            f"Search depth: {search_depth.value}",
        ]

        if requires_freshness:
            parts.append("Requires latest literature")
        if requires_plurality:
            parts.append("Requires multiple sources (2+ types)")
        if requires_completeness:
            parts.append("Requires complete structured output")
        if species_strict:
            parts.append("Species-strict: cat evidence only, flag extrapolation")

        return "; ".join(parts)

    def create_record(self, query: str) -> ResearchRecord:
        """
        Evaluate query and create initial research record.

        Args:
            query: User's research question

        Returns:
            Initialized ResearchRecord with evaluation results
        """
        evaluation = self.evaluate(query)

        record = ResearchRecord.create(
            user_request=query,
            task_type=evaluation.task_type,
            disease=evaluation.disease,
        )

        record.search_depth = evaluation.search_depth
        record.scope = evaluation.reasoning
        record.search_queries = evaluation.subqueries
        record.retrieval_sources = evaluation.suggested_sources

        record.add_decision(f"Task evaluated as: {evaluation.task_type.value}")
        record.add_decision(f"Search depth set to: {evaluation.search_depth.value}")

        if evaluation.species_strict:
            record.add_decision("Species-strict mode: will flag non-cat evidence")

        return record
