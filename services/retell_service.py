import os
import httpx
from schemas import UnifiedAgentRequest, UnifiedAgentResponse

RETELL_API_KEY = os.getenv("RETELL_API_KEY")
RETELL_BASE_URL = "https://api.retellai.com"

async def create_retell_agent(request: UnifiedAgentRequest) -> UnifiedAgentResponse:
    """
    Create an agent using the Retell API
    """
    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json",
        "Retell-Api-Version": "2024-03-05"
    }
    
    payload = {
        "agent_name": request.name,
        "llm_websocket_url": request.webhook_url,
        "voice_id": request.voice_config.voice_id,
        "voice_speed": request.voice_config.speed,
        "voice_temperature": request.llm_config.temperature,
        "voice_top_p": request.llm_config.top_p,
        "language_model": {
            "model": request.llm_config.model,
            "max_tokens": request.llm_config.max_tokens,
            "frequency_penalty": request.llm_config.frequency_penalty,
            "presence_penalty": request.llm_config.presence_penalty,
            "temperature": request.llm_config.temperature,
            "top_p": request.llm_config.top_p
        },
        "initial_message": request.first_message,
        "prompt": request.prompt,
        "enable_interruptions": request.interruptions_enabled,
        "silence_timeout_ms": request.silence_timeout_ms,
        "metadata": request.metadata
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{RETELL_BASE_URL}/create-agent",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        data = response.json()
        
        return UnifiedAgentResponse(
            agent_id=data["agent_id"],
            name=data["agent_name"],
            provider="retell",
            details=data
        )
