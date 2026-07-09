# 课堂事件展开标准模板 v0.1

        ```text
        stage_id=1013R_R223M_P3_STANDARD_TEMPLATE_AND_CONTROL_POINT_HARDENING
        standard_id=GOLDEN_CLASSROOM_EVENT_EXPANSION_STANDARD_V0.1
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

        - `event_id`
- `event_name`
- `section`
- `source_anchor`
- `teaching_responsibility`
- `student_problem`
- `task_release`
- `expected_student_responses`
- `likely_misconceptions_or_failures`
- `teacher_follow_up_questions`
- `teacher_scaffolding_moves`
- `teacher_rescue_strategy`
- `screen_trigger`
- `component_trigger`
- `learning_sheet_trigger`
- `evidence_trigger`
- `assessment_alignment`
- `transition_chain`
- `teacher_visible_note`

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
