from fastapi import HTTPException


class RealtimeService:
    def create_realtime_session(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def create_realtime_transcription_session(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")
