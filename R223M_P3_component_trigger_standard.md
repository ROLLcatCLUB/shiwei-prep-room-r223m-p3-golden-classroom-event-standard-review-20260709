# R223M-P3 Component Trigger Standard

```text
stage_id=1013R_R223M_P3_STANDARD_TEMPLATE_AND_CONTROL_POINT_HARDENING
status=component_trigger_standard_static_only
active_component_count=0
```

## 原则

组件不是按钮货架，而是课堂事件中的教学动作。每个组件必须有触发条件、解决的学生问题、替代方案和证据输出。

Required backend fields: `component_id`, `trigger_condition`, `student_problem_solved`, `alternative_component`, `evidence`.

| Event | component_id | trigger_condition | student_problem_solved | alternative_component | Evidence |
| --- | --- | --- | --- | --- | --- |
| 忆一忆：毛笔的诞生 | `circle_and_annotate` | 学生说得出工序名称但说不清结构位置 | 观察散乱，不能把工序和文具结构对应 | `teacher_quick_pointing_demo` | 学生圈出或口头指出一个结构位置 |
| 探一探：关键的结构 / 十万个为什么 | `circle_and_annotate` | 学生能说出猜想但不能指出结构依据 | 不知道观察点在哪里 | `match_cards` | 结构圈画或结构词卡匹配 |
| 探一探：关键的结构 / 十万个为什么 | `match_cards` | 需要把结构、功能和关键词建立对应 | 术语和图像关系弱 | `teacher_keyword_board` | 一条结构-功能连线和理由 |
| 设计会：像设计师一样思考 | `compare_two_images` | 学生只说喜欢或方便，无法说明差异 | 不能把设计差异和使用问题联系起来 | `say_reason_sentence_starter` | 学生说出一个差异和一个使用作用 |
| 设计会：像设计师一样思考 | `sentence_starter` | 学生有想法但说不完整 | 表达理由不足 | `teacher_oral_prompt` | 我这样改，是为了…… |
| 试一试：1+1 合作小设计 | `photo_submit` | 需要选择 2 到 3 件学生半成品投屏 | 学生看不到不同方案的差异 | `teacher_camera_projection` | 1+1 小设计照片 |
| 试一试：1+1 合作小设计 | `compare_two_images` | 学生只做装饰，不考虑使用问题 | 好看和好用没有区分 | `right_wrong_compare` | 学生能说出哪个设计解决了什么问题 |
| 试一试：1+1 合作小设计 | `learning_sheet_record` | 学生完成小设计但理由容易丢失 | 过程证据缺失 | `oral_reason_round` | 我想解决的问题 / 我用了什么 / 它带来的改变 |
| 创一创：1+n 文具大变身 | `technique_step_demo` | 学生不会固定线材、纸材或形状材料 | 有想法但操作不会做 | `teacher_half_finished_demo` | 学生能迁移一种技法完成局部改造 |
| 创一创：1+n 文具大变身 | `material_choice_board` | 学生材料选择过多或不合适 | 材料选择不服务使用问题 | `remove_one_material_prompt` | 学生说出保留材料的理由 |
| 创一创：1+n 文具大变身 | `photo_submit` | 需要保留过程或局部改造证据 | 创作过程不可见 | `teacher_sampling_photo` | 1+n 新朋友作品或局部改造照片 |
| 笔友汇 | `keyword_feedback` | 学生评价只说好看或可爱 | 评价语言空泛 | `sentence_starter` | 一条带关键词的同伴评价 |
| 笔友汇 | `gallery_walk` | 需要让学生按展示架进行分类和观察 | 自我评价缺少角度 | `teacher_selected_showcase` | 展示架选择和理由 |
| 赠笔礼 | `sentence_starter` | 学生表达太简单或说不出理由 | 情感表达没有设计理由 | `group_one_sentence` | 赠笔语 |
| 赠笔礼 | `learning_sheet_record` | 需要沉淀后续建议书素材 | 课堂表达没有转化为单元成果素材 | `teacher_collect_sample_quotes` | 可引用的使用建议 |
