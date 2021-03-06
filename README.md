<!-- Automatic builds status -->
<!-- [![Build Status](https://travis-ci.org/XX)](https://travis-ci.org/XX) -->

<!-- Codacy -->
[![Codacy grade](https://api.codacy.com/project/badge/Grade/c04cb69ce4104ea9839f2edb901ddefa)](https://www.codacy.com/app/cristianrcv/awesome-recipes?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cristianrcv/awesome-recipes&amp;utm_campaign=Badge_Grade)

<!-- [![Codacy coverage](https://api.codacy.com/project/badge/Coverage/XX)](https://www.codacy.com/app/XX) -->

<!-- Codecov -->
<!-- [![codecov](https://codecov.io/gh/XX)](https://codecov.io/gh/XX) -->

<!-- Maven central packages version -->
<!-- [![Maven Central](https://maven-badges.herokuapp.com/maven-central/XX)](https://maven-badges.herokuapp.com/maven-central/XX) -->

<!-- Dependencies update status -->
<!-- [![Dependency Status](https://www.versioneye.com/user/XX)](https://www.versioneye.com/user/XX) -->

<!-- Java DOC status -->
<!-- [![Javadocs](http://javadoc.io/badge/XX.svg)](http://javadoc.io/doc/XX) -->

<!-- Main Repository language -->
[![Language](https://img.shields.io/badge/language-python-brightgreen.svg)](https://img.shields.io/badge/language-python-brightgreen.svg)

<!-- Repository License -->
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/cristianrcv/pycompss-pluto/blob/master/LICENSE)


# Awesome Recipes

Awesome Recipes is a website to store food recipes and perform queries on them.

It is a personal project and it is still under development.


## Table of Contents

* [Dependencies](#dependencies)
    * [Software Dependencies](#software-dependencies)
    * [Python Module Dependencies](#python-module-dependencies)
* [Useful Commands](#useful-commands)
* [Style](#style)
* [Contributing](#contributing)
* [Author](#author)
* [License](#license)

---


## Dependencies

### Software Dependencies

[Django][django]: Django

### Python Module Dependencies

- [Django][django] Python module (1.11.15)
- [django-crispy-forms][django-crispy-forms] Python module (1.7.2)
- [django-filter][django-filter] Python module (1.1.0)
- [django-widget-tweaks][django-widget-tweaks] Python module (1.4.3)


## Useful Commands

### Run

```bash
python manage.py runserver
```

### Database

```bash
python manage.py flush
python manage.py makemigrations recipes
python manage.py migrate
python manage.py loaddata recipes/fixtures/base.json
```

### Super user creation

```bash
python manage.py createsuperuser
```

### Complete command

```bash
rm -f db.sqlite3 && python manage.py flush && python manage.py makemigrations recipes && python manage.py migrate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', '', '1234')" | python manage.py shell && python manage.py loaddata recipes/fixtures/base.json && python manage.py runserver
```


## Style

This project follows the [PyCodeStyle guide][pycodestyle] (formerly called pep8).

This project tolerates the following relaxations:
* `E501 line too long` : Code lines can be up to 120 characters

You can verify the code style by running:

```bash
pycodestyle . --max-line-length=120
```


## Contributing

All kinds of contributions are welcome. Please do not hesitate to open a new issue,
submit a pull request or contact the author if necessary. 
 

## Author

Cristián Ramón-Cortés Vilarrodona <cristian.ramoncortes(at)bsc.es> ([Personal Website][cristian])


## License

Licensed under the [Apache 2.0 License][apache-2]


[django]: https://www.djangoproject.com/
[django-crispy-forms]: https://django-crispy-forms.readthedocs.io/en/latest/
[django-filter]: https://django-filter.readthedocs.io/en/master/
[django-widget-tweaks]: https://pypi.org/project/django-widget-tweaks/

[pycodestyle]: https://pypi.python.org/pypi/pycodestyle

[cristian]: https://cristianrcv.netlify.com/

[apache-2]: http://www.apache.org/licenses/LICENSE-2.0
