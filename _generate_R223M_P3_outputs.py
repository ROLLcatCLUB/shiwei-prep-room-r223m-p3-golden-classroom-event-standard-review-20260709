from __future__ import annotations

import html
import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parent
STAGE_ID = "1013R_R223M_P3_STANDARD_TEMPLATE_AND_CONTROL_POINT_HARDENING"
STANDARD_ID = "GOLDEN_CLASSROOM_EVENT_EXPANSION_STANDARD_V0.1"


TEMPLATE_FIELDS = [
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


EVENTS = [
    {
        "event_id": "event_01_remember_brush_birth",
        "event_name": "忆一忆：毛笔的诞生",
        "section": "我们来学习",
        "source_anchor": {
            "sample": "我为文具代言",
            "anchor_text": ["智造·新朋友", "忆一忆：毛笔的诞生", "毛笔工艺", "传统工艺价值"],
            "source_status": "source_anchored_and_teacher_adjusted",
        },
        "teaching_responsibility": "把学生带回文具背后的传统工艺和使用智慧，建立“结构和材料服务使用”的改造前提。",
        "student_problem": "一年级学生容易把毛笔工序当成记忆内容，只记得热闹或名称，不知道工序与使用之间的关系。",
        "task_release": "从学习手册里选一个你记住的毛笔工序，说说这一步可能是为了让毛笔更好地做什么。",
        "expected_student_responses": ["能说出择笔、择料、结头、选管、装套等词", "会说为了写字更好、毛更整齐、笔杆更漂亮", "只记得看过毛笔厂或工序很多"],
        "likely_misconceptions_or_failures": ["把工序当作背诵题", "只说好看，不说使用功能", "回答和本课文具改造没有接上"],
        "teacher_follow_up_questions": ["这一步如果没有，会影响毛笔哪里？", "它是让毛笔更好看，还是更好用，还是两者都有？", "这个工序和笔头、笔杆、笔尾里的哪一处有关？"],
        "teacher_scaffolding_moves": ["投屏毛笔工序图", "圈出笔头、笔杆、笔尾", "给半句支架：这一步让毛笔……"],
        "teacher_rescue_strategy": ["学生说不出作用时，教师拿真实毛笔或图片做结构定位", "学生兴趣下降时，改成快速抢答：哪一步和笔头有关，哪一步和笔杆有关"],
        "control_points": {
            "observe": "学生是否能把至少一个工序和使用作用联系起来",
            "ask_when": "学生只背名称、只说好看或回答散开时",
            "rescue_when": "学生说不出工序作用或注意力开始下降时",
            "screen_when": "导入后 2 分钟内；学生说不出结构位置时",
            "component_when": "需要把工序和结构位置对应起来时",
            "evidence_when": "学生能说出一个工序名称和一个使用作用时",
            "proceed_when": "班级已经形成“文具结构为使用服务”的共同句子后",
        },
        "screen_trigger": {
            "type": "structure_recall",
            "content": "毛笔工序图 + 笔头/笔杆/笔尾圈画",
            "source_event_moment": "任务释放和学生说不清工序用途时",
            "screen_prompt": "这一步让毛笔哪里更好用？",
        },
        "component_trigger": [
            {
                "component_id": "circle_and_annotate",
                "trigger_condition": "学生说得出工序名称但说不清结构位置",
                "student_problem_solved": "观察散乱，不能把工序和文具结构对应",
                "alternative_component": "teacher_quick_pointing_demo",
                "evidence": "学生圈出或口头指出一个结构位置",
            }
        ],
        "learning_sheet_trigger": {
            "timing": "课中回忆后",
            "field": "我记住的毛笔工序 / 它让毛笔更好地……",
            "mode": "one_phrase_record",
        },
        "evidence_trigger": {
            "output": ["学习手册工序回忆", "学生口头解释一个工序作用"],
            "capture_timing": "导入收束前",
            "assessment_item": "发现文具结构与使用关系",
            "downstream_use": "为后续购买建议书提供“文具不是只看外观”的依据",
        },
        "assessment_alignment": ["发现新材料特性、新使用技法的前置观察能力", "展示会中能用理由表达想法的语言准备"],
        "transition_chain": {
            "from_evidence": "毛笔工序和使用作用",
            "to_task": "身边文具的结构为什么这样设计",
            "transition_talk": "既然毛笔每一步都有用，那我们来看看身边文具里还藏着哪些让人想问的为什么。",
        },
        "teacher_visible_note": "师维控制点：不要停在背工序，要把工序追问到“让哪里更好用”。",
        "teacher_process_paragraphs": [
            "教师先出示毛笔制作工艺图，请学生回忆学习手册中的工序。任务不要问成“你记住了什么”，而要问：“请你选一个记住的工序，说说这一步可能是为了让毛笔更好地做什么。”这样学生一开始就被带向结构和使用，而不是单纯复述。",
            "学生可能能说出择笔、择料、结头、选管、装套等词，也可能只说“工序很多”。如果学生把它当记忆题，教师追问：“这一步如果没有，会影响毛笔哪里？”当学生仍说不清时，教师投屏工序图或拿真实毛笔，圈出笔头、笔杆、笔尾，让学生把工序和位置对应起来。",
            "本环节证据不需要复杂，学生能说出一个工序名称和一个使用作用即可。教师收束：“一支毛笔不是随便拼起来的，每一步都在帮它变得更好用。今天我们也要从文具的结构和使用出发，试着给自己的文具交一个新朋友。”",
        ],
    },
    {
        "event_id": "event_02_ten_thousand_whys",
        "event_name": "探一探：关键的结构 / 十万个为什么",
        "section": "我们来学习",
        "source_anchor": {
            "sample": "我为文具代言",
            "anchor_text": ["探一探：关键的结构", "交流会：十万个为什么", "彩铅衣服", "毛笔小尾巴", "水彩笔笔盖", "圆珠笔笔尖"],
            "source_status": "source_anchored_and_teacher_adjusted",
        },
        "teaching_responsibility": "让学生从外观描述转向结构和功能解释，发现文具设计中隐藏的使用理由。",
        "student_problem": "学生能看到文具外形，但常常说不出为什么这样设计，容易停在好看、不好看。",
        "task_release": "同桌选择学习单上的一个为什么，先猜一猜这个设计帮我们解决了什么小麻烦，并说出你从哪里看出来。",
        "expected_student_responses": ["能围绕彩铅衣服、毛笔小尾巴、水彩笔笔盖、圆珠笔笔尖说猜想", "能说出保护、收纳、防掉、伸缩、方便携带", "只回答不知道或厂家这样做"],
        "likely_misconceptions_or_failures": ["只说漂亮或不漂亮", "争论答案对错，忽视观察依据", "把结构问题理解成装饰喜好"],
        "teacher_follow_up_questions": ["你从哪里看出来它是为了保护？", "如果没有笔盖，会发生什么？", "这个结构让使用更方便，还是让文具更安全？"],
        "teacher_scaffolding_moves": ["给保护、收纳、防掉、舒服、伸缩等选项", "用实物试开、试握、试收纳", "把学生答案写成关键词"],
        "teacher_rescue_strategy": ["学生不知道时给二选一：保护它，还是装饰它？", "学生只看外观时，让他亲手打开笔盖、按圆珠笔、摸毛笔尾部"],
        "control_points": {
            "observe": "学生是否能用一个关键词解释一个结构",
            "ask_when": "学生只说好看、厂家这样做或不知道时",
            "rescue_when": "讨论变成猜答案对错或学生没有观察依据时",
            "screen_when": "同桌交流后投屏四个为什么；出现好答案时圈出结构",
            "component_when": "学生说不清结构位置或需要把图像和关键词对应时",
            "evidence_when": "学生能在学习单或口头表达中用关键词解释结构时",
            "proceed_when": "学生能形成“文具小地方常在解决使用问题”的共识后",
        },
        "screen_trigger": {
            "type": "question_cluster",
            "content": "四个为什么 + 结构圈画 + 关键词",
            "source_event_moment": "同桌猜想后和答案收束时",
            "screen_prompt": "这个小结构解决了什么使用问题？",
        },
        "component_trigger": [
            {
                "component_id": "circle_and_annotate",
                "trigger_condition": "学生能说出猜想但不能指出结构依据",
                "student_problem_solved": "不知道观察点在哪里",
                "alternative_component": "match_cards",
                "evidence": "结构圈画或结构词卡匹配",
            },
            {
                "component_id": "match_cards",
                "trigger_condition": "需要把结构、功能和关键词建立对应",
                "student_problem_solved": "术语和图像关系弱",
                "alternative_component": "teacher_keyword_board",
                "evidence": "一条结构-功能连线和理由",
            },
        ],
        "learning_sheet_trigger": {
            "timing": "同桌交流后",
            "field": "我选择的为什么 / 我的猜想 / 我从哪里看出来",
            "mode": "keyword_plus_reason",
        },
        "evidence_trigger": {
            "output": ["十万个为什么记录", "结构关键词", "圈画截图或口头依据"],
            "capture_timing": "交流会收束时",
            "assessment_item": "能观察并说明文具结构与使用关系",
            "downstream_use": "为使用指南中的结构观察建议提供材料",
        },
        "assessment_alignment": ["发现文具结构和使用方法", "能用依据表达想法"],
        "transition_chain": {
            "from_evidence": "文具结构关键词",
            "to_task": "设计案例中的小巧思",
            "transition_talk": "这些小结构不是随便长出来的。接下来我们换个身份，不只做使用者，还要像设计师一样找小巧思。",
        },
        "teacher_visible_note": "师维控制点：学生只说好看时，立刻追到“它解决了什么使用问题”。",
        "teacher_process_paragraphs": [
            "教师组织同桌交流学习单中的“十万个为什么”。教师提醒学生：“答案可以先猜，不一定马上正确，但要说说你从哪里看出来。”这句话是控制点，避免讨论变成猜谜。",
            "学生可能会说“为了好看”“厂家就是这样做的”“不知道”。此时教师给出保护、收纳、防掉、舒服、伸缩等选项，并用实物让学生试开、试握、试收纳。当学生说出防掉、伸缩、保护笔头等答案时，教师投屏圈出对应结构，并写下关键词。",
            "学生能用一个关键词解释一个结构，就可以进入下一步。教师收束：“文具上很多小地方都不是随便长出来的，它们常常在解决一个使用问题。”",
        ],
    },
    {
        "event_id": "event_03_think_like_designer",
        "event_name": "设计会：像设计师一样思考",
        "section": "我们来学习",
        "source_anchor": {
            "sample": "我为文具代言",
            "anchor_text": ["设计会：像设计师一样思考", "小巧思", "握笔皮圈", "笔夹", "橡皮笔套", "磁吸白板笔"],
            "source_status": "source_anchored_and_teacher_adjusted",
        },
        "teaching_responsibility": "把结构观察推进到设计意识，让学生明白设计是发现一个小麻烦，再想一个小办法。",
        "student_problem": "学生会说喜欢或方便，但不一定能把喜欢和具体使用问题连接起来。",
        "task_release": "看大屏圈出的细节，猜一猜这个小巧思解决了什么麻烦。",
        "expected_student_responses": ["说握笔皮圈让手更舒服，笔夹方便固定", "用好看、方便、有趣评价案例", "提出会发光、会说话、会自动写字等大想法"],
        "likely_misconceptions_or_failures": ["把小巧思理解成装饰", "只说我喜欢，不说解决什么问题", "想法太大，不适合本课材料和时间"],
        "teacher_follow_up_questions": ["它帮谁解决了什么麻烦？", "如果你的文具也有这个小巧思，会让写字、收纳、寻找、保护更方便吗？", "今天先解决哪一个小问题？"],
        "teacher_scaffolding_moves": ["提供句式：我喜欢它，因为它能……", "给握、放、收、找四个方向", "把大想法缩到一个位置、一个材料、一个问题"],
        "teacher_rescue_strategy": ["学生只说喜欢时，用句式支架要求说理由", "学生想法过大时，教师把任务缩成可操作小目标"],
        "control_points": {
            "observe": "学生是否能说出小巧思对应的使用麻烦",
            "ask_when": "学生只说喜欢、好玩、方便但没有对象和问题时",
            "rescue_when": "学生想法过大或偏离本课材料条件时",
            "screen_when": "展示设计案例和板书握、放、收、找四个方向时",
            "component_when": "学生需要比较普通文具和有小巧思文具时",
            "evidence_when": "学生能说出一个小巧思和一个改进方向时",
            "proceed_when": "学生能把自己的改进想法缩成一个小问题后",
        },
        "screen_trigger": {
            "type": "design_case_compare",
            "content": "设计案例细节圈画 + 握/放/收/找方向",
            "source_event_moment": "学生从观察转入改进想法时",
            "screen_prompt": "这个小巧思帮谁解决了什么麻烦？",
        },
        "component_trigger": [
            {
                "component_id": "compare_two_images",
                "trigger_condition": "学生只说喜欢或方便，无法说明差异",
                "student_problem_solved": "不能把设计差异和使用问题联系起来",
                "alternative_component": "say_reason_sentence_starter",
                "evidence": "学生说出一个差异和一个使用作用",
            },
            {
                "component_id": "sentence_starter",
                "trigger_condition": "学生有想法但说不完整",
                "student_problem_solved": "表达理由不足",
                "alternative_component": "teacher_oral_prompt",
                "evidence": "我这样改，是为了……",
            },
        ],
        "learning_sheet_trigger": {
            "timing": "设计会收束前",
            "field": "我想解决的小麻烦 / 我想到的小办法",
            "mode": "one_problem_one_solution",
        },
        "evidence_trigger": {
            "output": ["一个改进方向", "一个小巧思理由"],
            "capture_timing": "进入 1+1 前",
            "assessment_item": "能说明设计理由",
            "downstream_use": "为 1+1 小设计和 1+n 文具大变身确定任务方向",
        },
        "assessment_alignment": ["自信表达自己的想法", "发现文具设计与使用关系"],
        "transition_chain": {
            "from_evidence": "一个可操作小问题",
            "to_task": "用铅笔和粘土做低门槛试验",
            "transition_talk": "现在我们先用最简单的一支铅笔和一块粘土，把一个小办法试出来。",
        },
        "teacher_visible_note": "师维控制点：把学生的“大设计”压成“一个小问题、一个位置、一个材料”。",
        "teacher_process_paragraphs": [
            "教师出示握笔皮圈、笔夹、橡皮笔套、磁吸白板笔等案例，让学生看大屏圈出的细节。教师不问“你喜欢哪个”，而问：“它小小的，但可能很有用。你能猜出这个小巧思解决了什么麻烦吗？”",
            "学生可能会说“好看”“方便”“我喜欢”。教师继续追问：“它帮谁解决了什么麻烦？”如果学生想法太大，教师把任务缩小：“今天先解决一个小问题，一个位置，一个材料。你最想让它更好握、更好找，还是更好收？”",
            "本环节的证据是学生能说出一个小巧思和一个改进方向。教师小结：“像设计师一样思考，就是先发现一个小麻烦，再想一个小办法。”",
        ],
    },
    {
        "event_id": "event_04_one_plus_one_design",
        "event_name": "试一试：1+1 合作小设计",
        "section": "我们来改造",
        "source_anchor": {
            "sample": "我为文具代言",
            "anchor_text": ["一支铅笔 + 一块粘土能有多少种设计", "1+1合作小设计", "粘土", "改进小草图"],
            "source_status": "source_anchored_and_teacher_adjusted",
        },
        "teaching_responsibility": "用低门槛材料让学生从草图进入可操作设计，建立一个问题对应一个改进的意识。",
        "student_problem": "学生有想法但直接做复杂改造困难，容易只做可爱装饰或合作分工不清。",
        "task_release": "如果只给你一支铅笔和一块粘土，你能让这支铅笔变得更好用，或者更有趣吗？先和同桌说草图，再动手试一试。",
        "expected_student_responses": ["捏小动物、小花或名字牌贴在笔杆上", "想到防滑、防滚动、标记自己的笔、握笔更舒服", "动手很快但说不出设计理由"],
        "likely_misconceptions_or_failures": ["只做可爱装饰，不考虑使用", "粘土位置影响握笔或书写", "合作变成一人做一人看", "作品掉落导致受挫"],
        "teacher_follow_up_questions": ["这个装饰让它更好拿了吗，还是更容易找到？", "你解决的是握、找、放、收里的哪一个问题？", "同桌负责什么，你负责什么？"],
        "teacher_scaffolding_moves": ["投屏对比装饰作品和功能改进作品", "示范压薄、包住、轻轻盘紧", "明确一人固定文具、一人塑形、一人说理由"],
        "teacher_rescue_strategy": ["只做装饰时，投屏比较两件作品并追问好看/好用", "贴不上时，教师展示半成品固定法", "合作失衡时，教师现场指定分工"],
        "control_points": {
            "observe": "学生是否能说出改进目的；粘土位置是否影响使用；合作是否均衡",
            "ask_when": "学生只做装饰或说不出理由时",
            "rescue_when": "材料固定失败、合作失衡或作品影响握笔时",
            "screen_when": "制作 4 到 5 分钟后出现典型装饰/功能差异作品时",
            "component_when": "需要对比半成品、提交照片或记录改进理由时",
            "evidence_when": "学生完成一个小设计并能说出目的时",
            "proceed_when": "大多数学生完成低门槛尝试，并理解一个问题对应一个改进后",
        },
        "screen_trigger": {
            "type": "student_work_compare",
            "content": "一件只是装饰的作品 + 一件解决防滑/防滚/易找问题的作品",
            "source_event_moment": "学生制作 4 到 5 分钟后",
            "screen_prompt": "哪一件解决了一个真实使用问题？",
        },
        "component_trigger": [
            {
                "component_id": "photo_submit",
                "trigger_condition": "需要选择 2 到 3 件学生半成品投屏",
                "student_problem_solved": "学生看不到不同方案的差异",
                "alternative_component": "teacher_camera_projection",
                "evidence": "1+1 小设计照片",
            },
            {
                "component_id": "compare_two_images",
                "trigger_condition": "学生只做装饰，不考虑使用问题",
                "student_problem_solved": "好看和好用没有区分",
                "alternative_component": "right_wrong_compare",
                "evidence": "学生能说出哪个设计解决了什么问题",
            },
            {
                "component_id": "learning_sheet_record",
                "trigger_condition": "学生完成小设计但理由容易丢失",
                "student_problem_solved": "过程证据缺失",
                "alternative_component": "oral_reason_round",
                "evidence": "我想解决的问题 / 我用了什么 / 它带来的改变",
            },
        ],
        "learning_sheet_trigger": {
            "timing": "1+1 作品完成后",
            "field": "我想解决的问题 / 我用了什么材料 / 它带来的改变",
            "mode": "photo_plus_short_reason",
        },
        "evidence_trigger": {
            "output": ["1+1 小设计照片", "改进理由", "合作分工痕迹"],
            "capture_timing": "投屏对比和小结前",
            "assessment_item": "能和小伙伴一起合作完成学习任务",
            "downstream_use": "作为 1+n 文具大变身的材料和问题起点",
        },
        "assessment_alignment": ["合作完成学习任务", "能说明改进理由"],
        "transition_chain": {
            "from_evidence": "一个低门槛小设计和改进理由",
            "to_task": "多材料、多技法的 1+n 文具大变身",
            "transition_talk": "刚才我们用粘土完成了第一次尝试。现在换一换材料，加一加技法，看看文具还能怎样变身。",
        },
        "teacher_visible_note": "师维控制点：只做装饰时不要否定，先追问它让文具更好看、好找，还是更好用。",
        "teacher_process_paragraphs": [
            "教师出示一支铅笔和一块粘土，提出挑战：“如果只给你一支铅笔和一块粘土，你能让这支铅笔变得更好用，或者更有趣吗？”教师补一句：“今天先不要做万能文具，先解决一个小问题。”",
            "学生动手后，常见反应是捏小动物、小花或名字牌贴在笔杆上。教师不急于否定，而是追问：“这个装饰让它更好拿了吗？让它更容易找到吗？还是让它更像你的专属文具？”如果学生完全只追求可爱，教师投屏两件作品比较：一件只是装饰，一件解决防滑、防滚动或标记问题。",
            "制作中若出现粘土贴不上、影响握笔、同桌合作变成一个人做，教师现场示范压薄、包住、轻轻盘紧，并明确一人固定文具、一人塑形、一人说理由。证据包括 1+1 小设计照片、改进理由和合作分工痕迹。",
        ],
    },
    {
        "event_id": "event_05_one_plus_n_transformation",
        "event_name": "创一创：1+n 文具大变身",
        "section": "我们来改造",
        "source_anchor": {
            "sample": "我为文具代言",
            "anchor_text": ["盘", "细细长长软软的线可以缠绕、盘圈", "1+n 文具大变身", "新材料特性", "新使用技法"],
            "source_status": "source_anchored_and_teacher_adjusted",
        },
        "teaching_responsibility": "把 1+1 小尝试扩展到多材料、多技法改造，并要求材料选择服务一个明确使用问题。",
        "student_problem": "学生容易材料拿太多、功能堆叠、技法不会迁移，作品变重或杂乱。",
        "task_release": "从材料区选择合适材料，用 1 到 2 种技法智造一支新朋友；材料要帮你解决刚才发现的小问题。",
        "expected_student_responses": ["选择毛线、扭扭棒、纸条、彩纸、形状材料", "尝试缠绕、盘圈、折叠、粘贴、组合", "发现细细长长软软的线可以缠绕、盘圈"],
        "likely_misconceptions_or_failures": ["堆材料忽视使用", "功能越加越多导致不好用", "不会从粘土迁移到线材、纸材或形状材料", "时间失控"],
        "teacher_follow_up_questions": ["这个材料的特性是什么？细、长、软、硬、轻、厚，哪一点帮了你？", "你的新朋友现在更好用了吗？哪里能看出来？", "如果只能保留一个材料，你会留下哪一个？"],
        "teacher_scaffolding_moves": ["展示线材盘圈、纸材折包、形状材料组合半成品", "给 1 到 2 种技法限制", "让学生删掉一个最不需要的材料"],
        "teacher_rescue_strategy": ["材料太多时做减材料追问", "不会做时提供半成品示范", "时间不足时允许局部改造并用学习单说明后续想法"],
        "control_points": {
            "observe": "学生材料是否服务使用问题；技法是否可控；时间是否失控",
            "ask_when": "学生堆材料、功能过多或说不清材料作用时",
            "rescue_when": "学生不会固定材料、作品变重或进度明显落后时",
            "screen_when": "技法归纳、材料过多对比、半成品示范时",
            "component_when": "需要技法拆解、材料选择板或拍照提交过程证据时",
            "evidence_when": "学生能说明材料特性和解决问题的关系时",
            "proceed_when": "作品或局部改造完成，且学生能说出材料/技法理由后",
        },
        "screen_trigger": {
            "type": "technique_and_material_demo",
            "content": "盘的技法、线材/纸材/形状材料半成品、材料过多与合适材料对比",
            "source_event_moment": "从 1+1 迁移到 1+n、学生不会固定材料或材料堆叠时",
            "screen_prompt": "这个材料的哪一点帮你解决了问题？",
        },
        "component_trigger": [
            {
                "component_id": "technique_step_demo",
                "trigger_condition": "学生不会固定线材、纸材或形状材料",
                "student_problem_solved": "有想法但操作不会做",
                "alternative_component": "teacher_half_finished_demo",
                "evidence": "学生能迁移一种技法完成局部改造",
            },
            {
                "component_id": "material_choice_board",
                "trigger_condition": "学生材料选择过多或不合适",
                "student_problem_solved": "材料选择不服务使用问题",
                "alternative_component": "remove_one_material_prompt",
                "evidence": "学生说出保留材料的理由",
            },
            {
                "component_id": "photo_submit",
                "trigger_condition": "需要保留过程或局部改造证据",
                "student_problem_solved": "创作过程不可见",
                "alternative_component": "teacher_sampling_photo",
                "evidence": "1+n 新朋友作品或局部改造照片",
            },
        ],
        "learning_sheet_trigger": {
            "timing": "1+n 创作中后段",
            "field": "我选择的材料 / 我使用的方法 / 它解决的问题 / 我还想继续改的地方",
            "mode": "process_reason_record",
        },
        "evidence_trigger": {
            "output": ["材料技法选择理由", "1+n 新朋友作品", "局部改造照片", "学习单过程记录"],
            "capture_timing": "中途投屏和作品完成后",
            "assessment_item": "我能发现新材料特性、新使用技法",
            "downstream_use": "为购买建议书和课堂使用指南提供材料选择和使用经验",
        },
        "assessment_alignment": ["发现新材料特性、新使用技法", "合作完成学习任务"],
        "transition_chain": {
            "from_evidence": "材料和技法选择理由",
            "to_task": "笔友汇展示和同伴评价",
            "transition_talk": "作品完成后，我们要把它介绍给大家，让同伴看看你的新朋友到底帮了什么忙。",
        },
        "teacher_visible_note": "师维控制点：学生堆材料时，不加任务，改问“如果只能留下一个材料，你留哪个，为什么”。",
        "teacher_process_paragraphs": [
            "教师从 1+1 作品中选择一件，引导学生观察：“它是怎样把粘土固定在笔杆上的？”师生共同归纳出“盘”的技法，再追问：“生活中还有哪些材料也可以盘？”学生可能想到毛线、扭扭棒、麻绳、金属丝，教师收束到“细细长长软软的线可以缠绕、盘圈”。",
            "随后教师出示纸材、线材、形状材料和技法图，发布任务：“选择合适材料，用 1 到 2 种技法智造一支新朋友。”这里的控制点是材料必须服务问题。学生材料拿太多时，教师不让他继续加，而问：“如果只能保留一个材料，你会留下哪一个？它帮了你什么？”",
            "中途可以停 1 分钟投屏：展示一个材料选择合适的作品和一个材料过多的作品，让学生比较哪个更方便使用。如果学生不会做，教师展示半成品示范。证据包括材料技法选择理由、1+n 新朋友作品和学习单过程记录。",
        ],
    },
    {
        "event_id": "event_06_pen_friend_gallery",
        "event_name": "笔友汇",
        "section": "我们来分享",
        "source_anchor": {
            "sample": "我为文具代言",
            "anchor_text": ["笔友汇", "词云图", "展示架", "同伴评价"],
            "source_status": "source_anchored_and_teacher_adjusted",
        },
        "teaching_responsibility": "把作品展示转化为自我评价和同伴评价，让学生用结构、功能、材料、使用等词说明改进理由。",
        "student_problem": "学生评价容易停在好看、可爱，不知道如何说出设计巧思；部分学生表达胆怯。",
        "task_release": "选择一个展示架放上自己的新朋友，并用一句话说明它为什么适合放在这里。",
        "expected_student_responses": ["按功能优化、外观优化、材料丰富、使用方便选择展示架", "用好看、可爱、方便介绍作品", "少数学生能用结构、功能、材料、使用中的一个词评价"],
        "likely_misconceptions_or_failures": ["选择朋友多的展示架", "评价只说好看", "不敢上台或声音很小", "同伴建议变成挑毛病"],
        "teacher_follow_up_questions": ["你为什么把它放在这个展示架？", "请从结构、功能、材料、使用里选一个词来说。", "这个建议能帮助同学改得更好吗？"],
        "teacher_scaffolding_moves": ["提供句式：我的新朋友原来……我用了……现在可以……", "投屏关键词词云", "教师示范一条具体评价"],
        "teacher_rescue_strategy": ["评价空泛时，要求从关键词中选一个角度", "表达胆怯时，允许同桌陪同或先小组内说", "建议变挑毛病时，重申建议是帮助改得更好"],
        "control_points": {
            "observe": "学生是否能用关键词说明设计理由；同伴评价是否具体友善",
            "ask_when": "学生只说好看或选择展示架没有理由时",
            "rescue_when": "学生胆怯、评价空泛或建议变挑毛病时",
            "screen_when": "展示关键词词云和选取 1 到 2 件作品现场点评时",
            "component_when": "评价空泛、需要句式或关键词支架时",
            "evidence_when": "学生完成介绍语、同伴点评语或展示架选择理由时",
            "proceed_when": "学生能从作品交流中提炼一条使用建议或改进建议后",
        },
        "screen_trigger": {
            "type": "keyword_feedback",
            "content": "结构、功能、材料、使用、方便、牢固、舒服、有创意词云",
            "source_event_moment": "作品展示和同伴点评时",
            "screen_prompt": "请选一个关键词，说说它哪里有巧思。",
        },
        "component_trigger": [
            {
                "component_id": "keyword_feedback",
                "trigger_condition": "学生评价只说好看或可爱",
                "student_problem_solved": "评价语言空泛",
                "alternative_component": "sentence_starter",
                "evidence": "一条带关键词的同伴评价",
            },
            {
                "component_id": "gallery_walk",
                "trigger_condition": "需要让学生按展示架进行分类和观察",
                "student_problem_solved": "自我评价缺少角度",
                "alternative_component": "teacher_selected_showcase",
                "evidence": "展示架选择和理由",
            },
        ],
        "learning_sheet_trigger": {
            "timing": "展示前后",
            "field": "我的新朋友原来……我用了……现在可以…… / 我收到的建议",
            "mode": "presentation_sentence_and_peer_feedback",
        },
        "evidence_trigger": {
            "output": ["展示架选择", "学生介绍语", "同伴点评语", "教师观察自信表达"],
            "capture_timing": "笔友汇展示和点评时",
            "assessment_item": "我能在展示会中自信表达自己的想法",
            "downstream_use": "转化为购买文具建议书和文具课堂使用指南中的建议语言",
        },
        "assessment_alignment": ["展示会中自信表达", "愿意接受同伴建议"],
        "transition_chain": {
            "from_evidence": "作品介绍和同伴建议",
            "to_task": "赠笔礼中的设计理由表达",
            "transition_talk": "会介绍自己的设计，也会听取别人的建议。最后，我们用一个小小的仪式，把今天的新朋友和建议送出去。",
        },
        "teacher_visible_note": "师维控制点：同伴评价不能只说好看，必须从关键词里选一个角度。",
        "teacher_process_paragraphs": [
            "学生完成作品后，教师提供展示架，如功能优化、外观优化、材料丰富、使用方便。学生选择展示架不是摆放动作，而是自我评价：它为什么属于这一类？",
            "进入笔友汇时，教师投屏关键词：结构、功能、材料、使用、方便、牢固、舒服、有创意。学生若只说“很好看”，教师要求他从关键词中选一个再说。句式可以是：“我的新朋友原来……我用了……现在可以……”",
            "同伴建议如果变成挑毛病，教师补一句：“建议是为了帮助同学改得更好，不是只说哪里不好。”证据包括展示架选择、学生介绍语、同伴点评语和教师对自信表达的观察。",
        ],
    },
    {
        "event_id": "event_07_gift_pen_ritual",
        "event_name": "赠笔礼",
        "section": "我们来分享",
        "source_anchor": {
            "sample": "我为文具代言",
            "anchor_text": ["赠笔礼", "购买文具建议书", "文具课堂使用指南", "使用建议"],
            "source_status": "source_anchored_and_teacher_adjusted",
        },
        "teaching_responsibility": "用仪式感完成情感收束，并把作品经验转化为后续建议书和使用指南的素材。",
        "student_problem": "学生容易只顾互赠热闹，忘记说清设计理由和使用建议。",
        "task_release": "可以把这支新朋友送给同伴，也可以送给自己。请说一句话：我想把它送给谁，为什么。",
        "expected_student_responses": ["说送给朋友、老师、爸爸妈妈或自己", "说因为好看、好用、想提醒自己爱惜文具", "部分学生能连接到买文具或用文具建议"],
        "likely_misconceptions_or_failures": ["只关注互赠热闹", "赠送对象引发争抢", "表达太简单或时间不够"],
        "teacher_follow_up_questions": ["你希望收到它的人怎样使用它？", "它提醒我们以后买文具、用文具时注意什么？", "这句话能不能放进后面的建议书或使用指南？"],
        "teacher_scaffolding_moves": ["投屏赠笔语句式", "每组一句赠笔语", "先静默写一句再交流"],
        "teacher_rescue_strategy": ["时间不足时改为每组一句", "表达太简单时给句式：我把它送给……因为它可以……", "现场太热闹时先写后说"],
        "control_points": {
            "observe": "学生是否把赠送理由和使用建议联系起来",
            "ask_when": "学生只说送给谁或因为好看时",
            "rescue_when": "时间不足、现场过热或表达太简单时",
            "screen_when": "投屏赠笔语句式和后续表现性任务标题时",
            "component_when": "需要句式支架或收集赠笔语时",
            "evidence_when": "学生说出可进入建议书/使用指南的一句话时",
            "proceed_when": "全课收束并明确下节课整理建议书和使用指南后",
        },
        "screen_trigger": {
            "type": "closing_sentence_and_unit_task",
            "content": "赠笔语句式 + 《一年级购买文具建议书》《文具课堂使用指南》",
            "source_event_moment": "赠笔表达和全课收束时",
            "screen_prompt": "我把它送给……因为它可以……",
        },
        "component_trigger": [
            {
                "component_id": "sentence_starter",
                "trigger_condition": "学生表达太简单或说不出理由",
                "student_problem_solved": "情感表达没有设计理由",
                "alternative_component": "group_one_sentence",
                "evidence": "赠笔语",
            },
            {
                "component_id": "learning_sheet_record",
                "trigger_condition": "需要沉淀后续建议书素材",
                "student_problem_solved": "课堂表达没有转化为单元成果素材",
                "alternative_component": "teacher_collect_sample_quotes",
                "evidence": "可引用的使用建议",
            },
        ],
        "learning_sheet_trigger": {
            "timing": "赠笔礼前或后",
            "field": "我把它送给……因为它可以…… / 这给我的购买或使用建议是……",
            "mode": "closing_sentence_capture",
        },
        "evidence_trigger": {
            "output": ["赠笔语", "作品照片", "可进入建议书和使用指南的使用建议"],
            "capture_timing": "全课收束时",
            "assessment_item": "展示会中自信表达自己的想法",
            "downstream_use": "直接进入第四阶段表现性任务素材池",
        },
        "assessment_alignment": ["展示会中自信表达", "把设计经验迁移到真实使用建议"],
        "transition_chain": {
            "from_evidence": "赠笔语和使用建议",
            "to_task": "第四阶段购买文具建议书和文具课堂使用指南",
            "transition_talk": "下节课，我们会把这些经验整理成给一年级同学的购买建议和课堂使用指南。",
        },
        "teacher_visible_note": "师维控制点：赠笔不是收尾热闹，必须说出“为什么送”和“怎样使用”。",
        "teacher_process_paragraphs": [
            "最后进行赠笔礼。教师营造简短仪式：“你可以把这支新朋友送给同伴，也可以送给自己。请说一句话：我想把它送给谁，为什么。”大屏只放一句句式，避免仪式失控。",
            "如果学生只说“我送给某某”，教师追问：“你希望收到它的人怎样使用它？”如果时间不足，改为每组一句赠笔语；如果表达太简单，给句式：“我把它送给……因为它可以……”",
            "赠笔语不是可有可无的漂亮话，而是后续《一年级购买文具建议书》和《文具课堂使用指南》的素材。教师最后收束：“今天我们不只是做了一件文具作品，还发现了材料的新办法，也学会了用设计帮助学习生活。”",
        ],
    },
]


def write_text(name: str, text: str) -> None:
    (ROOT / name).write_text(text.strip() + "\n", encoding="utf-8")


def write_json(name: str, data: object) -> None:
    (ROOT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def render_html(markdown_name: str, html_name: str) -> None:
    text = (ROOT / markdown_name).read_text(encoding="utf-8")
    lines = text.splitlines()
    heading = next((line[2:].strip() for line in lines if line.startswith("# ")), "R223M-P3")
    first_para = next(
        (
            line.strip()
            for line in lines
            if line.strip()
            and not line.startswith("#")
            and not line.startswith("```")
            and not line.startswith("stage_id")
            and not line.startswith("standard_id")
            and not line.startswith("status=")
            and not line.startswith("source=")
            and not line.startswith("formal_ui")
            and not line.startswith("R97B")
        ),
        "",
    )
    body = []
    in_fence = False
    pre_lines = []
    for line in lines:
        if line.strip().startswith("```"):
            if not in_fence:
                in_fence = True
                pre_lines = []
            else:
                body.append('<pre class="meta-block">' + html.escape("\n".join(pre_lines)) + "</pre>")
                in_fence = False
            continue
        if in_fence:
            pre_lines.append(line)
            continue
        if not line.strip():
            continue
        if line.startswith("# "):
            body.append(f"<h1>{html.escape(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            body.append(f"<section><h2>{html.escape(line[3:].strip())}</h2>")
        elif line.startswith("### "):
            body.append(f"<h3>{html.escape(line[4:].strip())}</h3>")
        else:
            raw = line.strip()
            klass = ""
            if raw.startswith("【本环节在做什么】"):
                klass = "section-purpose"
            elif raw.startswith("【师维控制点】"):
                klass = "control-note"
            elif raw.startswith("【"):
                klass = "intention"
            body.append(f'<p class="{klass}">{html.escape(raw)}</p>')

    html_doc = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{html.escape(heading)}</title>
<style>
:root{{--ink:#1e2f2a;--muted:#64766f;--line:#d9e5df;--paper:#fffef9;--bg:#f5f8f5;--accent:#227866;--soft:#edf7f3;--warn:#f6ead3;--ctrl:#f3f6ff;--ctrlLine:#8aa2d8;}}
*{{box-sizing:border-box;overflow-wrap:anywhere;}}
body{{margin:0;background:linear-gradient(90deg,rgba(34,120,102,.045) 1px,transparent 1px),linear-gradient(rgba(34,120,102,.045) 1px,transparent 1px),var(--bg);background-size:24px 24px;color:var(--ink);font-family:"Microsoft YaHei","PingFang SC",Arial,sans-serif;letter-spacing:0;}}
.shell{{max-width:1120px;margin:0 auto;padding:36px 28px 58px;}}
.paper{{background:var(--paper);border:1px solid var(--line);border-radius:8px;box-shadow:0 22px 62px rgba(31,63,55,.13);padding:46px 68px 56px;}}
.kicker{{color:var(--accent);font-weight:800;font-size:14px;margin-bottom:12px;}}
h1{{font-size:34px;line-height:1.3;margin:0 0 18px;color:#162922;}}
.summary{{font-size:16px;line-height:1.9;color:var(--muted);border-bottom:2px solid #b9d7cd;padding-bottom:20px;margin-bottom:28px;}}
.chips{{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 26px;}}
.chips span{{border:1px solid #c8dfd7;background:var(--soft);color:#155b4d;border-radius:999px;padding:5px 12px;font-size:12px;font-weight:700;}}
article{{max-width:900px;margin:0 auto;}}
section{{display:block;margin:30px 0;}}
h2{{margin:0 0 14px;font-size:23px;line-height:1.45;color:#162821;padding-left:13px;border-left:5px solid var(--accent);}}
h3{{margin:30px 0 10px;font-size:20px;line-height:1.5;color:#145e50;}}
p{{margin:0 0 15px;font-size:16px;line-height:2.08;text-align:justify;}}
.section-purpose{{margin:0 0 12px;padding:10px 14px;background:#eef7f3;border-left:4px solid #70a999;color:#2f5148;font-size:15px;line-height:1.85;text-align:left;}}
.control-note{{margin:0 0 17px;padding:10px 14px;background:var(--ctrl);border-left:4px solid var(--ctrlLine);color:#32476d;font-size:15px;line-height:1.85;text-align:left;}}
.intention{{margin:14px 0 20px;padding:13px 16px;background:#f2faf6;border-left:4px solid #86bbab;color:#36534b;font-size:15px;line-height:1.9;}}
.meta-block{{background:#102a24;color:#e7f5ef;border-radius:8px;padding:16px 20px;font-size:13px;line-height:1.7;white-space:pre-wrap;margin:14px 0 24px;word-break:break-word;}}
.note{{margin-top:30px;background:var(--warn);border:1px solid #ead59b;border-radius:8px;padding:14px 18px;color:#6b5418;font-size:14px;line-height:1.8;}}
.footer{{margin-top:30px;text-align:center;color:var(--muted);font-size:12px;}}
@media (max-width: 760px){{.shell{{padding:18px 12px 32px;}}.paper{{padding:28px 20px 36px;}}h1{{font-size:27px;}}h2{{font-size:20px;}}p{{font-size:15px;line-height:1.95;}}}}
</style>
</head>
<body data-stage-id="{STAGE_ID}" data-standard-id="{STANDARD_ID}" data-formal-ui="false" data-card-wall="false" data-r97b-modified="false">
<main class="shell"><div class="paper"><div class="kicker">师维智教 · 课堂事件展开标准样板 · 静态审核</div><div class="summary">{html.escape(first_para or '本页展示 R223M-P3 标准样板，不是正式 UI。')}</div><div class="chips"><span>黄金样板 v0.1</span><span>师维控制点</span><span>组件触发</span><span>大屏 / 学习单 / 证据链</span><span>formal UI blocked</span></div><article>
{''.join(body)}
</article><div class="note">边界：R223M-P3 只做静态标准样板和审核包；不改 R97B，不新增正式 route，不改 frontend/backend，不接 runtime/model/prompt/db，不写回 lesson body，不启动 R224，不 formal apply。</div></div><div class="footer">R223M-P3 standard template and control point hardening · fixture/static only</div></main>
</body></html>
"""
    write_text(html_name, html_doc)


def build_gold_chain() -> dict:
    return {
        "stage_id": STAGE_ID,
        "standard_id": STANDARD_ID,
        "status": "golden_classroom_event_expansion_standard_v0_1",
        "formal_ui": False,
        "sample": "我为文具代言",
        "lesson_stage": "第三阶段 智造·新朋友",
        "boundary": {
            "r97b_modified": False,
            "frontend_backend_modified": False,
            "runtime_model_prompt_db": False,
            "formal_apply": False,
            "teacher_main_draft_should_be_continuous": True,
            "card_wall_allowed": False,
            "component_runtime_allowed": False,
        },
        "template_fields": TEMPLATE_FIELDS,
        "granularity_rule": "一个课堂环节 = 一个明确教学责任 + 一组学生动作 + 一个证据产出；环节内必须能拆出任务释放、偏差出现、教师调控、证据采集和过渡链。",
        "events": EVENTS,
    }


def build_schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://shiwei.local/schemas/classroom_event_expansion_v0_1.json",
        "title": "Classroom Event Expansion Schema v0.1",
        "type": "object",
        "required": ["stage_id", "standard_id", "events", "boundary"],
        "properties": {
            "stage_id": {"const": STAGE_ID},
            "standard_id": {"const": STANDARD_ID},
            "formal_ui": {"const": False},
            "events": {
                "type": "array",
                "minItems": 7,
                "items": {
                    "type": "object",
                    "required": TEMPLATE_FIELDS + ["control_points"],
                    "properties": {
                        field: {"description": f"Required classroom event field: {field}"} for field in TEMPLATE_FIELDS
                    }
                    | {
                        "control_points": {
                            "type": "object",
                            "required": ["observe", "ask_when", "rescue_when", "screen_when", "component_when", "evidence_when", "proceed_when"],
                        }
                    },
                },
            },
        },
    }


def generate_template_md() -> str:
    return dedent(
        f"""
        # 课堂事件展开标准模板 v0.1

        ```text
        stage_id={STAGE_ID}
        standard_id={STANDARD_ID}
        status=standard_template_only
        formal_ui=blocked
        ```

        ## 一、定位

        课堂事件展开层不是 UI，也不是语言润色层。它位于“环节结构”和“教师可读整稿”之间，是大屏、课堂组件、学习单和评价证据的共同源头。

        标准颗粒度：

        ```text
        一个课堂环节 = 一个明确教学责任 + 一组学生动作 + 一个证据产出
        ```

        环节内部必须继续拆出：

        ```text
        任务释放 → 学生理解 → 偏差出现 → 教师追问 / 补救 → 示范 / 投屏 / 组件触发 → 证据采集 → 收束过渡
        ```

        ## 二、必备字段

        {chr(10).join(f"- `{field}`" for field in TEMPLATE_FIELDS)}

        ## 三、学生可能性类型库 v0.1

        ```text
        1. 说不出理由
        2. 只关注好看
        3. 操作不会做
        4. 材料选择不当
        5. 合作分工失衡
        6. 评价语言空泛
        7. 时间失控
        8. 任务理解偏差
        9. 创意过散
        10. 证据缺失
        ```

        ## 四、教师调控动作库 v0.1

        ```text
        追问理由
        给句式支架
        缩小任务
        投屏对比
        半成品示范
        错误修补
        关键词收束
        同伴互看
        材料替代
        暂停整理
        进入下一环节
        ```

        ## 五、教师主稿规则

        教师主稿必须连续可读，不得把字段铺成卡片墙。控制点只能作为短提示进入主稿，完整结构进入 JSON 或附录。
        """
    )


def generate_teacher_md() -> str:
    chunks = [
        f"""# 《我为文具代言》课堂过程展开标准样板 v4

```text
stage_id={STAGE_ID}
standard_id={STANDARD_ID}
status=teacher_readable_process_v4
source=R223M-P2 classroom event layer + P3 control point hardening
formal_ui=blocked
R97B / UI / runtime / prompt / model / db = untouched
```

## 一、标准样板定位

本稿把《我为文具代言》第三阶段“智造·新朋友”作为课堂事件展开标准样板。P2 已经让课堂过程“活起来”，P3 不再继续堆长文本，而是在连续教师稿中轻量埋入师维控制点，并把大屏、组件、学习单和证据触发沉到后端结构。

主稿仍然给老师读：先看环节在做什么，再看教师怎样释放任务、学生可能怎样反应、教师怎样接住课堂、何时投屏示范、何时收证据、怎样过渡到下一步。

## 二、教学过程标准样板
"""
    ]
    chinese_ord = ["一", "二", "三", "四", "五", "六", "七"]
    for index, event in enumerate(EVENTS):
        chunks.append(f"### （{chinese_ord[index]}）{event['event_name']}\n")
        chunks.append(f"【本环节在做什么】{event['teaching_responsibility']}\n")
        visible_note = event["teacher_visible_note"].removeprefix("师维控制点：")
        chunks.append(f"【师维控制点】{visible_note} 观察：{event['control_points']['observe']}；进入下一环节条件：{event['control_points']['proceed_when']}。\n")
        for paragraph in event["teacher_process_paragraphs"]:
            chunks.append(paragraph + "\n")
        chunks.append(f"过渡语：{event['transition_chain']['transition_talk']}\n")
    chunks.append(
        """## 三、评价与证据链

本课评价继续对齐原评价表：学生是否能发现新材料特性、新使用技法；是否能和小伙伴一起合作完成学习任务；是否能在展示会中自信表达自己的想法。P3 的变化是把这些评价证据放回课堂事件发生处，而不是课后才补。

具体证据包括：毛笔工序回忆、十万个为什么记录、设计小巧思理由、1+1 小设计照片、1+n 新朋友作品、材料技法选择理由、展示架选择、同伴点评语和赠笔语。这些证据同时服务第四阶段的《一年级购买文具建议书》和《文具课堂使用指南》。

## 四、标准样板使用说明

后续其他课例展开时，不必照搬《我为文具代言》的内容，但必须对齐这套结构：每个关键环节都要有教学责任、学生可能性、教师调控、触发点、证据和过渡链。教师主稿保持连续可读，结构化控制点进入后端 JSON 和审核附件。
"""
    )
    return "\n".join(chunks)


def generate_component_standard() -> str:
    lines = [
        f"# R223M-P3 Component Trigger Standard",
        "",
        "```text",
        f"stage_id={STAGE_ID}",
        "status=component_trigger_standard_static_only",
        "active_component_count=0",
        "```",
        "",
        "## 原则",
        "",
        "组件不是按钮货架，而是课堂事件中的教学动作。每个组件必须有触发条件、解决的学生问题、替代方案和证据输出。",
        "",
        "Required backend fields: `component_id`, `trigger_condition`, `student_problem_solved`, `alternative_component`, `evidence`.",
        "",
        "| Event | component_id | trigger_condition | student_problem_solved | alternative_component | Evidence |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for event in EVENTS:
        for comp in event["component_trigger"]:
            lines.append(
                f"| {event['event_name']} | `{comp['component_id']}` | {comp['trigger_condition']} | {comp['student_problem_solved']} | `{comp['alternative_component']}` | {comp['evidence']} |"
            )
    return "\n".join(lines)


def generate_screen_standard() -> str:
    lines = [
        "# R223M-P3 Screen Trigger Standard",
        "",
        "大屏内容必须从课堂事件中长出来，不得脱离任务、偏差、示范、关键词或证据提交。",
        "",
        "Required backend fields: `type`, `content`, `source_event_moment`, `screen_prompt`.",
        "",
        "| Event | Screen Type | Content | source_event_moment | Prompt |",
        "| --- | --- | --- | --- | --- |",
    ]
    for event in EVENTS:
        trigger = event["screen_trigger"]
        lines.append(f"| {event['event_name']} | `{trigger['type']}` | {trigger['content']} | {trigger['source_event_moment']} | {trigger['screen_prompt']} |")
    return "\n".join(lines)


def generate_evidence_standard() -> str:
    lines = [
        "# R223M-P3 Learning Sheet And Evidence Standard",
        "",
        "学习单和评价证据不做泛表，而从课堂事件采集点生成。",
        "",
        "| Event | Learning Sheet Field | Timing | Evidence Output | Assessment Alignment | Downstream Use |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for event in EVENTS:
        sheet = event["learning_sheet_trigger"]
        evidence = event["evidence_trigger"]
        lines.append(
            f"| {event['event_name']} | {sheet['field']} | {sheet['timing']} | {'；'.join(evidence['output'])} | {evidence['assessment_item']} | {evidence['downstream_use']} |"
        )
    return "\n".join(lines)


def generate_rubric() -> str:
    return dedent(
        f"""
        # R223M-P3 Control Point Rubric

        ```text
        stage_id={STAGE_ID}
        status=golden_standard_rubric_v0_1
        pass_line=20_of_25
        ```

        | Dimension | 5 points | 3 points | 1 point |
        | --- | --- | --- | --- |
        | 课堂事件是否真实展开 | 有任务释放、学生反应、偏差、教师调控、证据和过渡 | 有部分课堂事件，但偏摘要 | 只有活动流程 |
        | 学生可能性是否符合学情 | 能体现年级、能力、兴趣和常见偏差 | 有学生反应但不够具体 | 泛写学生讨论/制作 |
        | 教师追问和补救是否具体 | 有可说出口的追问、支架、补救和收束 | 有引导但偏泛 | 只写教师指导 |
        | 大屏 / 组件 / 学习单 / 证据是否有触发点 | 触发条件、时机、证据和替代方案齐全 | 有触发点但不完整 | 只列资源或组件名 |
        | 教师主稿是否连续可读 | 连续自然，控制点轻量，不堆卡片 | 可读但略重 | 卡片墙或字段墙 |

        低于 20 分，不允许作为课堂事件展开标准样板。
        """
    )


def generate_transition_notes() -> str:
    lines = [
        "# R223M-P3 Transition Chain Notes",
        "",
        "每个过渡语必须同时完成三件事：承接前一环节证据、推进下一项任务、告诉学生为什么进入下一步。",
        "",
        "| From Event | Evidence Carried Forward | Next Task | Transition Talk |",
        "| --- | --- | --- | --- |",
    ]
    for event in EVENTS:
        chain = event["transition_chain"]
        lines.append(f"| {event['event_name']} | {chain['from_evidence']} | {chain['to_task']} | {chain['transition_talk']} |")
    return "\n".join(lines)


def generate_before_after() -> str:
    return dedent(
        f"""
        # R223M-P3 Before / After Compare With P2

        ## P2 已解决

        ```text
        课堂事件展开层成立；
        学生可能反应、教师追问、补救、投屏和证据采集进入主稿；
        教师稿从卡片墙回到连续稿。
        ```

        ## P3 加固

        ```text
        1. 把 P2 中藏在自然段里的大屏、组件、学习单和证据触发显性化；
        2. 每个事件新增 control_points；
        3. 每个组件都有 trigger_condition、student_problem_solved、alternative_component、evidence；
        4. 每个大屏内容说明来自哪个课堂事件时刻；
        5. 每个证据点对齐原评价表和表现性任务；
        6. 教师 v4 稿只放轻量“师维控制点”，完整结构留在 JSON。
        ```

        ## 仍然禁止

        ```text
        不改 R97B；
        不开正式 UI；
        不接 runtime/model/prompt/db；
        不写回 lesson body；
        不启动 R224；
        不 formal apply。
        ```
        """
    )


def generate_report() -> str:
    return dedent(
        f"""
        # R223M-P3 Standardization Report

        ```text
        stage_id={STAGE_ID}
        standard_id={STANDARD_ID}
        status=READY_FOR_STANDARD_TEMPLATE_AND_CONTROL_POINT_REVIEW
        R223M-P2 = PASS_CLASSROOM_EVENT_LAYER_ESTABLISHED
        R223M-P3 = STANDARD_TEMPLATE_AND_CONTROL_POINT_HARDENING
        formal_ui=blocked
        R97B / UI / runtime / prompt / model / db = untouched
        ```

        ## Result

        R223M-P3 upgrades the P2 classroom event layer into a reusable golden standard sample. It keeps the teacher-facing draft continuous while adding backend-usable event fields, control points, component triggers, screen triggers, learning sheet triggers, evidence triggers, and transition chains.

        ## Main Review Question

        ```text
        Can this version serve as GOLDEN_CLASSROOM_EVENT_EXPANSION_STANDARD_V0.1 for later lesson examples?
        ```

        ## Outputs

        ```text
        R223M_P3_gold_classroom_event_chain.json
        R223M_P3_teacher_readable_process_v4.md
        R223M_P3_teacher_readable_process_v4.html
        R223M_P3_classroom_event_expansion_template_v0_1.md
        R223M_P3_classroom_event_expansion_schema_v0_1.json
        R223M_P3_component_trigger_standard.md
        R223M_P3_screen_trigger_standard.md
        R223M_P3_learning_sheet_and_evidence_standard.md
        R223M_P3_control_point_rubric.md
        R223M_P3_standardization_report.md
        ```

        ## Decision Options

        ```text
        R223M-P3 = PASS_GOLDEN_CLASSROOM_EVENT_EXPANSION_STANDARD_V0_1
        R223M-P3 = HOLD_FOR_CONTROL_POINT_REWRITE
        R223M-P3 = HOLD_FOR_TEACHER_READABILITY_COMPRESSION
        FORMAL_UI = BLOCKED
        ```
        """
    )


def generate_readmes() -> tuple[str, str]:
    readme = dedent(
        f"""
        # R223M-P3 Golden Classroom Event Expansion Standard Review

        ```text
        stage_id={STAGE_ID}
        standard_id={STANDARD_ID}
        formal_ui=blocked
        ```

        Main entry:

        ```text
        R223M_P3_teacher_readable_process_v4.html
        ```

        This is a static review package. It does not modify R97B, frontend/backend, runtime, provider/model, prompt, database, lesson body, or formal UI.
        """
    )
    guide = dedent(
        f"""
        # GPT Review Guide For R223M-P3

        Read first:

        ```text
        R223M_P3_teacher_readable_process_v4.html
        ```

        Then inspect:

        ```text
        R223M_P3_gold_classroom_event_chain.json
        R223M_P3_component_trigger_standard.md
        R223M_P3_screen_trigger_standard.md
        R223M_P3_learning_sheet_and_evidence_standard.md
        R223M_P3_control_point_rubric.md
        ```

        Hard review:

        ```text
        1. 这版能不能作为后续课例展开模板；
        2. 教师主稿是否仍然自然、连续、可读；
        3. 后端结构是否足够支撑大屏、组件、学习单和评价；
        4. 控制点是否具体，而不是泛泛写“教师引导”；
        5. 组件触发是否有条件；
        6. 证据链是否能对应评价表；
        7. 是否保留《我为文具代言》的精品课味；
        8. 是否仍然不改 UI、不接 runtime。
        ```
        """
    )
    return readme, guide


def main() -> None:
    write_json("R223M_P3_gold_classroom_event_chain.json", build_gold_chain())
    write_json("R223M_P3_classroom_event_expansion_schema_v0_1.json", build_schema())
    write_text("R223M_P3_classroom_event_expansion_template_v0_1.md", generate_template_md())
    write_text("R223M_P3_teacher_readable_process_v4.md", generate_teacher_md())
    render_html("R223M_P3_teacher_readable_process_v4.md", "R223M_P3_teacher_readable_process_v4.html")
    write_text("R223M_P3_component_trigger_standard.md", generate_component_standard())
    write_text("R223M_P3_screen_trigger_standard.md", generate_screen_standard())
    write_text("R223M_P3_learning_sheet_and_evidence_standard.md", generate_evidence_standard())
    write_text("R223M_P3_control_point_rubric.md", generate_rubric())
    write_text("R223M_P3_transition_chain_notes.md", generate_transition_notes())
    write_text("R223M_P3_before_after_compare_with_P2.md", generate_before_after())
    write_text("R223M_P3_standardization_report.md", generate_report())
    readme, guide = generate_readmes()
    write_text("README.md", readme)
    write_text("README_FOR_GPT_REVIEW.md", guide)


if __name__ == "__main__":
    main()
