facts_db = {
    "capital of france": "Paris",
    "capital of india": "New Delhi",
    "speed of light": "299,792,458 m/s",
    "pi value": "Approximately 3.14159"
}

def simple_search_tool(query: str):
    query = query.lower().strip()
    return facts_db.get(query, "No factual answer found in database.")
