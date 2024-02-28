# Cluster_Champion

[Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Cluster_Champion.git)

---

Hemos seguido realizando la tarea de la champions. En esta entrega, nos hemos centrado en los clusters y hemos hecho uso de series temporales para predecir la prediccion del modelo.

---

## Indice
- [Clusterizacion](#cluster)
  - [K-Means](#kmeans)
  - [Mean-Shift](#meanshift)
  - [Mini-Batch](#minibatch)
  - [DBSCAN](#dbscan)
  - [HDBSCAN](#hdbscan)
  - [OPTICS](#optics)
  - [GMM](#gmm)
  - [Agglomerative](#agglomerative)
- [Series Temporales](#serie)

---

## Clusterizacion <a name="cluster"></a>

Hemos realizado diferentes técnicas de clusterización, entre las que podemos destacar las técnicas de aprendizaje no supervisado, como la clusterización basada en centroides, en densidad, distribucion y hierarchical clustering. Podemos observar que la clusterizacion es diferente para cada caso:

---

#### K-Means <a name="kmeans"></a>

![Kmeans](https://github.com/rnoguer22/Cluster_Champion/blob/main/Clusters/CentroidClustering/img/kmeans/kmeans-GD-Attendance.png)

---

#### Mean-Shift <a name="meanshift"></a>

![Mean-Shift](https://github.com/rnoguer22/Cluster_Champion/blob/main/Clusters/CentroidClustering/img/mean-shift/mean-shift-GD-Attendance.png)

---

#### Mini-Batch <a name="minibatch"></a>

![Mini Batch](https://github.com/rnoguer22/Cluster_Champion/blob/main/Clusters/CentroidClustering/img/minibatch/minibatch-GD-Attendance.png)

---

#### DBSCAN <a name="dbscan"></a>

![DBSCAN](https://github.com/rnoguer22/Cluster_Champion/blob/main/Clusters/DensityClustering/img/dbscan/dbscan-GD-Attendance.png)

---

#### HDBSCAN <a name="hdbscan"></a>

![HDBSCAN](https://github.com/rnoguer22/Cluster_Champion/blob/main/Clusters/DensityClustering/img/hdbscan/hdbscan-GD-Attendance.png)

---

#### OPTICS <a name="optics"></a>

![OPTICS](https://github.com/rnoguer22/Cluster_Champion/blob/main/Clusters/DensityClustering/img/optics/optics-GD-Attendance.png)

---

#### GMM <a name="gmm"></a>

![GMM](https://github.com/rnoguer22/Cluster_Champion/blob/main/Clusters/DistributionClustering/img/gmm/gmm-GD-Attendance.png)

---

#### Agglomerative <a name="agglomerative"></a>

![Agglomerative](https://github.com/rnoguer22/Cluster_Champion/blob/main/Clusters/HierarchicalClustering/img/agglomerative/agglomerative-GD-Attendance.png)

---

## Series Temporales <a name="serie"></a>

Al realizar la prediccion por series temporales, la mejor prediccion resulto ser la arima, con los siguientes resultados (aunque hay que mejorarlos ya que no son muy precisos xd)

| Squad             | Prediction |
|-------------------|------------|
| Manchester City   | GR         |
| Real Madrid       | GR         |
| Bayern Munich     | GR         |
| Porto             | R16        |
| Inter             | F          |
| Atlético Madrid   | GR         |
| Arsenal           | GR         |
| Barcelona         | R16        |
| Lazio             | R16        |
| Dortmund          | QF         |
| Real Sociedad     | SF         |
| RB Leipzig        | F          |
| Paris S-G         | GR         |
| Napoli            | GR         |
| PSV Eindhoven     | GR         |
| FC Copenhagen     | GR         |
| Shakhtar          | R16        |
| Milan             | R16        |
| Lens              | R16        |
| Feyenoord         | QF         |
| Newcastle Utd     | QF         |
| Galatasaray       | SF         |
| Manchester Utd    | SF         |
| Benfica           | F          |
| RB Salzburg       | W          |
| Young Boys        | GR         |
| Braga             | GR         |
| Celtic            | GR         |
| Antwerp           | GR         |
| Union Berlin      | GR         |
| Sevilla           | GR         |
| Red Star          | R16        |
