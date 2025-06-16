# opensource-datalake

Este proyecto permite la creación de un datalake utilizando las siguientes tecnologías:

- **Kafka + Zookeeper**: Para la ingesta y gestión de flujos de datos.
- **MinIO**: Almacenamiento de objetos compatible con S3.
- **Apache NiFi**: Orquestación y procesamiento de flujos de datos.
- **Producer en Python**: Genera y envía datos a Kafka.

## Despliegue

Se proporcionan los manifiestos necesarios para desplegar cada servicio en Kubernetes. Cada carpeta contiene los archivos requeridos para su despliegue y configuración. Todos los servicios están preconfigurados para funcionar correctamente sin necesidad de ajustes adicionales.

## Estructura del repositorio

- `producer/`: Código fuente del producer en Python.
- `kafka-zookeeper/`: Manifiestos para Kafka y Zookeeper.
- `minio/`: Manifiestos para MinIO.
- `nifi/`: Manifiestos para Apache NiFi.

## Requisitos

- Docker
- Kubernetes cluster
- `kubectl` configurado

## Uso

1. Crea un secreto con las credenciales de MinIO. Por ejemplo:
```sh
kubectl create secret generic minio-credentials \
  --from-literal=MINIO_ACCESS_KEY=minioadmin \
  --from-literal=MINIO_SECRET_KEY=minioadmin
```
2. Despliega Kafka, Zookeeper, Nifi y MinIO ejecutando los manifiestos de cada carpeta.
3. Inicia el producer con Python para alimentar Kafka con datos (recuerda ajustar los valores necesarios). Se recomienda utilizar el Dockerfile para crear una imagen y el manifiesto para desplegarla en el clúster Kubernetes.