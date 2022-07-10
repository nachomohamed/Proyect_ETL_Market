# Estructura de datos de las tablas

En esta sección se define la estructura de las tablas junto con un diccionario de datos de todos los datasets analizados. Se presenta el nombre de la columna original de las tablas, el nuevo nombre registrado para su normalización, el tipo de dato establecido y una descripción del contenido de cada columna.

## **Tabla:** Cliente
| | Columna Normalizada | Columna Original | Tipo de Dato | Descripción |
|:-------------------:|---|---|---|---|
| 0 | IdCliente | ID | int64 | Clave única que identifica al cliente |
| 1 | Nombre_y_Apellido | Nombre_y_Apellido | object | Nombre y apellido del cliente |
| 2 | Edad | Edad | int64 | Edad del cliente |
| 3 | Telefono | Telefono | object | Teléfono del cliente |
| 4 | Domicilio | Domicilio | object | Domicilio del cliente |
| 5 | Provincia | Provincia | object | Provincia del cliente |
| 6 | Localidad | Localidad | object | Localidad del cliente |
| 7 | Latitud | X | float64 | Latitud del domicilio del cliente |
| 8 | Longitud | Y | float64 | Longitud del domicilio del cliente |

## **Tabla:** Compra
| | Columna Normalizada | Columna Original | Tipo de Dato | Descripción |
|:-------------------:|---|---|---|---|
| 0 | IdCompra | IdCompra | int64 | Clave única que identifica una compra |
| 1 | Fecha | Fecha | datetime64 | Fecha registrada de compra |
| 2 | Fecha_Año | Fecha_Año | int64 | Año registrado de compra |
| 3 | Fecha_Mes | Fecha_Mes | int64 | Mes registrado de compra |
| 4 | Fecha_Periodo | Fecha_Periodo | int64 | Periodo registrado de compra  |
| 5 | IdProducto | IdProducto | int64 | Clave única que identifica al producto adquirido |
| 6 | Cantidad | Cantidad | int64 | Cantidad de producto adquirido en la compra |
| 7 | Precio | Precio | float64 | Precio pagado por la compra |
| 8 | IdProveedor | IdProveedor | int64 | Clave única que identifica al proveedor |

## **Tabla:** Gasto
| | Columna Normalizada | Columna Original | Tipo de Dato | Descripción |
|:-------------------:|---|---|---|---|
| 0 | IdGasto | IdGasto | int64 | Clave única que identifica el gasto |
| 1 | IdSucursal | IdSucursal | int64 | Clave única que identifica la sucursal |
| 2 | IdTipoGasto | IdTipoGasto | int64 | Clave única que identifica el tipo de gasto |
| 3 | Fecha | Fecha | datetime64 | Fecha registrada del gasto |
| 4 | Monto | Monto | float64 | Monto total del gasto |

## **Tabla:** Localidad
| | Columna Normalizada | Columna Original | Tipo de Dato | Descripción |
|:-------------------:|---|---|---|---|
| 0 | IdLocalidad | id | int64 | Clave única que identifica la localidad |
| 1 | Localidad | nombre | object | Nombre de la localidad |
| 2 | IdMunicipio | municipio_id | int64 | Clave única que identifica al municipio |
| 3 | Municipio | municipio_nombre | object | Nombre del municipio |
| 4 | IdDepartamento | departamento_id | int64 | Clave única que identifica al departamento |
| 5 | Departamento | departamento_nombre | object | Nombre del departamento |
| 6 | IdProvincia | provincia_id | int64 | Clave única que identifica la provincia |
| 7 | Provincia | provincia_nombre | object | Nombre de la provincia |
| 8 | Fuente | fuente | object | Fuente de información de datos censales |
| 9 | IdLocalidadCensal | localidad_censal_id | int64 | Clave única que identifica la localidad censal  |
| 10 | LocalidadCensal | localidad_censal_nombre | object | Nombre de la localidad censal |
| 11 | Categoria | categoria | object | Categoria de la localidad censal |
| 12 | Latitud | centroide_lat | float64 | Latitud de la localidad |
| 13 | Longitud | centroide_lon | float64 | Longitud de la localidad |

## **Tabla:** Proveedor
| | Columna Normalizada | Columna Original | Tipo de Dato | Descripción |
|:-------------------:|---|---|---|---|
| 0 | IdProveedor | IDProveedor | int64 | Clave única que identifica al proveedor |
| 1 | Proveedor | Nombre | object | Nombre del proveedor |
| 2 | Domicilio | Address | object | Domicilio del proveedor |
| 3 | Ciudad | City | object | Ciudad del proveedor |
| 4 | Provincia | State | object | Provincia del proveedor |
| 5 | Pais | Country | object | Pais del proveedor |
| 6 | Departamento | departamen | object | Departamento del proveedor |

## **Tabla:** Sucursal
| | Columna Normalizada | Columna Original | Tipo de Dato | Descripción |
|:-------------------:|---|---|---|---|
| 0 | IdSucursal | ï»¿ID | int64 | Clave única que identifica la sucursal |
| 1 | Sucursal | Sucursal | object | Nombre de la sucursal |
| 2 | Domicilio | Direccion | object | Domicilio de la sucursal |
| 3 | Localidad | Localidad | object | Localidad de la sucursal |
| 4 | Provincia | Provincia | object | Provincia de la sucursal |
| 5 | Latitud | Latitud | float64 | Latitud de la sucursal |
| 6 | Longitud | Longitud | float64 | Longitud de la sucursal |

## **Tabla:** Venta
| | Columna Normalizada | Columna Original | Tipo de Dato | Descripción |
|:-------------------:|---|---|---|---|
| 0 | IdVenta | IdVenta | int64 | Clave única que identifica la venta |
| 1 | Fecha | Fecha | datetime64 | Fecha de la venta realizada |
| 2 | Fecha_Entrega | Fecha_Entrega | datetime64 | Fecha de entrega de la venta realizada |
| 3 | IdCanal | IdCanal | int64 | Clave única que identifica el canal de venta |
| 4 | IdCliente | IdCliente | int64 | Clave única que identifica al cliente |
| 5 | IdSucursal | IdSucursal | int64 | Clave única que identifica a la sucursal |
| 6 | IdEmpleado | IdEmpleado | int64 | Clave única que identifica al empleado |
| 7 | IdProducto | IdProducto | int64 | Clave única que identifica el producto de la venta|
| 8 | Precio | Precio | float64 | Precio total de la venta realizada |
| 9 | Cantidad | Cantidad | float64 | Cantidad de producto de la venta realizada |