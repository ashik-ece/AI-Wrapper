from pydantic import BaseModel
from typing import Optional, Literal, List, Dict, Any

class LLMConfig(BaseModel):
    model: str = "gpt-3.5-turbo"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None

class VoiceConfig(BaseModel):
    voice_id: str
    speed: Optional[float] = 1.0
    pitch: Optional[float] = 1.0
    style: Optional[str] = None

class UnifiedAgentRequest(BaseModel):
    name: str
    description: Optional[str] = None
    llm_config: LLMConfig
    voice_config: VoiceConfig
    prompt: Optional[str] = None
    first_message: Optional[str] = None
    webhook_url: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    interruptions_enabled: Optional[bool] = True
    silence_timeout_ms: Optional[int] = 5000

class UnifiedAgentResponse(BaseModel):
    agent_id: str
    name: str
    provider: Literal["vapi", "retell"]
    details: Dict[str, Any]
