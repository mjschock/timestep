from fastapi import APIRouter, Depends, Request

from backend.services.organization_service import OrganizationService

organization_router = APIRouter()


@organization_router.get("/organization/admin_api_keys")
def admin_api_keys_list(
    after: str,
    order: str,
    limit: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """List organization API keys"""
    return service.admin_api_keys_list(
        after=after, order=order, limit=int(limit) if limit else None
    )


@organization_router.post("/organization/admin_api_keys")
def admin_api_keys_create(
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Create an organization admin API key"""
    return service.admin_api_keys_create()


@organization_router.get("/organization/admin_api_keys/{key_id}")
def admin_api_keys_get(
    key_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Retrieve a single organization API key"""
    return service.admin_api_keys_get(key_id=key_id)


@organization_router.delete("/organization/admin_api_keys/{key_id}")
def admin_api_keys_delete(
    key_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Delete an organization admin API key"""
    return service.admin_api_keys_delete(key_id=key_id)


@organization_router.get("/organization/audit_logs")
def list_audit_logs(
    effective_at: str,
    project_ids: list[str],
    event_types: list[str],
    actor_ids: list[str],
    actor_emails: list[str],
    resource_ids: list[str],
    limit: str,
    after: str,
    before: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """List user actions and configuration changes within this organization."""
    return service.list_audit_logs(
        effective_at=int(effective_at) if effective_at else None,
        project_ids=project_ids,
        event_types=event_types,
        actor_ids=actor_ids,
        actor_emails=actor_emails,
        resource_ids=resource_ids,
        limit=int(limit) if limit else None,
        after=after,
        before=before,
    )


@organization_router.get("/organization/certificates")
def list_organization_certificates(
    limit: str,
    after: str,
    order: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """List uploaded certificates for this organization."""
    return service.list_organization_certificates(
        limit=int(limit) if limit else None, after=after, order=order
    )


@organization_router.post("/organization/certificates")
def upload_certificate(
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Upload a certificate to the organization. This does **not** automatically activate the certificate.

    Organizations can upload up to 50 certificates.
    """
    return service.upload_certificate()


@organization_router.post("/organization/certificates/activate")
def activate_organization_certificates(
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Activate certificates at the organization level.

    You can atomically and idempotently activate up to 10 certificates at a time.
    """
    return service.activate_organization_certificates()


@organization_router.post("/organization/certificates/deactivate")
def deactivate_organization_certificates(
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Deactivate certificates at the organization level.

    You can atomically and idempotently deactivate up to 10 certificates at a time.
    """
    return service.deactivate_organization_certificates()


@organization_router.get("/organization/certificates/{certificate_id}")
def get_certificate(
    certificate_id: str,
    include: list[str],
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Get a certificate that has been uploaded to the organization.

    You can get a certificate regardless of whether it is active or not.
    """
    return service.get_certificate(certificate_id=certificate_id, include=include)


@organization_router.post("/organization/certificates/{certificate_id}")
def modify_certificate(
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Modify a certificate. Note that only the name can be modified."""
    return service.modify_certificate()


@organization_router.delete("/organization/certificates/{certificate_id}")
def delete_certificate(
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Delete a certificate from the organization.

    The certificate must be inactive for the organization and all projects.
    """
    return service.delete_certificate()


@organization_router.get("/organization/costs")
def usage_costs(
    start_time: str,
    end_time: str,
    bucket_width: str,
    project_ids: list[str],
    group_by: list[str],
    limit: str,
    page: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Get costs details for the organization."""
    return service.usage_costs(
        start_time=int(start_time) if start_time else None,
        end_time=int(end_time) if end_time else None,
        bucket_width=bucket_width,
        project_ids=project_ids,
        group_by=group_by,
        limit=int(limit) if limit else None,
        page=page,
    )


@organization_router.get("/organization/invites")
def list_invites(
    limit: str,
    after: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Returns a list of invites in the organization."""
    return service.list_invites(limit=int(limit) if limit else None, after=after)


@organization_router.post("/organization/invites")
def invite_user(request: Request, service: OrganizationService = Depends()) -> None:  # noqa: B008
    """
    Create an invite for a user to the organization. The invite must be accepted by the user before they have access to the organization.
    """
    return service.invite_user()


@organization_router.get("/organization/invites/{invite_id}")
def retrieve_invite(
    invite_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Retrieves an invite."""
    return service.retrieve_invite(invite_id=invite_id)


@organization_router.delete("/organization/invites/{invite_id}")
def delete_invite(
    invite_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Delete an invite. If the invite has already been accepted, it cannot be deleted.
    """
    return service.delete_invite(invite_id=invite_id)


@organization_router.get("/organization/projects")
def list_projects(
    limit: str,
    after: str,
    include_archived: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Returns a list of projects."""
    return service.list_projects(
        limit=int(limit) if limit else None,
        after=after,
        include_archived=include_archived == "true" if include_archived else None,
    )


@organization_router.post("/organization/projects")
def create_project(request: Request, service: OrganizationService = Depends()) -> None:  # noqa: B008
    """
    Create a new project in the organization. Projects can be created and archived, but cannot be deleted.
    """
    return service.create_project()


@organization_router.get("/organization/projects/{project_id}")
def retrieve_project(
    project_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Retrieves a project."""
    return service.retrieve_project(project_id=project_id)


@organization_router.post("/organization/projects/{project_id}")
def modify_project(
    project_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Modifies a project in the organization."""
    return service.modify_project(project_id=project_id)


@organization_router.get("/organization/projects/{project_id}/api_keys")
def list_project_api_keys(
    project_id: str,
    limit: str,
    after: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Returns a list of API keys in the project."""
    return service.list_project_api_keys(
        project_id=project_id, limit=int(limit) if limit else None, after=after
    )


@organization_router.get("/organization/projects/{project_id}/api_keys/{key_id}")
def retrieve_project_api_key(
    project_id: str,
    key_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Retrieves an API key in the project."""
    return service.retrieve_project_api_key(project_id=project_id, key_id=key_id)


@organization_router.delete("/organization/projects/{project_id}/api_keys/{key_id}")
def delete_project_api_key(
    project_id: str,
    key_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Deletes an API key from the project."""
    return service.delete_project_api_key(project_id=project_id, key_id=key_id)


@organization_router.post("/organization/projects/{project_id}/archive")
def archive_project(
    project_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Archives a project in the organization. Archived projects cannot be used or updated.
    """
    return service.archive_project(project_id=project_id)


@organization_router.get("/organization/projects/{project_id}/certificates")
def list_project_certificates(
    project_id: str,
    limit: str,
    after: str,
    order: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """List certificates for this project."""
    return service.list_project_certificates(
        project_id=project_id,
        limit=int(limit) if limit else None,
        after=after,
        order=order,
    )


@organization_router.post("/organization/projects/{project_id}/certificates/activate")
def activate_project_certificates(
    project_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Activate certificates at the project level.

    You can atomically and idempotently activate up to 10 certificates at a time.
    """
    return service.activate_project_certificates(project_id=project_id)


@organization_router.post("/organization/projects/{project_id}/certificates/deactivate")
def deactivate_project_certificates(
    project_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Deactivate certificates at the project level. You can atomically and
    idempotently deactivate up to 10 certificates at a time.
    """
    return service.deactivate_project_certificates(project_id=project_id)


@organization_router.get("/organization/projects/{project_id}/rate_limits")
def list_project_rate_limits(
    project_id: str,
    limit: str,
    after: str,
    before: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Returns the rate limits per model for a project."""
    return service.list_project_rate_limits(
        project_id=project_id,
        limit=int(limit) if limit else None,
        after=after,
        before=before,
    )


@organization_router.post(
    "/organization/projects/{project_id}/rate_limits/{rate_limit_id}",
)
def update_project_rate_limits(
    project_id: str,
    rate_limit_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Updates a project rate limit."""
    return service.update_project_rate_limits(
        project_id=project_id, rate_limit_id=rate_limit_id
    )


@organization_router.get("/organization/projects/{project_id}/service_accounts")
def list_project_service_accounts(
    project_id: str,
    limit: str,
    after: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Returns a list of service accounts in the project."""
    return service.list_project_service_accounts(
        project_id=project_id, limit=int(limit) if limit else None, after=after
    )


@organization_router.post("/organization/projects/{project_id}/service_accounts")
def create_project_service_account(
    project_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """
    Creates a new service account in the project. This also returns an unredacted API key for the service account.
    """
    return service.create_project_service_account(project_id=project_id)


@organization_router.get(
    "/organization/projects/{project_id}/service_accounts/{service_account_id}",
)
def retrieve_project_service_account(
    project_id: str,
    service_account_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Retrieves a service account in the project."""
    return service.retrieve_project_service_account(
        project_id=project_id, service_account_id=service_account_id
    )


@organization_router.delete(
    "/organization/projects/{project_id}/service_accounts/{service_account_id}",
)
def delete_project_service_account(
    project_id: str,
    service_account_id: str,
    request: Request,
    service: OrganizationService = Depends(),  # noqa: B008
) -> None:
    """Deletes a service account from the project."""
    return service.delete_project_service_account(
        project_id=project_id, service_account_id=service_account_id
    )


@organization_router.get("/organization/projects/{project_id}/users")
def list_project_users(
    project_id: str,
    limit: str,
    after: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Returns a list of users in the project."""
    return service.list_project_users(
        project_id=project_id, limit=int(limit) if limit else None, after=after
    )


@organization_router.post("/organization/projects/{project_id}/users")
def create_project_user(
    project_id: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """
    Adds a user to the project. Users must already be members of the organization to be added to a project.
    """
    return service.create_project_user(project_id=project_id)


@organization_router.get("/organization/projects/{project_id}/users/{user_id}")
def retrieve_project_user(
    project_id: str,
    user_id: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Retrieves a user in the project."""
    return service.retrieve_project_user(project_id=project_id, user_id=user_id)


@organization_router.post("/organization/projects/{project_id}/users/{user_id}")
def modify_project_user(
    project_id: str,
    user_id: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Modifies a user's role in the project."""
    return service.modify_project_user(project_id=project_id, user_id=user_id)


@organization_router.delete("/organization/projects/{project_id}/users/{user_id}")
def delete_project_user(
    project_id: str,
    user_id: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Deletes a user from the project."""
    return service.delete_project_user(project_id=project_id, user_id=user_id)


@organization_router.get("/organization/usage/audio_speeches")
def usage_audio_speeches(
    start_time: str,
    end_time: str,
    bucket_width: str,
    project_ids: list[str],
    user_ids: list[str],
    api_key_ids: list[str],
    models: list[str],
    group_by: list[str],
    limit: str,
    page: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Get audio speeches usage details for the organization."""
    return service.usage_audio_speeches(
        start_time=int(start_time) if start_time else None,
        end_time=int(end_time) if end_time else None,
        bucket_width=bucket_width,
        project_ids=project_ids,
        user_ids=user_ids,
        api_key_ids=api_key_ids,
        models=models,
        group_by=group_by,
        limit=int(limit) if limit else None,
        page=page,
    )


@organization_router.get("/organization/usage/audio_transcriptions")
def usage_audio_transcriptions(
    start_time: str,
    end_time: str,
    bucket_width: str,
    project_ids: list[str],
    user_ids: list[str],
    api_key_ids: list[str],
    models: list[str],
    group_by: list[str],
    limit: str,
    page: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Get audio transcriptions usage details for the organization."""
    return service.usage_audio_transcriptions(
        start_time=int(start_time) if start_time else None,
        end_time=int(end_time) if end_time else None,
        bucket_width=bucket_width,
        project_ids=project_ids,
        user_ids=user_ids,
        api_key_ids=api_key_ids,
        models=models,
        group_by=group_by,
        limit=int(limit) if limit else None,
        page=page,
    )


@organization_router.get("/organization/usage/code_interpreter_sessions")
def usage_code_interpreter_sessions(
    start_time: str,
    end_time: str,
    bucket_width: str,
    project_ids: list[str],
    user_ids: list[str],
    api_key_ids: list[str],
    models: list[str],
    group_by: list[str],
    limit: str,
    page: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Get code interpreter sessions usage details for the organization."""
    return service.usage_code_interpreter_sessions(
        start_time=int(start_time) if start_time else None,
        end_time=int(end_time) if end_time else None,
        bucket_width=bucket_width,
        project_ids=project_ids,
        group_by=group_by,
        limit=int(limit) if limit else None,
        page=page,
    )


@organization_router.get("/organization/usage/completions")
def usage_completions(
    start_time: str,
    end_time: str,
    bucket_width: str,
    project_ids: list[str],
    user_ids: list[str],
    api_key_ids: list[str],
    models: list[str],
    group_by: list[str],
    limit: str,
    page: str,
    request: Request,
    batch: str = None,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Get completions usage details for the organization."""
    return service.usage_completions(
        start_time=int(start_time) if start_time else None,
        end_time=int(end_time) if end_time else None,
        bucket_width=bucket_width,
        project_ids=project_ids,
        user_ids=user_ids,
        api_key_ids=api_key_ids,
        models=models,
        batch=batch == "true" if batch else None,
        group_by=group_by,
        limit=int(limit) if limit else None,
        page=page,
    )


@organization_router.get("/organization/usage/embeddings")
def usage_embeddings(
    start_time: str,
    end_time: str,
    bucket_width: str,
    project_ids: list[str],
    user_ids: list[str],
    api_key_ids: list[str],
    models: list[str],
    group_by: list[str],
    limit: str,
    page: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Get embeddings usage details for the organization."""
    return service.usage_embeddings(
        start_time=int(start_time) if start_time else None,
        end_time=int(end_time) if end_time else None,
        bucket_width=bucket_width,
        project_ids=project_ids,
        user_ids=user_ids,
        api_key_ids=api_key_ids,
        models=models,
        group_by=group_by,
        limit=int(limit) if limit else None,
        page=page,
    )


@organization_router.get("/organization/usage/images")
def usage_images(
    start_time: str,
    end_time: str,
    bucket_width: str,
    sources: list[str],
    sizes: list[str],
    project_ids: list[str],
    user_ids: list[str],
    api_key_ids: list[str],
    models: list[str],
    group_by: list[str],
    limit: str,
    page: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Get images usage details for the organization."""
    return service.usage_images(
        start_time=int(start_time) if start_time else None,
        end_time=int(end_time) if end_time else None,
        bucket_width=bucket_width,
        sources=sources,
        sizes=sizes,
        project_ids=project_ids,
        user_ids=user_ids,
        api_key_ids=api_key_ids,
        models=models,
        group_by=group_by,
        limit=int(limit) if limit else None,
        page=page,
    )


@organization_router.get("/organization/usage/moderations")
def usage_moderations(
    start_time: str,
    end_time: str,
    bucket_width: str,
    project_ids: list[str],
    user_ids: list[str],
    api_key_ids: list[str],
    models: list[str],
    group_by: list[str],
    limit: str,
    page: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Get moderations usage details for the organization."""
    return service.usage_moderations(
        start_time=int(start_time) if start_time else None,
        end_time=int(end_time) if end_time else None,
        bucket_width=bucket_width,
        project_ids=project_ids,
        user_ids=user_ids,
        api_key_ids=api_key_ids,
        models=models,
        group_by=group_by,
        limit=int(limit) if limit else None,
        page=page,
    )


@organization_router.get("/organization/usage/vector_stores")
def usage_vector_stores(
    start_time: str,
    end_time: str,
    bucket_width: str,
    project_ids: list[str],
    user_ids: list[str],
    api_key_ids: list[str],
    models: list[str],
    group_by: list[str],
    limit: str,
    page: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Get vector stores usage details for the organization."""
    return service.usage_vector_stores(
        start_time=int(start_time) if start_time else None,
        end_time=int(end_time) if end_time else None,
        bucket_width=bucket_width,
        project_ids=project_ids,
        group_by=group_by,
        limit=int(limit) if limit else None,
        page=page,
    )


@organization_router.get("/organization/users")
def list_organization_users(
    limit: str,
    after: str,
    emails: list[str],
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Lists all of the users in the organization."""
    return service.list_users(
        limit=int(limit) if limit else None, after=after, emails=emails
    )


@organization_router.get("/organization/users/{user_id}")
def retrieve_organization_user(
    user_id: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Retrieves a user by their identifier."""
    return service.retrieve_user(user_id=user_id)


@organization_router.post("/organization/users/{user_id}")
def modify_organization_user(
    user_id: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Modifies a user's role in the organization."""
    return service.modify_user(user_id=user_id)


@organization_router.delete("/organization/users/{user_id}")
def delete_organization_user(
    user_id: str,
    request: Request,
    service: OrganizationService = Depends(OrganizationService),  # noqa: B008
) -> None:
    """Deletes a user from the organization."""
    return service.delete_user(user_id=user_id)
