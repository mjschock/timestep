import pytest


@pytest.mark.asyncio
async def test_moderation_single_input(async_client):
    """Test moderation with a single text input"""
    response = await async_client.moderations.create(
        input="This is a test message for moderation."
    )

    # Verify response structure
    assert hasattr(response, "id")
    assert hasattr(response, "model")
    assert hasattr(response, "results")

    # Verify results
    assert len(response.results) == 1
    result = response.results[0]
    assert hasattr(result, "flagged")
    assert hasattr(result, "categories")
    assert hasattr(result, "category_scores")

    # Verify categories structure - handle both present and None categories
    expected_categories = [
        "harassment",
        "harassment_threatening",
        "hate",
        "hate_threatening",
        "self_harm",
        "self_harm_instructions",
        "self_harm_intent",
        "sexual",
        "sexual_minors",
        "violence",
        "violence_graphic",
        "illicit",
        "illicit_violent",
    ]

    # Check that all expected categories exist as attributes (even if None)
    for category in expected_categories:
        assert hasattr(result.categories, category)
        assert hasattr(result.category_scores, category)

        # If the category has a value, it should be a number
        if getattr(result.categories, category) is not None:
            assert isinstance(getattr(result.categories, category), int | float)
        if getattr(result.category_scores, category) is not None:
            assert isinstance(getattr(result.category_scores, category), int | float)


@pytest.mark.asyncio
async def test_moderation_batch_input(async_client):
    """Test moderation with multiple text inputs"""
    inputs = ["First test message.", "Second test message.", "Third test message."]
    response = await async_client.moderations.create(input=inputs)

    # Verify response structure
    assert hasattr(response, "id")
    assert hasattr(response, "model")
    assert hasattr(response, "results")

    # Verify results
    assert len(response.results) == len(inputs)

    # Verify each result has the expected structure
    for result in response.results:
        assert hasattr(result, "flagged")
        assert hasattr(result, "categories")
        assert hasattr(result, "category_scores")

        # Verify categories structure
        expected_categories = [
            "harassment",
            "harassment_threatening",
            "hate",
            "hate_threatening",
            "self_harm",
            "self_harm_instructions",
            "self_harm_intent",
            "sexual",
            "sexual_minors",
            "violence",
            "violence_graphic",
            "illicit",
            "illicit_violent",
        ]
        for category in expected_categories:
            assert hasattr(result.categories, category)
            assert hasattr(result.category_scores, category)


@pytest.mark.asyncio
async def test_moderation_harmful_content(async_client):
    """Test moderation with potentially harmful content"""
    harmful_text = "I hate everyone and want to kill them all"
    response = await async_client.moderations.create(input=harmful_text)

    result = response.results[0]

    # Should be flagged as harmful
    assert result.flagged is True

    # Should have high scores for relevant categories (if they exist)
    if result.categories.hate is not None:
        assert result.categories.hate > 0.5
    if result.categories.hate_threatening is not None:
        assert result.categories.hate_threatening > 0.5
    if result.categories.violence is not None:
        assert result.categories.violence > 0.5


@pytest.mark.asyncio
async def test_moderation_safe_content(async_client):
    """Test moderation with safe content"""
    safe_text = "Hello, how are you today? The weather is nice."
    response = await async_client.moderations.create(input=safe_text)

    result = response.results[0]

    # Should not be flagged as harmful
    assert result.flagged is False

    # Should have low scores for all categories that have values
    expected_categories = [
        "harassment",
        "harassment_threatening",
        "hate",
        "hate_threatening",
        "self_harm",
        "self_harm_instructions",
        "self_harm_intent",
        "sexual",
        "sexual_minors",
        "violence",
        "violence_graphic",
        "illicit",
        "illicit_violent",
    ]

    for category in expected_categories:
        category_value = getattr(result.categories, category)
        if category_value is not None:
            assert category_value < 0.5


@pytest.mark.asyncio
async def test_moderation_missing_input(async_client):
    """Test moderation with missing input field"""
    with pytest.raises(
        Exception
    ) as exc_info:  # TODO: Replace with specific exception if possible
        await async_client.moderations.create()

    # Should return a 400 error for missing input
    assert "400" in str(exc_info.value) or "input" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_moderation_empty_input(async_client):
    """Test moderation with empty input"""
    with pytest.raises(
        Exception
    ) as exc_info:  # TODO: Replace with specific exception if possible
        await async_client.moderations.create(input="")

    # Should return a 400 error for empty input
    assert "400" in str(exc_info.value) or "input" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_moderation_invalid_input_type(async_client):
    """Test moderation with invalid input type"""
    with pytest.raises(Exception) as exc_info:
        await async_client.moderations.create(input=123)

    # Should return a 400 error for invalid input type
    assert "400" in str(exc_info.value) or "string" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_moderation_mixed_batch_with_harmful(async_client):
    """Test batch moderation with mix of safe and harmful content"""
    inputs = [
        "Hello, how are you?",  # Safe
        "I hate everyone",  # Harmful
        "The weather is nice",  # Safe
        "Kill yourself",  # Harmful
    ]

    response = await async_client.moderations.create(input=inputs)

    assert len(response.results) == 4

    # Check specific results
    assert response.results[0].flagged is False  # Safe
    assert response.results[1].flagged is True  # Harmful
    assert response.results[2].flagged is False  # Safe
    assert response.results[3].flagged is True  # Harmful

    # Verify harmful content has appropriate category scores (if they exist)
    if response.results[1].categories.hate is not None:
        assert response.results[1].categories.hate > 0.5
    if response.results[3].categories.self_harm is not None:
        assert response.results[3].categories.self_harm > 0.5
