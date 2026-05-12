import httpx
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

# SOVEREIGN AI - SECURE API GATEWAY & RBAC ROUTER
app = FastAPI(title="Sovereign AI Gateway")

# Internal routing to the localized Ollama inference engine
OLLAMA_LOCAL_URL = "http://localhost:11434/api/generate"

# Mock Institutional Access Control List (ACL)
AUTHORIZED_ROLES = {
    "doctor_token_778": {"role": "medical_staff", "models": ["llama3.2", "meditron"]},
    "student_token_112": {"role": "student", "models": ["llama3.2"]},
}

class PromptPayload(BaseModel):
    model: str
    prompt: str
    stream: bool = False

@app.post("/secure-generate")
async def route_to_inference_engine(payload: PromptPayload, x_auth_token: str = Header(...)):
    """
    Intercepts frontend requests, validates RBAC clearance, 
    and routes to the hardware-optimized Ollama backend.
    """
    print(f"[SYSTEM] Incoming generation request for model: {payload.model}")
    
    # 1. Execute Role-Based Access Control (RBAC) Validation
    user_session = AUTHORIZED_ROLES.get(x_auth_token)
    if not user_session:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid Institutional Token")
        
    if payload.model not in user_session["models"]:
        print(f"[SECURITY WARNING] Role '{user_session['role']}' attempted to access restricted model '{payload.model}'")
        raise HTTPException(status_code=403, detail="Forbidden: Clearance level too low for this tensor model.")

    # 2. Route the validated payload to the localized C++ Tensor Engine
    print("[SYSTEM] RBAC cleared. Routing payload to local Ollama instance...")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                OLLAMA_LOCAL_URL,
                json={
                    "model": payload.model,
                    "prompt": payload.prompt,
                    "stream": payload.stream
                },
                timeout=120.0 # Extended timeout for VRAM swapping
            )
            response.raise_for_status()
            
            print("[SUCCESS] Inference complete. Returning tokens to frontend.")
            return response.json()
            
    except httpx.RequestError as e:
        print(f"[HARDWARE ERROR] Inference engine failed to respond: {e}")
        raise HTTPException(status_code=503, detail="Service Unavailable: GTX 1650 may be experiencing VRAM overflow.")

if __name__ == "__main__":
    import uvicorn
    # Boot the gateway on localhost
    uvicorn.run(app, host="0.0.0.0", port=8000)