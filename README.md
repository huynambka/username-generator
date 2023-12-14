# Username Generator

## Overview

The Username Generator is a Python script that allows users to generate unique Latin usernames based on their first and last names. The script follows specific rules to create various username combinations, providing flexibility and customization.

## Usage

To use the username generator, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/huynambka/username-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd username-generator
    ```

3. Run the script with the command:

    ```bash
    python username-gen.py [first_name] [last_name]
    ```

    Or

    ```bash
    python username-gen.py -f [names_file]
    ```

## Rules

The script follows the following rules to generate usernames:

- `{fn}`: Represents the full first name.
- `{ln}`: Represents the full last name.
- `{fi}`: Represents the first name's initial.
= `{li}`: Represents the last name's initial.

Feel free to customize the script or add new rules according to your preferences.

## Example

```bash
python username-gen.py John Doe
