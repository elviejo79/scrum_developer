Proceso para hacer commit
=========================

Checa tus archivos para el estandard de c'odigo

  $ flake8 --max-line-length=160 ./practicas/*

Guardar tus cambios locales

 $ git commit -am "Resolv'i el problema ##"

Para traerte la versi'on m'as nueva desde el servidor:

  $ git pull

Si todo est'a bien ya tienes los cambios nuevos, y los tuyos...

  $ git commit -am "Merge"

Subir tus cambios al servidor

  $ git push

