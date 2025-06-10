from typing import Any, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# 대화 연장
class ActionAskContinue(Action):
    def name(self) -> str:
        return "utter_ask_continue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        dispatcher.utter_message(
            text="혹시 더 얘기하고 싶은 게 있나요?",
            metadata={"action_name": "utter_ask_continue"}
        )
        return []

# ✅ 긍정 종료 응답
class ActionEndChatPositive(Action):
    def name(self) -> str:
        return "utter_end_chat_positive"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        dispatcher.utter_message(
            text="오늘도 기분이 좋아서 다행이에요. 내일도 좋은 하루 보내요! (end positive)",
            metadata={"action_name": "utter_end_chat_positive"}
        )
        return []

# ✅ 중립 종료 응답
class ActionEndChatNeutral(Action):
    def name(self) -> str:
        return "utter_end_chat_neutral"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        dispatcher.utter_message(
            text="오늘도 수고했어요. 내일은 더 행복한 날이길! (end neutral)",
            metadata={"action_name": "utter_end_chat_neutral"}
        )
        return []

# ✅ 부정 종료 응답 (+ 상담 권유 포함)
class ActionEndChatNegative(Action):
    def name(self) -> str:
        return "utter_end_chat_negative"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        dispatcher.utter_message(
            text="오늘을 버틴 당신이 대견해요. 너무 힘들 땐 전문가와 상담해보는 것도 좋아요! (end negative)",
            metadata={"action_name": "utter_end_chat_negative"}
        )
        return []

# ✅ 전문가 상담 권유 응답 (보조 액션)
class ActionRecommendCounseling(Action):
    def name(self) -> str:
        return "utter_recommend_counseling"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        dispatcher.utter_message(
            text="당신의 상태가 많이 힘들어 보여요. 혼자 끌어안지 말고 전문가에게 상담받아보는 건 어때요?",
            metadata={"action_name": "utter_recommend_counseling"}
        )
        return []
