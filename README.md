[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<p align="center">
  <h3 align="center">GPU Price Extractor Argentina</h3>

  <p align="center">
    Extractor de precios de placas de video (GPU's) desde el sitio web de los principales proveedores de Argentina realizado en Python.
    <br />
    <a href="https://github.com/PecceG2/"><strong>Ver todos mis proyectos »</strong></a>
    <br />
    <br />
    <a href="https://github.com/PecceG2/GPU-Price-Extractor-Proveedores-Argentina/issues">Reportar un Bug</a>
    ·
    <a href="https://github.com/PecceG2/GPU-Price-Extractor-Proveedores-Argentina/blob/master/LICENSE.md">Ver Licencia</a>
    ·
    <a href="https://github.com/PecceG2/GPU-Price-Extractor-Proveedores-Argentina/issues">Solicitar Mejora</a>
  </p>
</p>


**Requisitos previos**
---

1. Descarga e instala [`Python3`](https://www.python.org/downloads/) para tu sistema operativo.

2. Descarga e instala [`Google Chrome`](https://www.google.com/chrome/) para tu sistema operativo.

3. Instalá las dependencias con `pip`:
    + `$ pip install -r requirements.txt`

**Uso**
---

Para obtener un archivo CSV, descargaremos el repositorio, abriremos una terminal `cmd` dentro del directorio, y ejecutaremos:
    + `$ python generate_gpu_list.py`

Luego aguardamos, y una vez finalizado se generará un archivo `placas.csv` con toda la información dentro del mismo directorio.


**Proveedores actualmente soportados:**
VENEX
CompraGamer

**Proveedores a agregar en un futuro:**
~~VENEX~~
~~CompraGamer~~
LOGG Hard Store
FullH4rd
Maximus Gaming Hardware


## To-Do

- [x] Unificar todos los proveedores en el mismo script (y exportar una lista conjunta)
- [ ] Agregar hashrate de cada placa
- [ ] Extraer el modelo exacto de cada placa en una columna independiente
- [ ] Agregar valor de ROI basado en minería de Ethereum
- [ ] Agregar consumo eléctrico estimado de cada placa
- [x] Agregar VENEX
- [x] Agregar CompraGamer
- [ ] Agregar LOGG Hard Store
- [ ] Agregar FullH4rd
- [ ] Agregar Maximus Gaming Store


## License
>You can check out the full license [here](https://github.com/PecceG2/GPU-Price-Extractor-Proveedores-Argentina/blob/master/LICENSE.md)

This project is licensed under the terms of the **MIT** license.


---
Descargo de responsabilidad: Ninguna marca, proveedor, o sitio web incluído aquí pertenece / tiene asociación de ningún tipo con el creador del repositorio. Si por algún motivo este script no funciona o genera cualquier problema en los sitios externos, queda a responsabilidad completa de la persona que utilizó el mismo.


[contributors-shield]: https://img.shields.io/github/contributors/PecceG2/GPU-Price-Extractor-Proveedores-Argentina.svg?style=flat-square
[contributors-url]: https://github.com/PecceG2/GPU-Price-Extractor-Proveedores-Argentina/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PecceG2/GPU-Price-Extractor-Proveedores-Argentina.svg?style=flat-square
[forks-url]: https://github.com/PecceG2/GPU-Price-Extractor-Proveedores-Argentina/network/members
[stars-shield]: https://img.shields.io/github/stars/PecceG2/GPU-Price-Extractor-Proveedores-Argentina.svg?style=flat-square
[stars-url]: https://github.com/PecceG2/GPU-Price-Extractor-Proveedores-Argentina/stargazers
[issues-shield]: https://img.shields.io/github/issues/PecceG2/GPU-Price-Extractor-Proveedores-Argentina.svg?style=flat-square
[issues-url]: https://github.com/PecceG2/GPU-Price-Extractor-Proveedores-Argentina/issues
[license-shield]: https://img.shields.io/github/license/PecceG2/GPU-Price-Extractor-Proveedores-Argentina.svg?style=flat-square
[license-url]: https://github.com/PecceG2/GPU-Price-Extractor-Proveedores-Argentina/blob/master/LICENSE.md

