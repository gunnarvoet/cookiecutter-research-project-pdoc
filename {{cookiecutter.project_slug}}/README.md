{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}

## Features

-   TODO

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[gunnarvoet/cookiecutter-research-project-pdoc](https://github.com/gunnarvoet/cookiecutter-research-project-pdoc)
project template.
