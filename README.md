# Python Widget for Bank Operations

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

Python Widget for Bank Operations is a project that provides a set of tools and functions for working with bank operations. It allows you to display and mask card and account numbers, as well as retrieve information about recent operations.
## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/exetch/bank-operations-python-widget.git
   ```
2. Install the dependencies:

    ```
   pip install -r requirements.txt
    ```
## Usage
1. Prepare the bank operation data in the expected format for the project.
   ```
   # Example of expected data
   [
    {"id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },...]
   ```
2. Replace the operations.json file with your own file containing the operations data.
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

