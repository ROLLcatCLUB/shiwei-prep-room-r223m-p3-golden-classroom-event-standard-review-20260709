#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


STAGE_ID = "1013R_R223M_P3_STANDARD_TEMPLATE_AND_CONTROL_POINT_HARDENING"
STANDARD_ID = "GOLDEN_CLASSROOM_EVENT_EXPANSION_STANDARD_V0.1"

REQUIRED_FILES = [
    "R223M_P3_gold_classroom_event_chain.json",
    "R223M_P3_teacher_readable_process_v4.md",
    "R223M_P3_teacher_readable_process_v4.html",
    "R223M_P3_classroom_event_expansion_template_v0_1.md",
    "R223M_P3_classroom_event_expansion_schema_v0_1.json",
    "R223M_P3_component_trigger_standard.md",
    "R223M_P3_screen_trigger_standard.md",
    "R223M_P3_learning_sheet_and_evidence_standard.md",
    "R223M_P3_control_point_rubric.md",
    "R223M_P3_transition_chain_notes.md",
    "R223M_P3_before_after_compare_with_P2.md",
    "R223M_P3_standardization_report.md",
    "R223M_P3_screenshot_smoke_result.json",
    "R223M_P3_teacher_readable_process_v4_screenshot.png",
    "README.md",
    "README_FOR_GPT_REVIEW.md",
]

REQUIRED_TEMPLATE_FIELDS = [
    "event_id",
    "event_name",
    "section",
    "source_anchor",
    "teaching_responsibility",
    "student_problem",
    "task_release",
    "expected_student_responses",
    "likely_misconceptions_or_failures",
    "teacher_follow_up_questions",
    "teacher_scaffolding_moves",
    "teacher_rescue_strategy",
    "screen_trigger",
    "component_trigger",
    "learning_sheet_trigger",
    "evidence_trigger",
    "assessment_alignment",
    "transition_chain",
    "teacher_visible_note",
]

CONTROL_POINT_KEYS = [
    "observe",
    "ask_when",
    "rescue_when",
    "screen_when",
    "component_when",
    "evidence_when",
    "proceed_when",
]

EVENT_NAMES = [
    "忆一忆：毛笔的诞生",
    "探一探：关键的结构 / 十万个为什么",
    "设计会：像设计师一样思考",
    "试一试：1+1 合作小设计",
    "创一创：1+n 文具大变身",
    "笔友汇",
    "赠笔礼",
]

FORBIDDEN = [
    "正式 UI 已放行",
    "formal UI approved",
    "R97B route implemented",
    "provider call enabled",
    "database write enabled",
    "R224 started",
    "问我任何问题",
    "组件货架",
]


def add(checks: list[dict], name: str, passed: bool, detail: str = "") -> None:
    checks.append({"name": name, "passed": bool(passed), "detail": detail})


def read(root: Path, name: str) -> str:
    return (root / name).read_text(encoding="utf-8")


