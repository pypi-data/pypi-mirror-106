## gitmodules

[![Version](https://img.shields.io/badge/version-2021.5-13-blue)](https://github.com/maite828/gitmodules.git)
[![Version](https://img.shields.io/badge/module_A-2.7.0-yellow)](https://github.com/maite828/module_A.git)
[![Version](https://img.shields.io/badge/module_B-1.6.0-yellow)](https://github.com/maite828/module_B.git)

# CONTAINER MODULE

#### gitmodules_mercurio[module_A==2.7.0,module_B==1.6.0]==2021.5-13.post12
#### gitmodules_mercurio[module_A==2.6.0,module_B==1.5.0]==2021.5-13.post10

#### Instalación de new módulo:
```git submodule add -b main ssh://git@github.com:maite828/module_A.git module_A```                                         
#### Actualización de módulos:
```git submodule update --init && git submodule update --remote --recursive```
####

- [INSTALAR PADRE CON VERSION]
  - ```pip install  gitmodules_mercurio==2021.5-13.post12```

- [INSTALAR PADRE SIN VERSION]
  - ```pip install gitmodules_mercurio```

- [INSTALAR HIJOS]
  - ```pip install gitmodules_mercurio[module_A]```
  - ```pip install gitmodules_mercurio[module_A,module_B]```
  - ```pip install gitmodules_mercurio[all]```

- [INSTALAR UN MODULO DE UNA VERSION PADRE ANTERIOR] (#en este ejemplo, la última version es 2021.5-13.post12)
  - ```pip install gitmodules_mercurio[module_A]==2021.5-13.post10```

- [INSTALAR DOS MODULOS DE UNA VERSION PADRE ANTERIOR] (#en este ejemplo, la última version es 2021.5-13.post12)
  - ```pip install gitmodules_mercurio[module_A,module_B]==2021.5-13.post10```

- [INSTALAR PADRE Y TODOS SUBMODULOS DE UNA VERSION ANTERIOR] (#en este ejemplo, la última version es 2021.5-13.post12)
  - ```pip install gitmodules_mercurio[all]==2021.5-13.post10```

- [INSTALAR MODULOS SUELTOS] (#con version, sustituye version actual)
  - ```pip install module_A==2.7.0```
  - ```pip install module_B==1.5.0```

- [BORRAR]
  - ```ll .venv/lib/python3.6/site-packages/```
  - ```rm -rf .venv/lib/python3.7/site-packages/git*```
  - ```rm -rf .venv/lib/python3.7/site-packages/module*```
