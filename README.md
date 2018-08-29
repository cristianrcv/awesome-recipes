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

- [Django][django] Python module
- [django-crispy-forms][django-crispy-forms] Python module
- [django-measurement][django-measurement] Python module
- [measurement][measurement] Python module


## Useful Commands

### Run

```
python manage.py runserver
```

### Database

```
python manage.py flush
python manage.py makemigrations recipe
python manage.py migrate
```

### Super user creation

```
python manage.py createsuperuser
```


## Style

This project follows the [PyCodeStyle guide][pycodestyle] (formerly called pep8).

This project tolerates the following relaxations:
* `E501 line too long` : Code lines can be up to 120 characters

You can verify the code style by running:

```
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
[django-measurement]: https://github.com/coddingtonbear/django-measurement
[measurement]: https://pypi.org/project/measurement/

[pycodestyle]: https://pypi.python.org/pypi/pycodestyle

[cristian]: https://cristianrcv.netlify.com/

[apache-2]: http://www.apache.org/licenses/LICENSE-2.0
