import random

# Common SQL injection payloads
payloads = [
    "' OR '1'='1",
    "'; DROP TABLE Users; --",
    "' UNION SELECT ALL FROM Users; --",
    "' OR 'a'='a",
    "' OR 1=1 --",
    "' OR 'a'='a' --",
    "' OR 1=1#",
    "' OR 1=1/*",
]

def generate_sql_injection_payloads():
    payloads = [
        "' OR '1'='1",
        "'; DROP TABLE Users; --",
        "' UNION SELECT ALL FROM Users; --",
        "' OR 'a'='a",
        "' OR 1=1 --",
        "' OR 'a'='a' --",
        "' OR 1=1#",
        "' OR 1=1/*",
    ]
    return random.choice(payloads)

# Example SQL injection detection function
def detect_sql_injection(query):
    # Simple detection based on common patterns (for demonstration purposes)
    injection_patterns = [
        " OR ",
        " AND ",
        " UNION ",
        "SELECT ",
        "INSERT ",
        "UPDATE ",
        "DELETE ",
        "DROP ",
        "--",
        "#",
        "/*",
    ]
    for pattern in injection_patterns:
        if pattern in query.upper():
            return True
    return False

# Example usage
if __name__ == "__main__":
    for _ in range(10):  # Generate and test 10 payloads
        payload = generate_sql_injection_payloads()
        print(f"Generated Payload: {payload}")
        query = f"SELECT * FROM Users WHERE Username = '{payload}'"
        if detect_sql_injection(query):
            print("Potential SQL injection detected.")
        else:
            print("No SQL injection detected.")
