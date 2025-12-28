"""
Response collector for Sentinel Forge AI evaluation.
Calls the /api/chat endpoint with test queries and saves responses.
Uses real HTTP requests for true integration testing.
"""
import json
import requests
import time
import os
from pathlib import Path
from typing import Optional


def load_queries(queries_path: str) -> list[dict]:
    """Load test queries from JSON file."""
    with open(queries_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def collect_response(base_url: str, query: str, context: str, api_key: str = None, timeout: int = 30) -> dict:
    """Call the AI chat endpoint and collect response via HTTP."""
    endpoint = f"{base_url}/api/chat"
    
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["X-API-Key"] = api_key

    # Sentinel Forge ChatRequest schema
    payload = {
        "messages": [
            {"role": "system", "content": f"Context: {context}"},
            {"role": "user", "content": query}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=timeout)
        response.raise_for_status()
        return {
            "success": True,
            "response": response.json(),
            "status_code": response.status_code
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e),
            "response": None
        }


def main():
    # Configuration - Use real HTTP requests for true integration testing
    base_url = "http://127.0.0.1:8000"
    eval_dir = Path(__file__).parent
    queries_file = eval_dir / "test_queries.json"
    responses_file = eval_dir / "test_responses.json"
    
    # Load configuration from environment
    api_key = os.getenv("API_KEY")
    timeout = int(os.getenv("HTTP_TIMEOUT", "30"))

    print("🚀 Starting response collection for Sentinel Forge AI...")
    print("   Using HTTP requests for true integration testing")
    
    if not queries_file.exists():
        print(f"❌ Error: {queries_file} not found.")
        return

    queries = load_queries(str(queries_file))
    print(f"✅ Loaded {len(queries)} test queries")
    
    responses = []
    print("\n📡 Collecting responses from API...")
    
    for i, query_data in enumerate(queries, 1):
        query_id = query_data["id"]
        query_text = query_data["query"]
        context = query_data.get("context", "")
        
        print(f"[{i}/{len(queries)}] {query_id}: {query_text[:50]}...")
        
        result = collect_response(base_url, query_text, context, api_key, timeout)
        
        response_entry = {
            "query_id": query_id,
            "query": query_text,
            "context": context,
            "expected_intent": query_data.get("expected_intent"),
            "timestamp": time.time(),
            "success": result["success"]
        }
        
        if result["success"]:
            # Extract content from ChatResponse schema
            chat_resp = result["response"]
            # Handle different response shapes if necessary
            content = chat_resp.get("choices", [{}])[0].get("message", {}).get("content", "")
            response_entry["response"] = content
            print(f"   ✅ Got response ({len(content)} chars)")
        else:
            response_entry["error"] = result.get("error", "Unknown error")
            print(f"   ❌ Failed: {response_entry['error']}")
        
        responses.append(response_entry)
        time.sleep(0.2) # Rate limit protection
    
    print(f"\n💾 Saving responses to: {responses_file}")
    with open(responses_file, 'w', encoding='utf-8') as f:
        json.dump(responses, f, indent=2, ensure_ascii=False)
    
    print("🎯 Collection complete!")


if __name__ == "__main__":
    main()
