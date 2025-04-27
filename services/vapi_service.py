import os
import httpx
from schemas import UnifiedAgentRequest, UnifiedAgentResponse

VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_BASE_URL = "https://api.vapi.ai"

async def create_vapi_agent(request: UnifiedAgentRequest) -> UnifiedAgentResponse:
    """
    Create an agent using the Vapi API
    """
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": request.name,
        "description": request.description,
        "model": {
            "provider": "openai",
            "model": request.llm_config.model,
            "temperature": request.llm_config.temperature,
            "maxTokens": request.llm_config.max_tokens,
            "topP": request.llm_config.top_p,
            "frequencyPenalty": request.llm_config.frequency_penalty,
            "presencePenalty": request.llm_config.presence_penalty
        },
        "voice": {
            "provider": "11labs",
            "voiceId": request.voice_config.voice_id,
            "speed": request.voice_config.speed,
            "pitch": request.voice_config.pitch
        },
        "firstMessage": request.first_message,
        "prompt": request.prompt,
        "interruptionsEnabled": request.interruptions_enabled,
        "silenceTimeoutMs": request.silence_timeout_ms,
        "metadata": request.metadata
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{VAPI_BASE_URL}/assistant",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        data = response.json()
        
        return UnifiedAgentResponse(
            agent_id=data["id"],
            name=data["name"],
            provider="vapi",
            details=data
        )
