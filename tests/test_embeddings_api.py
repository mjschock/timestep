import pytest

EMBEDDING_MODEL = (
    "sentence-transformers/paraphrase-MiniLM-L3-v2"  # Use smaller sentence transformer
)


@pytest.mark.asyncio
async def test_create_embedding(async_client):
    response = await async_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input="This is a test sentence for embedding.",
    )

    assert hasattr(response, "data")
    assert len(response.data) == 1
    embedding = response.data[0].embedding
    assert isinstance(embedding, list)
    assert len(embedding) > 0
    assert all(isinstance(x, int | float) for x in embedding)


@pytest.mark.asyncio
async def test_batch_embeddings(async_client):
    texts = [
        "First test sentence.",
        "Second test sentence.",
        "Third test sentence.",
    ]

    response = await async_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
    )

    assert hasattr(response, "data")
    assert len(response.data) == len(texts)
    for i, embedding_obj in enumerate(response.data):
        assert embedding_obj.index == i
        assert isinstance(embedding_obj.embedding, list)
