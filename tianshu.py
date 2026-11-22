"""天枢（TIANSHU）· 总领调度

道统出处：元极恒一·道统构件定名册 V2（谱首） ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：总领调度。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Tianshu:
    """天枢（TIANSHU）算子骨架 v0。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "TIANSHU"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "tianshu",
            "cn": "天枢",
            "code": self.CODE,
            "duty": "总领调度",
            "mingwen": "枢居中央，众柄自转",
            "anchor": self.ANCHOR,
        }

    def register_component(self, name, handler):
        """登记构件处理器，返回登记序号（只增不覆盖）（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("TIANSHU.register_component 骨架桩，候进化轮补齐")

    def dispatch(self, task):
        """按谱系把任务路由到责任构件；骨架期返回路由意向，不实际执行（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("TIANSHU.dispatch 骨架桩，候进化轮补齐")
