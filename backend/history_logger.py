history = []

class HistoryLogger:
    def save(self, event, conversation):
        history.append({
            "event": event,
            "conversation": conversation
        })

    def get_history(self):
        return history