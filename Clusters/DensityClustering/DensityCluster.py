from Clusters.CentroidClustering.CentroidCluster import CentroidCluster


class DensityCluster(CentroidCluster):

    def __init__(self, data_path, cluster_type:str='kmeans'):
        super().__init__(data_path, cluster_type)
