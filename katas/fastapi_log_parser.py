import re

def parse_fastapi_log(log_line: str):
    """
    Parses a single FastAPI request log entry into a structured dictionary, without regex.
    """
    try:
        # Remove the "INFO:" prefix
        parts = log_line.split("INFO:")[1].strip()

        # Split IP and port
        address_part, rest = parts.split(" - ", 1)
        client_ip, client_port = address_part.strip().split(":")

        # Extract method, endpoint, HTTP version
        request_part, status_part = rest.split('"')[1], rest.split('"')[2].strip()
        http_method, endpoint, http_version = request_part.strip().split()

        # Clean HTTP version
        http_version = http_version.replace("HTTP/", "")

        # Extract status code and status text
        status_code, status_text = status_part.split(" ", 1)

        return {
            "client_ip": client_ip,
            "client_port": client_port,
            "http_method": http_method,
            "endpoint": endpoint,
            "http_version": http_version,
            "status_code": status_code,
            "status_text": status_text
        }

    except (ValueError, IndexError):
        return {}  



if __name__ == "__main__":
    test_logs = [
        'INFO:     127.0.0.1:54321 - "GET /api/users HTTP/1.1" 200 OK',
        'INFO:     192.168.1.100:45678 - "POST /api/auth/login HTTP/1.1" 401 Unauthorized',
        'INFO:     10.0.0.5:33333 - "PUT /api/users/123 HTTP/1.1" 200 OK',
        'INFO:     203.0.113.25:12345 - "DELETE /api/orders/456 HTTP/1.1" 204 No Content',
        'INFO:     172.16.0.1:8080 - "GET /health HTTP/1.1" 500 Internal Server Error'
    ]

    print("FastAPI Log Parsing Results:")
    for i, log_line in enumerate(test_logs, 1):
        parsed = parse_fastapi_log(log_line)
        print(f"\nLog {i}:")
        print(f"  Input: {log_line}")
        print(f"  Parsed: {parsed}")
