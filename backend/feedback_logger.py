feedback_list = []

class FeedbackLogger:
    def save_feedback(self, event, feedback):
        feedback_list.append({
            "event": event,
            "feedback": feedback
        })

    def get_feedback(self):
        return feedback_list