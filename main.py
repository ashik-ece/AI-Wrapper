from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Literal
from services.vapi_service import create_vapi_agent
from services.retell_service import create_retell_agent
from schemas import UnifiedAgentRequest, UnifiedAgentResponse

app = FastAPI(title="AI Agent Wrapper API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/create-agent", response_model=UnifiedAgentResponse)
async def create_agent(
    request: UnifiedAgentRequest,
    provider: Literal["vapi", "retell"] = "vapi"
):
    """
    Unified endpoint to create an AI agent with either Vapi or Retell as the provider.
    
    Args:
        request: Unified agent configuration parameters
        provider: Which provider to use ('vapi' or 'retell')
    
    Returns:
        UnifiedAgentResponse with created agent details
    """
    try:
        if provider == "vapi":
            response = await create_vapi_agent(request)
        elif provider == "retell":
            response = await create_retell_agent(request)
        else:
            raise HTTPException(status_code=400, detail="Invalid provider specified")
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
