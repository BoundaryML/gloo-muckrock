 generator default {
    language "python"
    project_root "../"
    test_command "poetry run python -m pytest"
    install_command "poetry add baml@latest"
    package_version_command "poetry show baml"
}