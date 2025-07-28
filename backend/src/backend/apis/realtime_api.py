from fastapi import APIRouter, Depends, Request

from backend.services.realtime_service import RealtimeService

realtime_router = APIRouter()


@realtime_router.post("/realtime/sessions")
def create_realtime_session(
    request: Request,
    service: RealtimeService = Depends(RealtimeService),  # noqa: B008
) -> None:
    """
    Create an ephemeral API token for use in client-side applications with the
    Realtime API. Can be configured with the same session parameters as the
    `session.update` client event.

    It responds with a session object, plus a `client_secret` key which contains
    a usable ephemeral API token that can be used to authenticate browser clients
    for the Realtime API.
    """
    return service.create_realtime_session()


@realtime_router.post("/realtime/transcription_sessions")
def create_realtime_transcription_session(
    request: Request,
    service: RealtimeService = Depends(RealtimeService),  # noqa: B008
) -> None:
    """
    Create an ephemeral API token for use in client-side applications with the
    Realtime API specifically for realtime transcriptions.
    Can be configured with the same session parameters as the `transcription_session.update` client event.

    It responds with a session object, plus a `client_secret` key which contains
    a usable ephemeral API token that can be used to authenticate browser clients
    for the Realtime API.
    """
    return service.create_realtime_transcription_session()
