
---
## AWS S3 + Python (probando - intentando)
---

Instalar la librería *boto3*
```bash
$ pip install boto3
```

**Nota:** si ya configuramos la AWS CLI (*aws configure*) los siguientes dos pasos no son necesarios, dado que al hacer el *aws configure* ya nos guarda las credenciales de acceso y la región.

Configurar (o verificar) las credenciales de acceso en el archivo:  ~/.aws/credentials
```bash
$ vi .aws/credentailes
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
```

Configurar la región que vamos a usar por defecto, en el archivo: ~/.aws/config
```bash
$ vi .aws/config
[default]
output = json
region = us-west-2
```


Ref:
* [Boto 3 - The AWS SDK for Python](https://github.com/boto/boto3#boto-3---the-aws-sdk-for-python)
*
