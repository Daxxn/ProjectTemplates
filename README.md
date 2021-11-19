# Project Template Creator

> Tool for creating a template project of any language and have everything installed and ready to go.

## Usage

> Args: tc [language] [type] [sub-type]

Enter the project details:

* Name
* Path
* License

then the configureator will generate the project.

### ..config.json file:

The config file is placed at the root of the template project (with the package.json file or similar) and is where the install scripts, required dependencies, and the package manager command is defined.

#### Schema:

```json
{
    "scripts": [],
    "pm": "",
    "dependencies": []
}
```

```json
{
    "pm": "npm",
    "install": "install",
    "depCheck": "version",
    "dependencies": [
        "package-a",
        "package-b"
    ]
}
```

### Installation

I'm not sure how to install the package globally yet. for now its using the python interpreter and setting a bash alias to trigger it.

In the future there will be an install script that will activate the script through the `tc` command.