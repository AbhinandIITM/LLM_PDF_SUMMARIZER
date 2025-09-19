# LLM PDF Summarizer

This project provides a powerful tool for summarizing PDF documents using Large Language Models (LLMs) and Retrieval Augmented Generation (RAG). It allows users to ingest PDF files, process their content, and then interactively query or summarize them using an intelligent chat interface. The system leverages a vector database (ChromaDB) to efficiently store and retrieve document chunks, ensuring context-aware and accurate responses from the LLM.

## Features

*   **PDF Document Ingestion**: Easily add and process multiple PDF files.
*   **LLM-Powered Summarization**: Generate concise and informative summaries of PDF content.
*   **Retrieval Augmented Generation (RAG)**: Enhance LLM responses with relevant information retrieved directly from your documents, reducing hallucinations and improving accuracy.
*   **Vector Database Integration**: Utilizes ChromaDB for efficient storage and semantic search of document embeddings.
*   **Interactive Chat Interface**: Engage in a conversational manner with your documents to extract specific information or generate summaries.

## Installation

Follow these steps to set up the project locally:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/AbhinandIITM/LLM_PDF_SUMMARIZER.git
    cd LLM_PDF_SUMMARIZER
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies**:
    Install the necessary Python packages. You might need to install an LLM provider like `ollama` or `openai` depending on your chosen LLM.
    ```bash
    pip install langchain chromadb pypdf ollama # or openai, depending on your LLM setup
    ```
    *Note: If you are using a specific LLM provider (e.g., OpenAI, Hugging Face), ensure you have the corresponding library installed and your API key configured as an environment variable (e.g., `OPENAI_API_KEY`).*

## Usage

To use the LLM PDF Summarizer:

1.  **Place your PDF documents**:
    Put the PDF files you want to summarize into the `documents/` directory.

2.  **Run the chat/summarization script**:
    Execute the main script to start interacting with your documents.
    ```bash
    python chat.py
    ```
    *Follow the on-screen prompts to load documents, build the knowledge base, and start chatting.*

## Project Structure

```
.
├── chat.ipynb              # Jupyter Notebook for interactive development/testing
├── chat.py                 # Main script for interactive chat with PDFs
├── llm_assist.py           # Core logic for LLM interaction, RAG, and document processing
├── documents/              # Directory to store your PDF files
│   ├── 2101.01158v1.pdf
│   ├── Acoustic_SLAM.pdf
│   └── Team 16 - ROB 530.pdf
├── chroma_db/              # Directory for ChromaDB vector store
│   └── ...                 # ChromaDB internal files
├── LICENSE                 # Project license file
└── README.md               # Project README file
```

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.
