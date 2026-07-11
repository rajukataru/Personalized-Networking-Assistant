from fastapi import APIRouter
from backend.event_analyzer import EventAnalyzer
from backend.topic_generator import TopicGenerator
from backend.fact_checker import FactChecker
from backend.history_logger import HistoryLogger
from backend.feedback_logger import FeedbackLogger

router = APIRouter()

analyzer = EventAnalyzer()
generator = TopicGenerator()
fact_checker = FactChecker()
history_logger = HistoryLogger()
feedback_logger = FeedbackLogger()


@router.get("/")
def home():
    return {"message": "Welcome to Personalized Networking Assistant!"}


@router.get("/analyze")
def analyze(event: str):
    themes = analyzer.extract_themes(event)
    return {"event": event, "themes": themes}


@router.get("/generate")
def generate(event: str):
    themes = analyzer.extract_themes(event)
    conversation = generator.generate_topics(themes)
    history_logger.save(event, conversation)

    return {
        "event": event,
        "themes": themes,
        "conversation_starters": conversation
    }


@router.get("/fact")
def fact(topic: str):
    return {
        "topic": topic,
        "fact": fact_checker.check_fact(topic)
    }


@router.get("/history")
def history():
    return history_logger.get_history()


@router.get("/feedback")
def feedback(event: str, user_feedback: str):
    feedback_logger.save_feedback(event, user_feedback)
    return {"message": "Feedback saved successfully!"}


@router.get("/feedback-history")
def feedback_history():
    return feedback_logger.get_feedback()