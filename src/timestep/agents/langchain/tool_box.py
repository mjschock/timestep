from __future__ import annotations

from langchain.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.agent_toolkits.file_management import FileManagementToolkit
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_community.tools.wikidata.tool import WikidataAPIWrapper, WikidataQueryRun
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_community.tools.youtube.search import YouTubeSearchTool
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.language_models import BaseChatModel
from langchain_core.tools import BaseTool

# @contextmanager
# def pushd(new_dir):
#     """Context manager for changing the current working directory."""
#     prev_dir = os.getcwd()
#     os.chdir(new_dir)
#     try:
#         yield
#     finally:
#         os.chdir(prev_dir)


# @tool
# def process_csv_tool(
#     workspace_path: str,
#     csv_file_path: str,
#     instructions: str,
#     output_path: Optional[str] = None,
# ) -> str:
#     """Process a CSV by with pandas in a limited REPL.\
#  Only use this after writing data to disk as a csv file.\
#  Any figures must be saved to disk to be viewed by the human.\
#  Instructions should be written in natural language, not code. Assume the dataframe is already loaded."""
#     with pushd(workspace_path):
#         try:
#             df = pd.read_csv(csv_file_path)
#         except Exception as e:
#             return f"Error: {e}"
#         agent = create_pandas_dataframe_agent(llm, df, max_iterations=30, verbose=True)
#         if output_path is not None:
#             instructions += f" Save output to disk at {output_path}"
#         try:
#             result = agent.run(instructions)
#             return result
#         except Exception as e:
#             return f"Error: {e}"


# async def async_load_playwright(url: str) -> str:
#     """Load the specified URLs using Playwright and parse using BeautifulSoup."""
#     from bs4 import BeautifulSoup
#     from playwright.async_api import async_playwright

#     results = ""
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         try:
#             page = await browser.new_page()
#             await page.goto(url)

#             page_source = await page.content()
#             soup = BeautifulSoup(page_source, "html.parser")

#             for script in soup(["script", "style"]):
#                 script.extract()

#             text = soup.get_text()
#             lines = (line.strip() for line in text.splitlines())
#             chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
#             results = "\n".join(chunk for chunk in chunks if chunk)
#         except Exception as e:
#             results = f"Error: {e}"
#         await browser.close()
#     return results


# def run_async(coro):
#     event_loop = asyncio.get_event_loop()
#     return event_loop.run_until_complete(coro)


# @tool
# def browse_web_page(url: str) -> str:
#     """Verbose way to scrape a whole webpage. Likely to cause issues parsing."""
#     return run_async(async_load_playwright(url))


# def _get_text_splitter():
#     return RecursiveCharacterTextSplitter(
#         # Set a really small chunk size, just to show.
#         chunk_size=500,
#         chunk_overlap=20,
#         length_function=len,
#     )


# class WebpageQATool(BaseTool):
#     name = "query_webpage"
#     description = (
#         "Browse a webpage and retrieve the information relevant to the question."
#     )
#     text_splitter: RecursiveCharacterTextSplitter = Field(
#         default_factory=_get_text_splitter
#     )
#     qa_chain: BaseCombineDocumentsChain

#     def _run(self, url: str, question: str) -> str:
#         """Useful for browsing websites and scraping the text information."""
#         result = browse_web_page.run(url)
#         docs = [Document(page_content=result, metadata={"source": url})]
#         web_docs = self.text_splitter.split_documents(docs)
#         results = []
#         # TODO: Handle this with a MapReduceChain
#         for i in range(0, len(web_docs), 4):
#             input_docs = web_docs[i : i + 4]
#             window_result = self.qa_chain(
#                 {"input_documents": input_docs, "question": question},
#                 return_only_outputs=True,
#             )
#             results.append(f"Response from window {i} - {window_result}")
#         results_docs = [
#             Document(page_content="\n".join(results), metadata={"source": url})
#         ]
#         return self.qa_chain(
#             {"input_documents": results_docs, "question": question},
#             return_only_outputs=True,
#         )

#     async def _arun(self, url: str, question: str) -> str:
#         raise NotImplementedError


# def get_tools(llm, workspace_path):
def get_tools(llm: BaseChatModel, workspace_path: str) -> list[BaseTool]:  # noqa: ARG001
    file_management_toolkit = FileManagementToolkit(
        root_dir=workspace_path,
        # selected_tools=["read_file", "write_file"],
    )

    # async_browser = create_async_playwright_browser(headless=False)
    # play_wright_browser_toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)

    tools = [
        # ArxivAPIWrapper(),
        # DuckDuckGoSearchResults(api_wrapper=DuckDuckGoSearchAPIWrapper(region="us-en")),
        DuckDuckGoSearchRun(),
        PubmedQueryRun(),
        # PythonREPL(),
        # process_csv_tool.partial(workspace_path=workspace_path),
        # partial(process_csv_tool, workspace_path=workspace_path),
        # ReadFileTool(),
        # ShellTool(),
        YahooFinanceNewsTool(),
        YouTubeSearchTool(),
        # WebpageQATool(qa_chain=load_qa_with_sources_chain(llm)),
        WikidataQueryRun(api_wrapper=WikidataAPIWrapper()),
        WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()),
        # WriteFileTool(),
    ]

    tools += file_management_toolkit.get_tools()
    # tools += play_wright_browser_toolkit.get_tools()
    # tools += [browse_web_page]

    # + load_tools(["requests_all"])

    return tools
