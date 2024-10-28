


# Retrieval-Augmented Generation (RAG) System

## Website Selection Rationale

Reddit hosts a wide variety of discussions across thousands of "subreddits" (community forums focused on specific interests). This diversity makes it valuable for studying a broad range of topics, from niche hobbies to global news.

## Implementation Details

Sure! Here are the detailed implementation specifics for your Retrieval-Augmented Generation (RAG) system using the provided code:

### 1. Environment Setup

- **Prerequisites**: Ensure you have Python and pip installed. You'll also need to set up a virtual environment if desired.

- **Install Required Libraries**: Use pip to install the necessary libraries. Run the following command:
  ```bash
  pip install llama-index qdrant-client python-dotenv
  ```

- **Environment Variables**: Create a `.env` file in your project directory to securely store your API keys:
  ```plaintext
  JINA_API_KEY=your_jina_api_key
  GROQ_API_KEY=your_groq_api_key
  ```

### 2. Code Breakdown

- **Importing Modules**:  
  The script imports modules necessary for vector storage, embeddings, and LLM interaction from `llama_index`, as well as the `QdrantClient` from `qdrant_client` for managing the vector store.

- **Loading Environment Variables**:  
  The script utilizes the `dotenv` library to load API keys from the `.env` file:
  ```python
  load_dotenv()
  ```

### 3. Model Configuration

- **Embedding Model Setup**:  
  The embedding model is configured to use Jina’s embedding focused on passage retrieval:
  ```python
  Settings.embed_model = JinaEmbedding(
      api_key=os.getenv("JINA_API_KEY"),
      model="jina-embeddings-v3",
      task="retrieval.passage",
  )
  ```

- **LLM Configuration**:  
  The language model (LLM) is set to Groq:
  ```python
  Settings.llm = Groq(
      api_key=os.getenv("GROQ_API_KEY"),
      model="gemma-7b-it",
      temperature=0.7
  )
  ```

### 4. Creating the RAG System

- **Function: `create_rag_system(data_dir="./data")`**:
  - **Initialize Qdrant Client**: This connects to Qdrant, using a local path to store data.
  - **Create Qdrant Vector Store**: This sets up a vector store for document embeddings.
  - **Load Documents**: The function uses `SimpleDirectoryReader` to read documents from the specified directory.
  - **Create Vector Store Index**: It builds an index from the loaded documents for efficient querying.
  - **Query Engine**: The function returns a query engine that allows interaction with the index.

### 5. Querying the RAG System

- **Function: `query_rag(query_engine, question: str)`**:
  - Accepts a user query and retrieves a response by querying the system.
  - Returns the response to be displayed to the user.

### 6. Main Loop

- **Function: `main()`**:
  - Initializes the RAG system by calling `create_rag_system()`.
  - Enters a loop, prompting the user for questions until 'quit' is entered.
  - Uses the `query_rag()` function to process each question and print the corresponding answer.

### 7. Execution of the Script

- The script is executed when run as the main program:
  ```python
  if __name__ == "__main__":
      main()
  ```

## Usage Instructions

1. **Prepare Documents**: Place relevant documents (e.g., PDFs or text files) in the `./data` directory. These documents should contain information related to the queries you expect users to ask.

2. **Run the Script**:  
   Execute the script using Python:
   ```bash
   python your_script_name.py
   ```

3. **Interact with the System**:  
   Once the script is running, you can enter questions related to the content of the documents. Type your question and press Enter. To exit, type `quit`.

### Additional Considerations

- **Document Format**: Ensure that the documents are in a format that `SimpleDirectoryReader` can process effectively.
- **API Key Security**: Keep your API keys secure and do not hard-code them into your script. Use the `.env` file as shown.
- **Debugging**: If you encounter issues, consider adding logging to track the flow of data and identify any potential errors during document loading or querying.

## Examples of Queries and Responses

- **Enter your question (or 'quit' to exit)**: *What is Reddit?*  
  **Answer**: Reddit is a social news aggregation, web content rating, and discussion website. It is registered as a domain community, where registered members submit content such as text posts or direct links. Other members then vote the submitted content up or down to organize the posts and determine their position on the site's pages. The submissions with the most positive votes appear on the front page or the top of a category. Content entries are organized by areas of interest called "subreddits".

- **Enter your question (or 'quit' to exit)**: *Give me some recent updates on Reddit.*  
  **Answer**: Sure, here are some recent updates that have been trending on Reddit:
  1. In the sports subreddit, there's a post about Nathan Shepherd attempting to injure Justin Herbert and getting decked by a Charger.
  2. The r/nba subreddit is buzzing about Dwayne Wade's statue unveiling.
  3. Carlos Sainz has won the 2024 Mexico City Grand Prix, as reported in the r/formula1 subreddit.
  4. In the r/leagueoflegends subreddit, there's a post-match discussion about T1 vs. Gen.G in the 2024 World Championship.
  5. The r/movies subreddit has some exciting news about the '28 Years Later' trilogy, with the first two movies reportedly already shot.
  6. Lastly, in the r/nfl subreddit, there's a highlight of Jayden Daniels throwing a last-second Hail Mary that Noah Brown caught to win the game.

- **Enter your question (or 'quit' to exit)**: *Who is Nathan?*  
  **Answer**: Nathan appears to be a football player, as indicated by the image and text associated with the first image link. The text specifically mentions an incident where Nathan Shepard tries to injure Justin Herbert and gets decked by a Charger. However, the context does not provide any further information about Nathan's full name, team, or position.

- **Enter your question (or 'quit' to exit)**: *How many users does Reddit have?*  
  **Answer**: I cannot provide the current number of Reddit users directly from the given context. However, the context does show that Reddit is a popular platform with a variety of active communities, such as r/sports, r/nba, r/formula1, r/leagueoflegends, r/movies, and r/nfl. You can check Reddit's official website or press releases for the most up-to-date user statistics.

## Challenges and Solutions

### The General Challenges that Came Up:

- **Handling Miscellaneous Errors**: 
- **Processing Time**
- **Renewing API Keys**
```




