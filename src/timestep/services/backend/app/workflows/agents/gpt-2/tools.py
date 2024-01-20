# from llama_hub.tools.gmail.base import GmailToolSpec
# from llama_hub.tools.google_calendar import GoogleCalendarToolSpec
# from llama_hub.tools.wikipedia.base import WikipediaToolSpec

# from llama_index import download_loader
import io
import os
from llama_index.tools import FunctionTool
from minio import Minio

# MinioReader = download_loader("MinioReader")

# gmail_tool_spec = GmailToolSpec()
# google_calendar_tool_spec = GoogleCalendarToolSpec()
# wikipedia_tool_spec = WikipediaToolSpec()

# minio_reader = MinioReader(
#     bucket="documents",
#     minio_endpoint="localhost:9000",
#     minio_secure=False,
#     minio_access_key="minio_access_key",
#     minio_secret_key="minio_secret_key",
# )

def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)

def divide(a: int, b: int) -> float:
    """Divide two integers and returns the result float"""
    return a / b

divide_tool = FunctionTool.from_defaults(fn=divide)

def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)

# gmail_tools = gmail_tool_spec.to_tool_list()

# google_calendar_tools = google_calendar_tool_spec.to_tool_list()

# def read_minio_file(
#     bucket: str,
#     minio_endpoint: str,
#     minio_secure: bool,
#     minio_access_key: str,
#     minio_secret_key: str,
#     file_name: str,
# ) -> str:
#     """Reads a file from a Minio bucket and returns the file contents as a string"""
#     minio_reader = MinioReader(
#         bucket=bucket,
#         minio_endpoint=minio_endpoint,
#         minio_secure=minio_secure,
#         minio_access_key=minio_access_key,
#         minio_secret_key=minio_secret_key,
#     )
#     return minio_reader.read_file(file_name)

# minio_reader_tool = FunctionTool.from_defaults(fn=read_minio_file)

def write_to_file(
    # bucket_name: str,
    # minio_endpoint: str,
    # minio_secure: bool,
    # minio_access_key: str,
    # minio_secret_key: str,
    # file_name: str,
    # file_contents: str,
    destination_file: str,
    source_contents: str,
) -> None:
    """Writes a file to a Minio bucket"""
    minio_endpoint = os.getenv("MINIO_ENDPOINT")
    minio_client = Minio(
        minio_endpoint,
        access_key=os.getenv("MINIO_ROOT_USER"),
        secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
        secure=False,
    )

    # The file to upload, change this path if needed
    # source_file = "/tmp/test-file.txt"

    # The destination bucket and filename on the MinIO server
    bucket_name = "default"
    # destination_file = "my-test-file.txt"

    # Make the bucket if it doesn't exist.
    found = minio_client.bucket_exists(bucket_name)

    if not found:
        minio_client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)

    else:
        print("Bucket", bucket_name, "already exists")

    # TODO: use nhost storage to store files

    data = io.BytesIO(source_contents.encode())
    minio_client.put_object(
        bucket_name=bucket_name,
        object_name=destination_file,
        # file_path=source_file,
        # =taio.BytesIO(source_contents.encode()),
        data=data,
        length=len(source_contents),
        content_type="application/octet-stream",
    )

    # print(
    #     source_file, "successfully uploaded as object",
    #     destination_file, "to bucket", bucket_name,
    # )

write_to_file_tool = FunctionTool.from_defaults(fn=write_to_file)

# wikipedia_tools = wikipedia_tool_spec.to_tool_list()
