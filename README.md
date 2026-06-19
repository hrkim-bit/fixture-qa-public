# yuanta-qa-public

Multi-language vulnerable fixture for IVAS QA (Python + Java + Docker).

> ⚠️ 의도적으로 취약하게 작성된 테스트 픽스처입니다. 절대 운영 환경에 사용하지 마세요.
> 모든 시크릿/키는 형식만 진짜 같은 **가짜 값**입니다.

## 의도된 취약점

### Python (`app.py`, `src/utils.py`)
- Flask 라우트는 **명명된 함수** — IVAS 함수 매칭용
- `src/utils.py`는 `app.py`에서 import 후 `/extract`, `/utils-hash`, `/encrypt` 라우트로 **호출 연결**

### Java (`src/main/java/ai/labradorlabs/qa/VulnUtils.java`)
- SQL Injection, Path Traversal, 역직렬화, 약한 해시 — **명명된 static 메서드**
- YAML 역직렬화 RCE — `yaml.load(user_input)`
- Pickle 역직렬화 — `pickle.loads(request.data)`
- Command Injection — `subprocess.check_output(..., shell=True)`
- SQL Injection — f-string 쿼리 조립
- SSTI — Jinja2 `Template(user_input).render()`
- Path Traversal — 검증 없는 `open()`
- SSRF — `requests.get(user_url)`
- 약한 해시 — `hashlib.md5()`
- Flask `debug=True` + `0.0.0.0` 바인딩
- 하드코딩 시크릿

### 의존성
- `requirements.txt` — 알려진 CVE 보유 Python 패키지 구버전
- `pom.xml` — log4j, jackson-databind 등 취약 Java 라이브러리

### Docker
- `Dockerfile` — root 실행, `latest` 태그, ENV 시크릿 노출
