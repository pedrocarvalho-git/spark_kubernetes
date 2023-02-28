# Spark on Kubernetes
Recentemente tivemos o interesse de testar o [spark-on-k8s-operator](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator). Esse operador permite o uso e o gerenciamento do Spark pelo Kubernetes.

O uso dessa forma nós dara maior portabilidade do ambiente, mais controle sobre as versões e um ambiente mais controlavel.

## Primeiras impressões
Seguimos o tutorial de instalação descrito no site. O repositório nos prove um template _Helm_, que é bem simples e objetivo. 

Porém, durante a instalação em nosso ambiente de homologação encontramos alguns problemas que tivemos que adaptar:

*  **Readiness e Liveness Probe**: O template helm que nós é fornecido, não possui esses dois parametros no manifesto de deploy. Encontramos um [Pull Request](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/pull/1628/files) que estava aberto no repositório, que continha exatamente essa alteração que pensavamos em fazer, usamos o código como referência. Além disso apontamos os dois parametros, para o endpoint `/metrics` do driver.

* **Imagens Docker**: Para subirmos a aplicação com sucesso, foi necessário subir as imagens docker em nosso repositorio privado o _harbor_.

* **Node Selector**: Mesmo sendo permitdo passar esse parametro, acabamos tendo um problema referente ao _helm_, que estava gerando os manifestos de forma erronea. Identificamos que o erro estava acontecendo por conta de uma [issue](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/issues/1393) que ainda não tinha sido resolvida. Para resolver o problema, utilizamos como referencia o [Pull Request](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/pull/1633) que estava atrelado a issue.

* **Webhook Cleanup Job**: Para usar um PersistentVolume o spark-on-k8s-operator, precisa que o webhook esteja habilitado. Ao ativarmos, encontramos um erro no manifesto `webhook-cleanup-job.yaml`, que estava escrito de forma erronea. Para resolver o problema resolvemos a linha que continha o valor `{{ .Values.webhook.enable }}`.

A partir disso, conseguimos instalar o spark-on-k8s-operator com sucesso em nosso cluster de homologação.

## Adaptações
Para que consiguessimos utilizar o chart do spark-operator com sucesso, fizemos um fork e aplicamos as seguintes alterações:
* Inclusão do Readiness and LivenessProbe (deployment.yaml).
* Correção do bug ao passar o NodeSelector (webhook-cleanup-job.yaml e webhook-init-job.yaml).
* Subida das imagens no Harbor.

## Como instalar/executar
Acesse nossa [documentação de instalação/execução](examples/README.md).
