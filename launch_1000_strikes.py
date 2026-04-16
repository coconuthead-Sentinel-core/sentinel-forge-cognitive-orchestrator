import httpx
import asyncio
import time

async def launch():
    print("⏳ Waiting for API to warm up...")
    await asyncio.sleep(3)
    
    async with httpx.AsyncClient() as client:
        try:
            print("🚀 Initiating 1000 Strikes Protocol via CNO-AX Engine...")
            response = await client.post("http://localhost:8000/api/simulation/cno-ax/start")
            if response.status_code == 200:
                print(f"✅ Success: {response.json()}")
            else:
                print(f"❌ Failed: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Connection Error: {e}")
            print("Ensure the backend server is running (uvicorn backend.main:app).")

if __name__ == "__main__":
    asyncio.run(launch())
