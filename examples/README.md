## Como Instalar
Para instalar o spark-on-k8s-operator, execute o comando:
```shell
helm install v3.0.0 charts/spark-operator -f examples/operator-config.yaml --namespace spark --create-namespace
```
Os manifestos irão ser instalados no namespace `spark`.

## Como executar os exemplos
Testamos a instalação/funcionamento do spark-on-k8s-operator com alguns exemplos, e os versionamos neste repositório.

### PI
É a copia de um exemplo utilizado pelo proprio Spark para testar se a aplicação está funcionando como esperado. Caso você deseje executar uma aplicação de exemplo, execute o comando:
```shell
kubectl apply -f examples/spark-py-pi.yaml
```

### Read Blob
Tem a principal funcionalidade de testar a execução da leitura de um csv, que está no `Blob Storage`, a partir de um `PersistentVolume`. Para executar o exemplo, execute os passos abaixo:

1. Verifique se os recursos já existem. 
```shell
# Verifique se a secret já existe.
kubectl get secrets -n spark

# Verifique se o PersistentVolume já existe.
kubectl get pvc -n spark
```

Deve ser retornado recursos com o prefixo `vvdevdsdatalake-*`

2. Caso os recursos não existam, crie os recursos executando:
```shell
# Crie a secret de acesso ao Blob Storage.
kubectl create secret generic vvdevdsdatalake-storage --from-literal azurestorageaccountname=<storage-account-name> --from-literal azurestorageaccountkey=<storage-account-key> --type=Opaque -n spark

# Crie o PersistentVolume.
kubectl apply -f examples/persistent-volume.yaml -n spark

# Crie o PersistentVolumeClaim.
kubectl apply -f examples/persistent-volume-claim.yaml -n spark
```

3. Após a criação dos recursos aplique o manifesto da aplicação.
```shell
kubectl apply -f examples/spark-read-blob.yaml -n spark
```

Você pode encontrar o código utilizado para a execução do exemplo em [docker/app.py](../docker/app.py)

4. Caso tenha retornado algum tipo de erro, adeque os manifestos. Qualquer dúvida falar com Eric Venarusso ou Johnatan Santana.
