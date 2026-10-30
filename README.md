
# AutomationExercise UI Automation Testing

## About the Project

This project is an automated UI testing suite for the [AutomationExercise](https://www.automationexercise.com/) website.

It is built with Python, Selenium WebDriver, Pytest, and Allure. The project demonstrates practical UI automation skills, test organization, Page Object Model implementation, test data management, and containerized test execution.

The test suite covers key user workflows, including authentication, account management, product browsing, shopping cart operations, and checkout.

## Test Coverage

The project includes **31 automated tests** covering 10 functional areas:

- **Login**
- **Logout**
- **Signup**
- **Account Management**
- **Products**
- **Shopping Cart**
- **Search and Filter**
- **Checkout and Orders**
- **Contact Us**
- **Subscription**

The complete list of automated tests is available in [tests.md](docs/tests.md).

## Technologies

- **Python** — programming language
- **Selenium WebDriver** — browser automation
- **Pytest** — test framework and test execution
- **Allure Report** — test reporting and results visualization
- **Page Object Model (POM)** — design pattern for organizing page objects, locators, and interactions
- **Faker** — dynamic test data generation
- **Docker** — containerized test execution
- **Docker Compose** — container orchestration for test execution
- **GitHub Actions** — CI workflow automation

## Getting Started

### Prerequisites

For local execution, make sure the following tools are installed:

- Python compatible with the project dependencies
- Google Chrome
- Git
- Allure Commandline (for generating and viewing Allure reports)

For Docker execution:

- Docker Desktop (Windows/macOS) or Docker Engine (Linux)
- Docker Compose

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PavloIvanochok/Automation_Exercise_UI_tests.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Automation_Exercise_UI_tests
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment.

   **Windows (PowerShell):**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   **macOS / Linux:**

   ```bash
   source .venv/bin/activate
   ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running Tests Locally

Run the complete test suite:

```bash
pytest -v
```

Run the tests and generate Allure results:

```bash
pytest -v --alluredir=allure-results
```

The test results will be saved in the `allure-results` directory.

## Running Tests with Docker

Build the Docker image and run the complete test suite:

```bash
docker compose up --build --exit-code-from regression
```

Run the tests again without rebuilding the image:

```bash
docker compose up --exit-code-from regression
```

The Allure results are saved in the local `allure-results` directory through the Docker volume configuration.

If your tests require registered user credentials, provide the `EMAIL` and `PASSWORD` environment variables before running Docker Compose.
## Allure Reports

Allure provides a detailed overview of test execution, including:

- Test names and descriptions
- Test execution status
- Test steps
- Failure details

To generate the report locally, make sure Allure Commandline is installed and available in your system's `PATH`.

Generate the report:

```bash
allure generate allure-results --clean -o allure-report
```

Open the generated report:

```bash
allure open allure-report
```

Alternatively, use:

```bash
allure serve allure-results
```

This command generates a temporary report and opens it in your default browser.

## Project Goals

This project was created to practice and demonstrate Junior QA Automation skills, including:

- UI test automation with Python and Selenium WebDriver
- Test organization and execution with Pytest
- Page Object Model implementation
- Positive and negative test scenarios
- Dynamic test data generation with Faker
- Test reporting with Allure
- Browser automation and end-to-end user workflows
- Containerized test execution with Docker
- CI workflow automation with GitHub Actions

## Application Under Test

[AutomationExercise](https://www.automationexercise.com/)
