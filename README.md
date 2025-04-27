# AI Agent Wrapper API

This API provides a unified interface for creating AI agents across different providers (Vapi and Retell).

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables:
   - `VAPI_API_KEY`: Your Vapi API key
   - `RETELL_API_KEY`: Your Retell API key
4. Run the server: `uvicorn main:app --reload`

## API Endpoint

### Create Agent

`POST /create-agent`

Parameters:
- `request`: UnifiedAgentRequest object with agent configuration
- `provider`: Either "vapi" or "retell" (default: "vapi")

Example request body:
```json
{
    "name": "Customer Support Agent",
    "description": "Handles customer inquiries",
    "llm_config": {
        "model": "gpt-3.5-turbo",
        "temperature": 0.7
    },
    "voice_config": {
        "voice_id": "21m00Tcm4TlvDq8ikWAM",
        "speed": 1.0
    },
    "prompt": "You are a helpful customer support agent...",
    "first_message": "Hello! How can I help you today?"
}
