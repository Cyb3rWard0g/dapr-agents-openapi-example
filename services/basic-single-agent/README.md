# Basic Agent Test

```bash
python3 server.py --debug
```

```
INFO:     127.0.0.1:57846 - "GET /openapi.json HTTP/1.1" 200 OK
2025-04-21 02:14:53,756 - calculator-api - INFO - Adding 2.0 and 2.0
INFO:     127.0.0.1:57852 - "GET /add?a=2&b=2 HTTP/1.1" 200 OK
2025-04-21 02:14:54,773 - calculator-api - INFO - Multiplying 5.0 and 5.0
INFO:     127.0.0.1:57854 - "GET /multiply?a=5&b=5 HTTP/1.1" 200 OK
2025-04-21 02:14:56,438 - calculator-api - INFO - Dividing 2.4 by 2.0
INFO:     127.0.0.1:57855 - "GET /divide?a=2.4&b=2 HTTP/1.1" 200 OK
2025-04-21 02:14:57,591 - calculator-api - INFO - Adding -34.0 and 10.0
INFO:     127.0.0.1:57857 - "GET /add?a=-34&b=10 HTTP/1.1" 200 OK
2025-04-21 02:14:58,638 - calculator-api - INFO - Multiplying 2.9283 and 2.23234
INFO:     127.0.0.1:57858 - "GET /multiply?a=2.9283&b=2.23234 HTTP/1.1" 200 OK
```