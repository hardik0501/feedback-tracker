feedback_db = []

def store_feedback(data):
    feedback_db.append(data)

def get_all_feedback():
    return feedback_db

def get_summary():
    if not feedback_db:
        return {"count": 0, "average_rating": 0}
    total = sum([f['rating'] for f in feedback_db if 'rating' in f])
    count = len(feedback_db)
    return {
        "count": count,
        "average_rating": round(total / count, 2)
    }
