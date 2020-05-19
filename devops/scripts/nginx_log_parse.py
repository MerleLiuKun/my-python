"""
    Nginx 日志解析
"""
from dataclasses import dataclass

@dataclass
class LogInfo:
    req: str
    body: str
    ua: str

def parse_log_log():
    """
    follow by http://desert3.iteye.com/blog/1001568
    """
    ip_p = r"?P<ip>[\d.]*"
    time_p = r"?P<time>\[[^\[\]]*\]"
    request_p = r"?P<request>\"[^\"]*\""
    status_p = r"?P<status>\d+"
    body_bytes_p = r"?P<bodyByteSent>\d+"
    body_p = r"?P<pBody>.*"
    refer_p = r"?P<refer>\"[^\"]*\""
    user_agent_p = r"?P<userAgent>\"[^\"]*\""

    log_pattern = re.compile(
        r"({ip}) - - ({time}) ({req}) ({status}) ({body}) ({body_p}) ({refer}) ({ua})".format(
            ip=ip_p, time=time_p, req=request_p, status=status_p,
            body=body_bytes_p, body_p=body_p, refer=refer_p, ua=user_agent_p)
    )
    result = log_pattern.match(line)
    if result:
        log_line = LogInfo(
            req=result.group('request'),
            body=result.group("pBody"),
            ua=result.group('userAgent')
        )
        return log_line
