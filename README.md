# dapr-agents-openapi-example

## How to run

1. Launch calculator with API and OpenAPI specification

```
cd services/calculator_api
python3 server.py --debug
````

2. Launch app in Dapr:

```
dapr run --app-id CalculatorAgentApp --app-port 8003 --resources-path ./components/ -- python ./services/calculator_openapi_agent/app.py
```

3. Request task:

```
dapr run --app-id MessagingClientApp --resources-path ./components/ -- python ./services/messaging_client/app.py
```
