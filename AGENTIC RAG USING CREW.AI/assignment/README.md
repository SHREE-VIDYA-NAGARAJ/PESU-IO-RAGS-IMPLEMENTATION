# Government Services Chatbot for Senior Citizens

This project is an AI-powered chatbot designed to provide senior citizens in India with accurate and up-to-date information about government services. The chatbot utilizes CrewAI agents to conduct web research and analyze relevant information to assist elderly users in finding services suited to their needs.

## Features

- **Automated Research**: Gathers the latest information from official government sources.
- **Information Analysis**: Extracts and summarizes relevant details about available services.
- **User-Friendly Output**: Generates reports in a structured markdown format for easy readability.

## Project Structure

```
project_root/
│-- assignment/
│   │-- crew.py         # Defines the CrewAI workflow and agents
│   │-- agents.yaml     # Configuration for different agents
│   │-- tasks.yaml      # Configuration for task definitions
│-- main.py             # Main entry point to run the chatbot
│-- README.md           # Project documentation
```

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Pip

### Setup

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <project-folder>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set the required API key for the search tool in your environment:
   ```sh
   export SERPER_API_KEY='your_api_key_here'
   ```

## Usage

### Running the chatbot

To run the chatbot and process user queries:

```sh
python main.py run
```

### Training the chatbot

To train the chatbot with specific inputs:

```sh
python main.py train <iterations> <output_filename>
```

Example:

```sh
python main.py train 10 training_output.log
```

### Replaying a previous execution

To replay the chatbot's execution from a specific task:

```sh
python main.py replay <task_id>
```

### Testing the chatbot

To test the chatbot's functionality:

```sh
python main.py test <iterations> <openai_model_name>
```

Example:

```sh
python main.py test 5 'gpt-4'
```

## Configuration

The behavior of agents and tasks is configured through `agents.yaml` and `tasks.yaml`. You can modify these files to customize the chatbot’s workflow.

### Agents

- **Search Agent**: Responsible for researching government services.
- **Analysis Agent**: Processes and synthesizes the collected information.

### Tasks

- **Information Gathering Task**: Collects government service details for senior citizens.
- **Information Analysis Task**: Structures and refines collected data into a comprehensive report.

## Output

The chatbot generates:

- A **list of relevant government services** with eligibility details.
- A **comprehensive markdown report** (`government_services_report.md`).

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance the chatbot's functionality 
