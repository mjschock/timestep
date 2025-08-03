from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import TypeAdapter

from backend.services.responses_service import ResponsesService
from openai.types.responses import Response as ResponsesAPIResponse
from openai.types.responses.response_create_params import (
    ResponseCreateParamsNonStreaming,
    ResponseCreateParamsStreaming,
)

responses_router = APIRouter()


@responses_router.post("/responses")
async def create_response(
    request: Request,
    service: ResponsesService = Depends(ResponsesService),  # noqa: B008
):
    """
    Creates a model response. Provide [text](/docs/guides/text) or
    [image](/docs/guides/images) inputs to generate [text](/docs/guides/text)
    or [JSON](/docs/guides/structured-outputs) outputs. Have the model call
    your own [custom code](/docs/guides/function-calling) or use built-in
    [tools](/docs/guides/tools) like [web search](/docs/guides/tools-web-search)
    or [file search](/docs/guides/tools-file-search) to use your own data
    as input for the model's response.
    """
    try:
        body = await request.json()

        # Validate the entire request using OpenAI Responses API types
        try:
            # Check if streaming is requested to use the correct validation model
            is_streaming = body.get("stream", False)
            
            if is_streaming:
                adapter = TypeAdapter(ResponseCreateParamsStreaming)
                validated_request = adapter.validate_python(body)
            else:
                adapter = TypeAdapter(ResponseCreateParamsNonStreaming)
                validated_request = adapter.validate_python(body)
                
            validated_body = dict(validated_request)
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Invalid request format: {e}"
            ) from e

        result = await service.create_response(validated_body)

        # Validate the response using OpenAI Responses API types
        if isinstance(result, dict):
            try:
                validated_response = ResponsesAPIResponse.model_validate(result)
                result = validated_response.model_dump(exclude_unset=True)
            except Exception as e:
                # Log the error but don't expose internal details
                raise HTTPException(
                    status_code=500,
                    detail="Internal server error: invalid response format",
                ) from e

        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {e}"
        ) from e


@responses_router.get("/responses/{response_id}")
def get_response(
    response_id: str,
    include: list[str],
    stream: str,
    starting_after: str,
    request: Request,
    service: ResponsesService = Depends(ResponsesService),  # noqa: B008
):
    """Retrieves a model response with the given ID."""
    return service.get_response(response_id, include, stream, starting_after)


@responses_router.delete("/responses/{response_id}")
def delete_response(
    response_id: str,
    request: Request,
    service: ResponsesService = Depends(ResponsesService),  # noqa: B008
):
    """Deletes a model response with the given ID."""
    return service.delete_response(response_id)


@responses_router.post("/responses/{response_id}/cancel")
def cancel_response(
    response_id: str,
    request: Request,
    service: ResponsesService = Depends(ResponsesService),  # noqa: B008
):
    """
    Cancels a model response with the given ID. Only responses created with
    the `background` parameter set to `true` can be cancelled.
    [Learn more](/docs/guides/background).
    """
    return service.cancel_response(response_id)


@responses_router.get("/responses/{response_id}/input_items")
def list_input_items(
    response_id: str,
    limit: str,
    order: str,
    after: str,
    before: str,
    include: list[str],
    request: Request,
    service: ResponsesService = Depends(ResponsesService),  # noqa: B008
):
    """Returns a list of input items for a given response."""
    return service.list_input_items(response_id, limit, order, after, before, include)
