from  typing import List, Dict, Any, Optional
from pydantic import BaseModel, HttpUrl, Field
from app.simulations.utils import HTTPMethod

class DDoSParams(BaseModel):
    target_url: HttpUrl
    num_requests: int = Field(1000, gt=0, le=50000, description="Total number of requests to be sent")
    concurrency: int = Field(50, gt=0, le=500, description="Number of concurrent request workers")
    method: HTTPMethod = Field(HTTPMethod.GET, description="HTTP method to use")
    payload: Optional[Dict[str, Any]] = Field(None, description="JSON payload for POST requests")
    headers: Optional[Dict[str, str]] = Field(None, description="Custom HTTP headers")
    timeout_seconds: float = Field(10.0, gt=0, description="Timeout for each request (seconds)")
    random_delay_ms_max: int = Field(0, ge=0, le=1000, description="Maximum random delay between requests (milliseconds, 0 = off)")

class BruteForceParams(BaseModel):
    target_url: HttpUrl
    usernames: List[str] = Field(default_factory=lambda: ["admin", "user", "testuser", "root"])
    passwords: List[str] = Field(default_factory=lambda: ["password", "123456", "admin", "qwerty", "test"])
    success_text_indicator: Optional[str] = Field(None, description="Text to search for in the response on successful login (case insensitive)")
    success_status_code: Optional[int] = Field(None, description="HTTP status code of successful login (e.g., 200, 302)")
    username_field: str = Field("username", description="The name of the username field in the form")
    password_field: str = Field("password", description="Name of the password field in the form")
    concurrency: int = Field(5, gt=0, le=20, description="Number of passwords to try concurrently (for each user)")
    stop_on_first_success: bool = Field(True, description="Stop all attempts on first successful login for any user")

class SQLInjectionParams(BaseModel):
    target_url: HttpUrl
    param_to_inject: str = Field(description="Parameter name where the payload will be injected (URL query or POST form field)")
    method: HTTPMethod = Field(HTTPMethod.GET, description="HTTP method to use")
    other_post_data: Optional[Dict[str, str]] = Field(None, description="Other form data for POST (excluding the parameter to be injected)")
    base_value_for_param: Optional[str] = Field(None, description="Base value of the parameter to be injected (payload can be appended/prepended to it)")
    payload_categories: List[str] = Field(default_factory=lambda: ["error_based", "boolean_based", "time_based_light", "union_light"])
    error_indicator_texts: List[str] = Field(default_factory=lambda: ["sql syntax", "unclosed quotation mark", "odbc driver error", "mysql_fetch_array()", "you have an error in your sql syntax"])