def validate(root: Path) -> dict:
    checks: list[dict] = []

    for name in REQUIRED_FILES:
        add(checks, f"required_file::{name}", (root / name).exists())

    chain = json.loads(read(root, "R223M_P3_gold_classroom_event_chain.json"))
    schema = json.loads(read(root, "R223M_P3_classroom_event_expansion_schema_v0_1.json"))
    teacher_md = read(root, "R223M_P3_teacher_readable_process_v4.md")
    teacher_html = read(root, "R223M_P3_teacher_readable_process_v4.html")
    template_md = read(root, "R223M_P3_classroom_event_expansion_template_v0_1.md")
    component_md = read(root, "R223M_P3_component_trigger_standard.md")
    screen_md = read(root, "R223M_P3_screen_trigger_standard.md")
    evidence_md = read(root, "R223M_P3_learning_sheet_and_evidence_standard.md")
    rubric_md = read(root, "R223M_P3_control_point_rubric.md")
    report_md = read(root, "R223M_P3_standardization_report.md")

    add(checks, "stage_id_matches", chain.get("stage_id") == STAGE_ID)
    add(checks, "standard_id_matches", chain.get("standard_id") == STANDARD_ID)
    add(checks, "formal_ui_false", chain.get("formal_ui") is False)
    boundary = chain.get("boundary", {})
    add(checks, "r97b_unmodified", boundary.get("r97b_modified") is False)
    add(checks, "runtime_prompt_db_blocked", boundary.get("runtime_model_prompt_db") is False)
    add(checks, "card_wall_not_allowed", boundary.get("card_wall_allowed") is False)
    add(checks, "component_runtime_not_allowed", boundary.get("component_runtime_allowed") is False)

    for field in REQUIRED_TEMPLATE_FIELDS:
        add(checks, f"template_field_in_chain::{field}", field in chain.get("template_fields", []))
        add(checks, f"template_field_in_md::{field}", f"`{field}`" in template_md)
        add(checks, f"schema_requires::{field}", field in json.dumps(schema, ensure_ascii=False))

    events = chain.get("events", [])
    add(checks, "event_count_is_7", len(events) == 7, f"count={len(events)}")
    names = [event.get("event_name") for event in events]
    for name in EVENT_NAMES:
        add(checks, f"event_name_present::{name}", name in names)
        add(checks, f"teacher_md_has_event::{name}", name in teacher_md)

    for idx, event in enumerate(events, start=1):
        for field in REQUIRED_TEMPLATE_FIELDS:
            add(checks, f"event_{idx:02d}_has::{field}", bool(event.get(field)))
        control = event.get("control_points", {})
        for key in CONTROL_POINT_KEYS:
            add(checks, f"event_{idx:02d}_control_has::{key}", bool(control.get(key)))
        comps = event.get("component_trigger", [])
        add(checks, f"event_{idx:02d}_has_component_trigger", isinstance(comps, list) and len(comps) >= 1)
        for c_idx, component in enumerate(comps, start=1):
            for key in ["component_id", "trigger_condition", "student_problem_solved", "alternative_component", "evidence"]:
                add(checks, f"event_{idx:02d}_component_{c_idx:02d}_has::{key}", bool(component.get(key)))
        screen = event.get("screen_trigger", {})
        for key in ["type", "content", "source_event_moment", "screen_prompt"]:
            add(checks, f"event_{idx:02d}_screen_has::{key}", bool(screen.get(key)))
        sheet = event.get("learning_sheet_trigger", {})
        for key in ["timing", "field", "mode"]:
            add(checks, f"event_{idx:02d}_learning_sheet_has::{key}", bool(sheet.get(key)))
        evidence = event.get("evidence_trigger", {})
        for key in ["output", "capture_timing", "assessment_item", "downstream_use"]:
            add(checks, f"event_{idx:02d}_evidence_has::{key}", bool(evidence.get(key)))
        transition = event.get("transition_chain", {})
        for key in ["from_evidence", "to_task", "transition_talk"]:
            add(checks, f"event_{idx:02d}_transition_has::{key}", bool(transition.get(key)))

    add(checks, "teacher_md_has_7_purpose_notes", teacher_md.count("【本环节在做什么】") == 7)
    add(checks, "teacher_md_has_7_control_notes", teacher_md.count("【师维控制点】") == 7)
    add(checks, "teacher_md_has_transition_notes", teacher_md.count("过渡语：") == 7)
    add(checks, "teacher_html_stage_attr", f'data-stage-id="{STAGE_ID}"' in teacher_html)
    add(checks, "teacher_html_standard_attr", f'data-standard-id="{STANDARD_ID}"' in teacher_html)
    add(checks, "teacher_html_formal_ui_false", 'data-formal-ui="false"' in teacher_html)
    add(checks, "teacher_html_card_wall_false", 'data-card-wall="false"' in teacher_html)
    add(checks, "teacher_html_has_7_control_notes", teacher_html.count('class="control-note"') == 7)
    add(checks, "teacher_html_no_question_mojibake", "???" not in teacher_html and "????" not in teacher_html)
    for forbidden_class in ["component-card", "chain-node", "decision-card"]:
        add(checks, f"teacher_html_no_card_class::{forbidden_class}", forbidden_class not in teacher_html)

    for phrase in ["component_id", "trigger_condition", "student_problem_solved", "alternative_component", "Evidence"]:
        add(checks, f"component_standard_has::{phrase}", phrase in component_md)
    for phrase in ["source_event_moment", "任务", "对比", "示范", "关键词"]:
        add(checks, f"screen_standard_has::{phrase}", phrase in screen_md)
    for phrase in ["发现新材料特性", "合作完成学习任务", "展示会中自信表达", "购买文具建议书", "文具课堂使用指南"]:
        add(checks, f"evidence_standard_has::{phrase}", phrase in evidence_md)
    for phrase in ["pass_line=20_of_25", "课堂事件是否真实展开", "教师主稿是否连续可读"]:
        add(checks, f"rubric_has::{phrase}", phrase in rubric_md)
    for phrase in ["GOLDEN_CLASSROOM_EVENT_EXPANSION_STANDARD_V0.1", "READY_FOR_STANDARD_TEMPLATE", "FORMAL_UI = BLOCKED"]:
        add(checks, f"report_has::{phrase}", phrase in report_md)

    smoke_path = root / "R223M_P3_screenshot_smoke_result.json"
    if smoke_path.exists():
        smoke = json.loads(smoke_path.read_text(encoding="utf-8"))
        add(checks, "smoke_stage_matches", smoke.get("stage") == STAGE_ID)
        add(checks, "smoke_no_horizontal_overflow", smoke.get("horizontalOverflow") is False)
        add(checks, "smoke_has_7_control_notes", smoke.get("controlNoteCount") == 7)
        add(checks, "smoke_no_question_mojibake", smoke.get("questionMarkInChromeText") is False)
        for key, value in smoke.get("hasText", {}).items():
            add(checks, f"smoke_has_text::{key}", value is True)
    else:
        add(checks, "smoke_file_present_for_checks", False)

    all_text = "\n".join([teacher_md, teacher_html, template_md, component_md, screen_md, evidence_md, rubric_md, report_md, json.dumps(chain, ensure_ascii=False)])
    for phrase in FORBIDDEN:
        add(checks, f"forbidden_absent::{phrase}", phrase not in all_text)

    failed = [check for check in checks if not check["passed"]]
    return {
        "stage_id": STAGE_ID,
        "standard_id": STANDARD_ID,
        "passed": not failed,
        "check_count": len(checks),
        "failed": len(failed),
        "failed_checks": failed,
        "event_count": len(events),
        "template_field_count": len(REQUIRED_TEMPLATE_FIELDS),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    result = validate(Path(args.root).resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
