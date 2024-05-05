# Cluster_Champion

[Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Cluster_Champion.git)

---

Hemos seguido realizando la tarea de la champions. En esta entrega, nos hemos centrado en los clusters y hemos hecho uso de series temporales para predecir la prediccion del modelo.

---

## Indice
- [Web Scrapping](#webscrapping)
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
  - [Random Forest](#randomforest)
  - [Gradient Boosting](#gradientboosting)
  - [Autoregressive](#autoregressive)
  - [Exponential Smoothing](#exponentialsmoothing)
  - [Arima](#arima)
  - [Sarimax](#sarimax)
  - [Regresión Lineal](#regresionlineal)
  - [Monte Carlo](#montecarlo)
- [Gradio && Llama3](#gradiou)

---

## Web Scrapping <a name="webscrapping"></a>

El primer paso de este proyecto, como cualquier otro relacionado con la Inteligencia Artificial, son los datos, ya que esto es la base de la IA. Para ello, hemos recaudado dichos datos utilizando diversas técnicas de Web Scrapping, provenientes de [esta](https://fbref.com/en/comps/8/Champions-League-Stats) página web, ya que ofrece información actualizada y relativamente fácil de realizar un scrapping de la Uefa Champions League UCL.

<br>

En cuanto al scrapping, hemos hecho diversos tipos, tales como un scrapping de la clasificación global del torneo, como de jugadores, goleadores, porteros, logos de equipos, etc. Todo ello para mejorar los modelos de IA que hemos usado para predecir la futura clasificación de este torneo (series temporales, regresión lineal, monte carlo...) de manera que conseguimos una métrica adicional para mejorar el rendimiento y desempeño, y, sobre todo, fiabilidad de la predicción.

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

Una de las partes más importantes de este proyecto, es predecir el ganador de la Champions. Para ello, hemos hecho uso de Series Temporales (arima, sarimax, etc.) y otros modelos de predicción como la Regresión Lineal, Random Forest, e incluso otros algoritmos como el famoso Monte Carlo. Estos datos están actualizados hasta las semifinales, por lo que en las predicciones lo único que va a cambiar son los 4 primeros equipos, y los demas se quedarán fijos en la clasificación al estar ya eliminados.

<br>

Cabe destacar que el resultado de estas predicciones las hemos modificado según los jugadores que componen su equipo en base al scrapping de jugadores que mencionamos anteriormente, aumentando así las probabilidades de acierto de los modelos.

El resultado de dichas predicciones es el siguiente:

---

#### Random Forest <a name="randomforest"></a>

| Squad           | Prediction |
|-----------------|------------|
| Bayern Munich   | W          |
| Paris S-G       | F          |
| Real Madrid     | SF         |
| Dortmund        | SF         |
| Manchester City | QF         |
| Atlético Madrid | QF         |
| Barcelona       | QF         |
| Arsenal         | QF         |
| Porto           | R16        |
| Inter           | R16        |
| RB Leipzig      | R16        |
| Lazio           | R16        |
| Real Sociedad   | R16        |
| Napoli          | R16        |
| PSV Eindhoven   | R16        |
| FC Copenhagen   | R16        |
| Shakhtar        | GR         |
| Milan           | GR         |
| Lens            | GR         |
| Feyenoord       | GR         |
| Newcastle Utd   | GR         |
| Galatasaray     | GR         |
| Manchester Utd  | GR         |
| Benfica         | GR         |
| RB Salzburg     | GR         |
| Young Boys      | GR         |
| Braga           | GR         |
| Celtic          | GR         |
| Antwerp         | GR         |
| Union Berlin    | GR         |
| Sevilla         | GR         |
| Red Star        | GR         |

---

#### Gradient Boosting <a name="gradientboosting"></a>

| Squad           | Prediction |
|-----------------|------------|
| Bayern Munich   | W          |
| Dortmund        | F          |
| Real Madrid     | SF         |
| Paris S-G       | SF         |
| Manchester City | QF         |
| Atlético Madrid | QF         |
| Barcelona       | QF         |
| Arsenal         | QF         |
| Porto           | R16        |
| Inter           | R16        |
| RB Leipzig      | R16        |
| Lazio           | R16        |
| Real Sociedad   | R16        |
| Napoli          | R16        |
| PSV Eindhoven   | R16        |
| FC Copenhagen   | R16        |
| Shakhtar        | GR         |
| Milan           | GR         |
| Lens            | GR         |
| Feyenoord       | GR         |
| Newcastle Utd   | GR         |
| Galatasaray     | GR         |
| Manchester Utd  | GR         |
| Benfica         | GR         |
| RB Salzburg     | GR         |
| Young Boys      | GR         |
| Braga           | GR         |
| Celtic          | GR         |
| Antwerp         | GR         |
| Union Berlin    | GR         |
| Sevilla         | GR         |
| Red Star        | GR         |

---

#### Autoregressive <a name="autoregressive"></a>

| Squad           | Prediction |
|-----------------|------------|
| Bayern Munich   | W          |
| Paris S-G       | F          |
| Real Madrid     | SF         |
| Dortmund        | SF         |
| Manchester City | QF         |
| Atlético Madrid | QF         |
| Barcelona       | QF         |
| Arsenal         | QF         |
| Porto           | R16        |
| Inter           | R16        |
| RB Leipzig      | R16        |
| Lazio           | R16        |
| Real Sociedad   | R16        |
| Napoli          | R16        |
| PSV Eindhoven   | R16        |
| FC Copenhagen   | R16        |
| Shakhtar        | GR         |
| Milan           | GR         |
| Lens            | GR         |
| Feyenoord       | GR         |
| Newcastle Utd   | GR         |
| Galatasaray     | GR         |
| Manchester Utd  | GR         |
| Benfica         | GR         |
| RB Salzburg     | GR         |
| Young Boys      | GR         |
| Braga           | GR         |
| Celtic          | GR         |
| Antwerp         | GR         |
| Union Berlin    | GR         |
| Sevilla         | GR         |
| Red Star        | GR         |

---

#### Exponential Smoothing <a name="exponentialsmoothing"></a>

| Squad           | Prediction |
|-----------------|------------|
| Bayern Munich   | W          |
| Paris S-G       | F          |
| Real Madrid     | SF         |
| Dortmund        | SF         |
| Manchester City | QF         |
| Atlético Madrid | QF         |
| Barcelona       | QF         |
| Arsenal         | QF         |
| Porto           | R16        |
| Inter           | R16        |
| RB Leipzig      | R16        |
| Lazio           | R16        |
| Real Sociedad   | R16        |
| Napoli          | R16        |
| PSV Eindhoven   | R16        |
| FC Copenhagen   | R16        |
| Shakhtar        | GR         |
| Milan           | GR         |
| Lens            | GR         |
| Feyenoord       | GR         |
| Newcastle Utd   | GR         |
| Galatasaray     | GR         |
| Manchester Utd  | GR         |
| Benfica         | GR         |
| RB Salzburg     | GR         |
| Young Boys      | GR         |
| Braga           | GR         |
| Celtic          | GR         |
| Antwerp         | GR         |
| Union Berlin    | GR         |
| Sevilla         | GR         |
| Red Star        | GR         |

---

#### Arima <a name="arima"></a>

| Squad           | Prediction |
|-----------------|------------|
| Paris S-G       | W          |
| Bayern Munich   | F          |
| Real Madrid     | SF         |
| Dortmund        | SF         |
| Manchester City | QF         |
| Atlético Madrid | QF         |
| Barcelona       | QF         |
| Arsenal         | QF         |
| Porto           | R16        |
| Inter           | R16        |
| RB Leipzig      | R16        |
| Lazio           | R16        |
| Real Sociedad   | R16        |
| Napoli          | R16        |
| PSV Eindhoven   | R16        |
| FC Copenhagen   | R16        |
| Shakhtar        | GR         |
| Milan           | GR         |
| Lens            | GR         |
| Feyenoord       | GR         |
| Newcastle Utd   | GR         |
| Galatasaray     | GR         |
| Manchester Utd  | GR         |
| Benfica         | GR         |
| RB Salzburg     | GR         |
| Young Boys      | GR         |
| Braga           | GR         |
| Celtic          | GR         |
| Antwerp         | GR         |
| Union Berlin    | GR         |
| Sevilla         | GR         |
| Red Star        | GR         |

---

#### Sarimax <a name="sarimax"></a>

| Squad           | Prediction |
|-----------------|------------|
| Bayern Munich   | W          |
| Paris S-G       | F          |
| Real Madrid     | SF         |
| Dortmund        | SF         |
| Manchester City | QF         |
| Atlético Madrid | QF         |
| Barcelona       | QF         |
| Arsenal         | QF         |
| Porto           | R16        |
| Inter           | R16        |
| RB Leipzig      | R16        |
| Lazio           | R16        |
| Real Sociedad   | R16        |
| Napoli          | R16        |
| PSV Eindhoven   | R16        |
| FC Copenhagen   | R16        |
| Shakhtar        | GR         |
| Milan           | GR         |
| Lens            | GR         |
| Feyenoord       | GR         |
| Newcastle Utd   | GR         |
| Galatasaray     | GR         |
| Manchester Utd  | GR         |
| Benfica         | GR         |
| RB Salzburg     | GR         |
| Young Boys      | GR         |
| Braga           | GR         |
| Celtic          | GR         |
| Antwerp         | GR         |
| Union Berlin    | GR         |
| Sevilla         | GR         |
| Red Star        | GR         |

---

#### Regresión Lineal <a name="regresionlineal"></a>

| Squad           | Prediction |
|-----------------|------------|
| Real Madrid     | W          |
| Paris S-G       | F          |
| Bayern Munich   | SF         |
| Dortmund        | SF         |
| Manchester City | QF         |
| Atlético Madrid | QF         |
| Barcelona       | QF         |
| Arsenal         | QF         |
| Porto           | R16        |
| Inter           | R16        |
| RB Leipzig      | R16        |
| Lazio           | R16        |
| Real Sociedad   | R16        |
| Napoli          | R16        |
| PSV Eindhoven   | R16        |
| FC Copenhagen   | R16        |
| Shakhtar        | GR         |
| Milan           | GR         |
| Lens            | GR         |
| Feyenoord       | GR         |
| Newcastle Utd   | GR         |
| Galatasaray     | GR         |
| Manchester Utd  | GR         |
| Benfica         | GR         |
| RB Salzburg     | GR         |
| Young Boys      | GR         |
| Braga           | GR         |
| Celtic          | GR         |
| Antwerp         | GR         |
| Union Berlin    | GR         |
| Sevilla         | GR         |
| Red Star        | GR         |

---

#### Monte Carlo <a name="montecarlo"></a>

| Squad           | Win Probability (%) |
|-----------------|---------------------|
| Bayern Munich   | 28.9                |
| Real Madrid     | 26.7                |
| Dortmund        | 25.7                |
| Paris S-G       | 18.7                |
| Manchester City | 0.0                 |
| Atlético Madrid | 0.0                 |
| Barcelona       | 0.0                 |
| Arsenal         | 0.0                 |
| Porto           | 0.0                 |
| Inter           | 0.0                 |
| RB Leipzig      | 0.0                 |
| Lazio           | 0.0                 |
| Real Sociedad   | 0.0                 |
| Napoli          | 0.0                 |
| PSV Eindhoven   | 0.0                 |
| FC Copenhagen   | 0.0                 |
| Shakhtar        | 0.0                 |
| Milan           | 0.0                 |
| Lens            | 0.0                 |
| Feyenoord       | 0.0                 |
| Newcastle Utd   | 0.0                 |
| Galatasaray     | 0.0                 |
| Manchester Utd  | 0.0                 |
| Benfica         | 0.0                 |
| RB Salzburg     | 0.0                 |
| Young Boys      | 0.0                 |
| Braga           | 0.0                 |
| Celtic          | 0.0                 |
| Antwerp         | 0.0                 |
| Union Berlin    | 0.0                 |
| Sevilla         | 0.0                 |
| Red Star        | 0.0                 |

---

## Interfaz con Gradio y Llama3 <a name="gradiou"></a>



---
