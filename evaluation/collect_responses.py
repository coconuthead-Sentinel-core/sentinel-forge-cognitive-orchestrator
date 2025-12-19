"""
Response collector for Sentinel Forge AI evaluation.
Calls the /api/chat endpoint with test queries and saves responses.
"""
import json
import requests
import time
import os
from pathlib import Path
from typing import Optional

# Try to import TestClient for in-process testing
TEST_CLIENT_AVAILABLE = False
TestClient = None
app = None


def load_queries(queries_path: str) -> list[dict]:
    """Load test queries from JSON file."""
    with open(queries_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def collect_response(base_url: str, query: str, context: str, api_key: str = None, use_test_client: bool = False) -> dict:
    """Call the AI chat endpoint and collect response."""
    if use_test_client and TEST_CLIENT_AVAILABLE:
        # Use TestClient for in-process testing
        client = TestClient(app)
        endpoint = "/api/chat"
        headers = {"Content-Type": "application/json"}
        if api_key:
            headers["X-API-Key"] = api_key
        
        payload = {
            "messages": [
                {"role": "system", "content": f"Context: {context}"},
                {"role": "user", "content": query}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        try:
            response = client.post(endpoint, json=payload, headers=headers)
            return {
                "success": True,
                "response": response.json(),
                "status_code": response.status_code
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "response": None
            }
    else:
        # Use HTTP requests
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
            response = requests.post(endpoint, json=payload, headers=headers, timeout=30)
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
    global TEST_CLIENT_AVAILABLE, TestClient, app
    
    # Add project root to path
    import sys
    sys.path.append(str(Path(__file__).parent.parent))
    
    # Try to import TestClient for in-process testing
    try:
        from fastapi.testclient import TestClient
        from backend.main import app
        TEST_CLIENT_AVAILABLE = True
        TestClient = TestClient
        app = app
        print("✅ TestClient available for in-process testing")
    except Exception as e:
        TEST_CLIENT_AVAILABLE = False
        print(f"⚠️ TestClient not available: {e}")
        print("   Falling back to HTTP requests")
    
    # Configuration
    base_url = "http://127.0.0.1:8000"
    eval_dir = Path(__file__).parent
    queries_file = eval_dir / "test_queries.json"
    responses_file = eval_dir / "test_responses.json"
    
    # Load API Key from env if available (for local testing)
    api_key = os.getenv("API_KEY")

    print("🚀 Starting response collection for Sentinel Forge AI...")
    
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
        
        result = collect_response(base_url, query_text, context, api_key, use_test_client=True)
        
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
