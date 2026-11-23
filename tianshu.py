"""天枢（TIANSHU）· 总领调度

道统出处：元极恒一·道统构件定名册 V2（谱首） ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：总领调度。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Tianshu:
    """天枢（TIANSHU）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "TIANSHU"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.components = {}

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
        """众柄归枢：构件登记。"""
        if not callable(handler):
            raise ValueError("构件须可调用")
        self.components[name] = handler
        self.events.append({"event": "register_component", "name": name})
        return name

    def dispatch(self, task):
        """枢居中央：按构件名分派任务。"""
        name = (task or {}).get("component")
        if name not in self.components:
            raise KeyError("枢不知此柄： %s" % name)
        result = self.components[name]((task or {}).get("payload"))
        self.events.append({"event": "dispatch", "component": name})
        return result
