#!/usr/bin/env python3
import json
import sys
import time
from dapr.clients import DaprClient

# Default Pub/Sub component
PUBSUB_NAME = "pubsub"

def main(agent_topic, max_attempts=10, retry_delay=1):
    """
    Publishes a task to a specified Dapr Pub/Sub topic with retries.

    Args:
        agent_topic (str): The name of the orchestrator topic.
        max_attempts (int): Maximum number of retry attempts.
        retry_delay (int): Delay in seconds between attempts.
    """
    task_message = {
        "task": "Precisely calculate with available tools: 2 + 2, 5*5, 2.4 / 2, -34 + 10, and 2.9283 * 2.23234",
    }

    time.sleep(5)

    attempt = 1

    while attempt <= max_attempts:
        try:
            print(f"📢 Attempt {attempt}: Publishing to topic '{agent_topic}'...")
            
            with DaprClient() as client:
                client.publish_event(
                    pubsub_name=PUBSUB_NAME,
                    topic_name=agent_topic,
                    data=json.dumps(task_message),
                    data_content_type="application/json",
                    publish_metadata={
                        "cloudevent.type": "TriggerAction",
                    }
                )

            print(f"✅ Successfully published request to '{agent_topic}'")
            sys.exit(0)

        except Exception as e:
            print(f"❌ Request failed: {e}")
        
        attempt += 1
        print(f"⏳ Waiting {retry_delay}s before next attempt...")
        time.sleep(retry_delay)

    print(f"❌ Maximum attempts ({max_attempts}) reached without success.")
    sys.exit(1)

if __name__ == "__main__":
    main("CalculatorOpenAPIReActAgent")