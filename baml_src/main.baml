 generator default {
    language "python"
    project_root "../"
    test_command "pyenv activate gloo && poetry run python -m pytest"
    install_command "pyenv activate gloo && poetry add baml@latest"
    package_version_command "pyenv activate gloo && poetry show baml"
}