from fastapi import HTTPException


class OrganizationService:
    def admin_api_keys_list(
        self, after: str | None, order: str, limit: int | None
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def admin_api_keys_create(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def admin_api_keys_get(self, key_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def admin_api_keys_delete(self, key_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_audit_logs(
        self,
        effective_at: int | None,
        project_ids: list[str] | None,
        event_types: list[str] | None,
        actor_ids: list[str] | None,
        actor_emails: list[str] | None,
        resource_ids: list[str] | None,
        limit: int | None,
        after: str | None,
        before: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_organization_certificates(
        self, limit: int | None, after: str | None, order: str
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def upload_certificate(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def activate_organization_certificates(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def deactivate_organization_certificates(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def get_certificate(self, certificate_id: str, include: list[str] | None) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def modify_certificate(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def delete_certificate(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def usage_costs(
        self,
        start_time: int | None,
        end_time: int | None,
        bucket_width: str | None,
        project_ids: list[str] | None,
        group_by: list[str] | None,
        limit: int | None,
        page: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_invites(self, limit: int | None, after: str | None) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def invite_user(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def retrieve_invite(self, invite_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def delete_invite(self, invite_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_projects(
        self, limit: int | None, after: str | None, include_archived: bool | None
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def create_project(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def retrieve_project(self, project_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def modify_project(self, project_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_project_api_keys(
        self, project_id: str, limit: int | None, after: str | None
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def retrieve_project_api_key(self, project_id: str, key_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def delete_project_api_key(self, project_id: str, key_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def archive_project(self, project_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_project_certificates(
        self, project_id: str, limit: int | None, after: str | None, order: str
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def activate_project_certificates(self, project_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def deactivate_project_certificates(self, project_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_project_rate_limits(
        self, project_id: str, limit: int | None, after: str | None, before: str | None
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def update_project_rate_limits(self, project_id: str, rate_limit_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_project_service_accounts(
        self, project_id: str, limit: int | None, after: str | None
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def create_project_service_account(self, project_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def retrieve_project_service_account(
        self, project_id: str, service_account_id: str
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def delete_project_service_account(
        self, project_id: str, service_account_id: str
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_project_users(
        self, project_id: str, limit: int | None, after: str | None
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def create_project_user(self, project_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def retrieve_project_user(self, project_id: str, user_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def modify_project_user(self, project_id: str, user_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def delete_project_user(self, project_id: str, user_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def usage_audio_speeches(
        self,
        start_time: int | None,
        end_time: int | None,
        bucket_width: str | None,
        project_ids: list[str] | None,
        user_ids: list[str] | None,
        api_key_ids: list[str] | None,
        models: list[str] | None,
        group_by: list[str] | None,
        limit: int | None,
        page: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def usage_audio_transcriptions(
        self,
        start_time: int | None,
        end_time: int | None,
        bucket_width: str | None,
        project_ids: list[str] | None,
        user_ids: list[str] | None,
        api_key_ids: list[str] | None,
        models: list[str] | None,
        group_by: list[str] | None,
        limit: int | None,
        page: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def usage_code_interpreter_sessions(
        self,
        start_time: int | None,
        end_time: int | None,
        bucket_width: str | None,
        project_ids: list[str] | None,
        group_by: list[str] | None,
        limit: int | None,
        page: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def usage_completions(
        self,
        start_time: int | None,
        end_time: int | None,
        bucket_width: str | None,
        project_ids: list[str] | None,
        user_ids: list[str] | None,
        api_key_ids: list[str] | None,
        models: list[str] | None,
        batch: bool | None,
        group_by: list[str] | None,
        limit: int | None,
        page: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def usage_embeddings(
        self,
        start_time: int | None,
        end_time: int | None,
        bucket_width: str | None,
        project_ids: list[str] | None,
        user_ids: list[str] | None,
        api_key_ids: list[str] | None,
        models: list[str] | None,
        group_by: list[str] | None,
        limit: int | None,
        page: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def usage_images(
        self,
        start_time: int | None,
        end_time: int | None,
        bucket_width: str | None,
        project_ids: list[str] | None,
        user_ids: list[str] | None,
        api_key_ids: list[str] | None,
        models: list[str] | None,
        sources: list[str] | None,
        sizes: list[str] | None,
        group_by: list[str] | None,
        limit: int | None,
        page: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def usage_moderations(
        self,
        start_time: int | None,
        end_time: int | None,
        bucket_width: str | None,
        project_ids: list[str] | None,
        user_ids: list[str] | None,
        api_key_ids: list[str] | None,
        models: list[str] | None,
        group_by: list[str] | None,
        limit: int | None,
        page: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def usage_vector_stores(
        self,
        start_time: int | None,
        end_time: int | None,
        bucket_width: str | None,
        project_ids: list[str] | None,
        group_by: list[str] | None,
        limit: int | None,
        page: str | None,
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_users(
        self, limit: int | None, after: str | None, emails: list[str] | None
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def retrieve_user(self, user_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def modify_user(self, user_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def delete_user(self, user_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")
